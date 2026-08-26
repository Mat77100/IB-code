#25/08/2026
#CLEAN algorythm test
import numpy as np
import matplotlib.pyplot as plt

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
DirtyBeam /= DirtyBeam.max()
plt.plot(TrueArr)
plt.show()
plt.plot(Samples)
plt.show()
plt.plot(DirtyBeam)
plt.show()

#convolve into dirty image
DirtyArr = np.convolve(TrueArr, DirtyBeam, mode="same")
plt.plot(DirtyArr)
plt.show()

def CLEAN(ResidualArr, CLEANcomponents):
    MaxIndex = ResidualArr.argmax()
    MaxBrightness = ResidualArr[MaxIndex]
    
    if MaxBrightness < 0.01:
        return ResidualArr, CLEANcomponents
    component = DirtyBeam * 0.1
    
