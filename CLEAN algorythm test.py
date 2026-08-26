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
    MaxIndex = np.argmax(np.abs(ResidualArr))
    MaxBrightness = ResidualArr[MaxIndex]
    
    if (abs(MaxBrightness) < 0.01) or (iteration == 2000):
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

CLEANmap = np.zeros(N)
for i,component in FinalCLEANcomp:
    CLEANmap[i] += component

plt.plot(CLEANmap)
plt.ylim(-1, 1)
plt.show


x = np.arange(N)
centre = N // 2
sigma = 2

CLEANbeam = np.exp(-((x - centre)**2) / (2 * sigma**2))

RestoredArr = np.convolve(CLEANmap, CLEANbeam, mode="same")
plt.figure()
plt.plot(RestoredArr)

plt.show

