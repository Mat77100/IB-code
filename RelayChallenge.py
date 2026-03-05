#made 12/02/2026
import random
import string #for random genaration of letters, got how to from https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
import time
class CommSat:
    def __init__(self,name,ID,signalLoss,currentSignal):
        self.name = name
        self.ID = ID
        self.signalLoss = signalLoss
        self.currentSignal = currentSignal
    def GetName(self):
        return self.name
    def GetID(self):
        return self.ID
    def setCurSig(self,RecivedSig):
        self.currentSignal = RecivedSig
    def processSignal(self):
        return self.currentSignal - self.signalLoss

class relaySat(CommSat):
    def __init__(self,name,ID,signalgain,currentSignal):
        super().__init__(name,ID,0,currentSignal)
        self.signalgain = signalgain
    def processSignal(self):
        return self.currentSignal + self.signalgain

class OldSat(CommSat):
    def __init__(self, name, ID, signalLoss, currentSignal,malfunctionChance):
        super().__init__(name, ID, signalLoss, currentSignal)
        self.malfunctionChance = malfunctionChance
    def processSignal(self):
        RNG = random.randint(1,100)
        if RNG > self.malfunctionChance:
            print("**TRANSMISSION ERROR -- SIGNAL SIGNIFICANTLY REDUCED**")
            return self.currentSignal - self.signalLoss * 2
        else:
            return self.currentSignal - self.signalLoss



def CreateNetwork(size): #genarates a random network comprised of mainly Comm Satellites with a few relay and old satellites
    SatNetwork = []
    for i in range(0,size):
        sat = random.randint(1,6)
        if sat == 1 or sat == 2 or sat == 3:
            SatNetwork.append(CommSat("Standared Communaction Satellite",random.randint(10000,99999),random.randint(5,10),0))
        elif sat == 4:
            SatNetwork.append(relaySat("New High-Power Relay Satellite",random.randint(1000,9999),random.randint(10,15),0))
        elif sat == 6:
            SatNetwork.append(OldSat("Old Weak Satellite",random.randint(100,999),random.randint(10,15),0,random.randint(5,10)))
    return SatNetwork


def SendSignal(SignalStrength, S=0):
    #Base case --> if the signal is below 10%, return 0, if its at the end of the network return the final signal strength
    if (SignalStrength < 10):
        return 0
    elif S == len(SatNetwork):
        return SignalStrength
    
    SatNetwork[S].setCurSig(SignalStrength)
    SignalStrength = SatNetwork[S].processSignal()
    print("New Signal Strength: ",SignalStrength)
    time.sleep(0.5)
    return SendSignal(SignalStrength, S+1)



print("Welcome to the OOP Relay Challenge")
size = -1
while not size > 0:
    try:
        size = int(input("Please enter the size of the satellite network to genarate: (Must be larger than 0) "))
    except:
        print("Input Invalid")
SatNetwork = CreateNetwork(size)

SatNames = "Genarated Network: "
for sat in SatNetwork:
    SatNames = SatNames + " - " + sat.GetName()
print("")
print(SatNames)
print("")
Message = str(input("Now input the message you would like to transmit: "))
print("")
result = SendSignal(100)
if result == 0:
    print("--------------------------------------------------")
    print("**TRANSMISSION FAILED -- SIGNAL STRENGTH TOO LOW**")
    print("--------------------------------------------------")
else:
    print("--------------------------------------------------")
    print("Transmission successfull!")
    print("Final signal strength: ", result,"%")
    MessageCorruption = (100 - result)
    Message = list(Message)
    for i in range(len(Message)):
        if random.randint(1,100) < MessageCorruption/3:
            Message[i] = random.choice(string.printable) #randomly replaces a the selected letter with random punctuation, saw how to genarate random letters like this (random.choice(string.punctuation)) from https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
    Message = "".join(Message)#this line and line 96 were with help from GPT for how to change a char in a string through the indecies
    print("Total Signal Loss: ", MessageCorruption,"%")
    print("Final Message:")
    print(Message)
    print("--------------------------------------------------")

#fix the corruption as it dont work well