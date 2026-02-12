#made 12/02/2026
import random
class CommSat:
    def __init__(self,name,ID,signalLoss,currentSignal):
        self.name = name
        self.ID = ID
        self.signalLoss = signalLoss
        self.currentSignal = currentSignal
    def setCurSig(self,RecivedSig):
        self.currentSignal = RecivedSig
    def processSignal(self):
        return self.currentSignal - self.signalLoss

class relaySat(CommSat):
    def __init__(self,name,ID,signalgain,currentSignal):
        super().__init__(name,ID,currentSignal)
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
            return self.currentSignal - self.signalLoss * random.randint(2,4)
        else:
            return self.currentSignal - self.signalLoss


SatNetwork = []

def MakeNetwork(size):
    for i in range(0,size):
        sat = random.randint(1,3)
        if sat = 1:
        
        elif sat = 2:
        
        elif sat = 3:
