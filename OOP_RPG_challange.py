#OOP coding challenge
#created 28/11/2025

class RPG:
    def __init__(self,name,clas,lvl,HP):
        self.name = name
        self.clas = clas
        self.lvl = lvl
        self.HP = HP
    def intro(self):
        return (f"Greetings! My name is {self.name}. I am a {self.clas} of level {self.lvl}. I have {self.HP} HP")

print("create yotu custom character!")
Iname = str(input("Name your character: "))
Iclas = str(input("Pick its class:" ))
while True:
    try:
        Ilvl = int(input("And its level: "))
        if Ilvl<=0:
            print("")
            print("minimum level is 1")
            print("")
            continue
        break
    except:
        print("")
        print("must be an integer!")
        print("")

while True:
    try:
        IHP = int(input("Now its HP: "))
        if IHP<=0:
            print("")
            print("Cant be already dead (HP wise)")
            print("")
            continue
        break
    except:
        print("")
        print("must be an integer!")
        print("")
print("")

member = RPG(Iname, Iclas, Ilvl, IHP)
print(member.intro())
