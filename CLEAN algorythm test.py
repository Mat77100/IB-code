#25/08/2026
#CLEAN algorythm test
import numpy as np
import matplotlib.pyplot as plt
import time
N = 256

#True sky/1D arr
TrueArr = np.zeros(N)
TrueArr[60] = 1.0
TrueArr[120] = 0.6
TrueArr[180] = 0.8

#Sampling function and creating the dirty beam
Samples = np.zeros(N)
Samples[N//2] = 1
for x in [5,10,28,42]:
    Samples[N//2 + x] = 1
    Samples[N//2 - x] = 1

#actually making the dirty beam
DirtyBeam = np.fft.ifft(Samples).real
DirtyBeam = np.fft.fftshift(DirtyBeam)
DirtyBeam /= DirtyBeam.max()
plt.plot(TrueArr)
plt.ylim(0, 1)
plt.show()
plt.plot(Samples)
plt.ylim(0, 1)
plt.show()
plt.plot(DirtyBeam)
plt.ylim(-1, 1)
plt.show()

#convolve into dirty image
DirtyArr = np.convolve(TrueArr, DirtyBeam, mode="same")
plt.plot(DirtyArr)
plt.ylim(-1, 1)
plt.show()

def CLEAN(ResidualArr, CLEANcomponents, iteration):
    MaxIndex = ResidualArr.argmax()
    MaxBrightness = ResidualArr.max()
    
    if (MaxBrightness < 0.01) or (iteration == 50):
        return ResidualArr, CLEANcomponents, iteration
    
    component = MaxBrightness * 0.1
    CLEANcomponents.append((MaxIndex,component))

    ScaledDirtyBeam = DirtyBeam * component
    shift = MaxIndex - np.argmax(DirtyBeam)
    ScaledDirtyBeam = np.roll(ScaledDirtyBeam, shift)
    
    ResidualArr = ResidualArr - ScaledDirtyBeam

    
    #plt.plot(ResidualArr)
    #plt.ylim(-1, 1)
    #plt.show
    
    iteration += 1
    return CLEAN(ResidualArr, CLEANcomponents, iteration)

FinalResidual, FinalCLEANcomp, iteration = CLEAN(DirtyArr,[],0)
plt.plot(FinalResidual)
plt.ylim(-1, 1)
plt.show

