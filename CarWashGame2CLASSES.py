#last modified 05/02/2026
import time
import random

class player:
    def __init__(self, money, fame, costF):
        self.money = money
        self.fame = fame
        self.costF = costF
        #self.locations = []
    def GetMoney(self, Amount):
        self.money =+ Amount
    def GetBalance(self):
        return self.money
    def GetFame(self):
        return self.fame
    def GetCostF(self):
        return self.costF
    def UpgradeFame(self):
        if self.money >= self.costF:
            self.money - costF
            self.costF + (costF * 0.6)
            self.fame + 1
            print(f"Upgrade compleate! Fame at {self.fame}")
        else:
            print("\033[31m**Upgrade Failed** ---> Balance too low\033[0m")
    def GetMoneyPerSecond(self):
        T1 = self.money
        time.sleep(1)
        T2 = self.money
        return T2-VT
    #def GetLocationArr(self):
       # return self.locations
    
    #Being able to open multiple washes wont work, too many things going on for the program.
    #Make so you can open a new type of wash, as progression kind off - unlocking new washes every time. this allows for new ones to be added easily using the WashStation Class

p1 = player(0,1,50)

class WashStation:
    def __init__(self,speed,QueueSlots,FoQ, BoQ):
        self.speed = speed
        self.QueueSlots = QueueSlots
        self.FoQ = FoQ
        self.BoQ = BoQ
        self.Q = ["Empty"]*self.QueueSlots
    def GetCurrentQ(self):
        return self.Q
    def GetSpeed(self):
        return self.speed
    #def AddToQ(self):
        #LOOK AT UML NOW BEFORE ADDING THIS
        '''if not(self.BoQ >= len(self.Q)-1):
            self.BoQ += 1
            self.Q[self.BoQ] = "car"
            print("\033[36m A car has arrived!!\033[0m", flush=True)
        '''#Idea, remove AddToQ, finish the rest of the methods, then when making the subclasses add the appropriate AddToQ method (Car, boat, plane, truck)
    def WashFoQ(self):
        if self.Q[0] != "Empty":
            Selected = self.Q[0]
            dirt = 15*Selected.GetSizeMult()
            while dirt != 0:
                dirt -= 1
                time.sleep(self.speed)
            #shuffle everything forward
            #Pay player
            #Notify of compleation
            
    def UpgradeQ(self):
        
    def UpgradeSpeed(self):
        #add the money check and notification
        self.speed = round(self.speed * 0.75,3)

        
class Vehicles:
    def __init__(self, Pay, WashTime,SizeMult):
        self.pay = Pay
        self.WashTime = WashTime
        self.SizeMult = SizeMult
    def GetPay(self):
        return self.Pay
    def GetWashTime(self):
        return self.WashTime
    def GetSizeMult(self):
        return self.SizeMult

class Cars(Vehicles):
    def __init__(self,Pay,WashTime,SizeMult,FuelTank%,FuelType):
        super().__init__(Pay,WashTime,SizeMult)
        self.FuelTank% = FuelTank%
        self.FuelType = FuelType
    def GetFuelTank%(self):
        return self.FuelTank%
    def GetFuelType(self):
        return self.FuelType
    def Refuel(self):
        if self.FuelTank% > 80:
           print("Car doesn't need fuel")
        elif self.FuelTank% > 50:
            #Different prices for different fuel, make the wash station first for the diff fuel types









price = 10

costS = 50
costW = 100
costP = 100



action = int(0)
carNum = 0
shopAct = 0

running = True
lock = threading.Lock()