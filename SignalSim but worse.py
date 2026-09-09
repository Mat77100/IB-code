#made 09/09/26
#bored and wanted to ply VotV, but cant cuz chromebook, so ill make smth instead
import numpy as np
import sounddevice as sd

SampleRate = 44100 
Duration = 2 #Length of messadge in seconds

Noise = np.random.uniform(-1,1,SampleRate*Duration)
Noise = np.convolve(Noise, np.ones(25))
Noise /= 100 #NOISE LOUDNESS

#Crackling, pls improve
Noise[np.random.randint(0,SampleRate-1)] = 1

sd.play(Noise,SampleRate)
sd.wait()
