import random
import time
import string
while True:
    e = str("\033[0;32m")
    for i in range(0,979):
        e += str((random.choice(string.hexdigits)))
    print(e)