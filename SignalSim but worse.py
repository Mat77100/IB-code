#made 09/09/26
#bored and wanted to ply VotV, but cant cuz chromebook, so ill make smth instead
import numpy as np
import sounddevice as sd

Audio = np.random.uniform(1,-1,44100)
sd.play(Audio,44100)
sd.wait
