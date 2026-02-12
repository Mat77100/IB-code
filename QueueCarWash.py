#last modified 10/11/2025
money = 0
import time
import threading
import random
fame = 2
washlvl = 1
Q = ["null"]*3
front = 0
rear = -1
speed = 2
price = 10

costF = 50
costS = 50
costW = 100
costP = 100

action = int(0)
carNum = 0
shopAct = 0

running = True
lock = threading.Lock()

print("Welcome to my car wash idle game, for now all you need to do is wait for a car to show up, this may take awhile but you can speed it up with upgrades. Have fun! (hit enter to start)")
input()
print("")

def menu():
    global action,Q,money,running,fame,speed,washlvl,price,shopAct,costW,costP,costS,costF
    print("what would you like to do?", flush=True)
    while running:
        with lock:
            print("")
            print("1 - Check cars in wash", flush=True)
            print("2 - Check money", flush=True)
            print("3 - Enter upgrade shop", flush=True)
            print("4 - Save progress to file",flush=True)
            print("5 - load progress from file",flush=True)
            print("6 - Quit", flush=True)
        try:
            action = int(input(">>"))
        except:
            print("\033[31minvalid input\33[0m")
        print("", flush=True)
        if(action==1):
            with lock:
                print("\033[33mcars in wash: \033[0m", Q, flush=True)
                print("")


        if(action==2):
            with lock:
                print("\033[33myou have:\033[0m", flush=True)
                print(f"£{money}", flush=True)
                print("")

        if(action ==3):
            shopAct = 0
            with lock:
                print("\033[33mSTORE:\033[0m", flush=True)
                print(f"1 -- More advertisement - £{costF}, (fame lvl {fame}-->{fame+2})", flush=True)
                print(f"2 -- higher pressure washers - £{costS}, (speed lvl {speed}-->{speed+2})",flush = True)
                print(f"3 -- larger station - £{costW}, (wash lvl {washlvl}-->{washlvl+1}) \033[31m!!WILL REMOVE ALL CARS IN QUEUE!!\033[0m",flush = True)
                print(f"4 -- premium soaps - £{costP}, (income per car {price}-->{price+5})",flush = True)
                print("5 -- leave shop",flush = True)
                print("")
                print("balance: £",money)
                while shopAct > 5 or shopAct < 1:
                    try:
                            shopAct = int(input())
                    except:
                            print("Valid input required")

                if shopAct == 1 and money>=costF:
                    money -= costF
                    fame +=2
                    costF = costF + (costF * 0.5)
                    print("upgrades compleate")
                    print(f"Fame lvl - {fame}")
                    print(f"New balance - £{money}")
                elif shopAct == 3 and money<costF:
                    print("\033[31mnot enough money\033[0m")

                if shopAct == 2 and money>=costS:
                    money -= costS
                    speed +=2
                    costS = costS + (costS * 0.5)
                    print("upgrades compleate")
                    print(f"Speed lvl - {speed}")
                    print(f"New balance - £{money}")
                elif shopAct == 3 and money<costS:
                    print("\033[31mnot enough money\033[0m")

                if shopAct == 3 and money>=costW:
                    money -= costW
                    washlvl += 1
                    Q = ["null"]*(2+washlvl)
                    costW = costW + (costW * 0.5)
                    print("upgrades compleate")
                    print(f"New queue - {Q}")
                    print(f"New balance - £{money}")
                elif shopAct == 3 and money<costW:
                    print("\033[31mnot enough money\033[0m")

                if shopAct == 4 and money>=costP:
                    money -= costP
                    price += 5
                    costP = costP + (costP * 0.5)
                    print("upgrades compleate")
                    print(f"Income per car - £{price}")
                    print(f"New balance - £{money}")
                elif shopAct == 3 and money<costP:
                    print("\033[31mnot enough money\033[0m")

                if shopAct == 5:
                    continue
                
        if(action == 4):
            print("You have one save slot, are you sure you want to overwrite it?")
            yes = input("insert YES to proceed: ").upper()
            if yes == "YES":
                print("Saving...")
                with open("CarWashSaveFile.txt", "w") as save:
                    global front, rear, carNum
                    save.write(str(money)+":")
                    save.write(str(fame)+":")
                    save.write(str(washlvl)+":")
                    for i in range (len(Q)):
                        save.write(Q[i] + " ")
                    save.write(":")
                    save.write(str(front)+":")
                    save.write(str(rear)+":")
                    save.write(str(speed)+":")
                    save.write(str(price)+":")
                    save.write(str(costF)+":")
                    save.write(str(costS)+":")
                    save.write(str(costW)+":")
                    save.write(str(costP)+":")
                    save.write(str(carNum))
                print("Saved!")
        
        if(action == 5):
            print("This will overwrite current progress, are you sure you want to do that?")
            yes = input("insert YES to proceed: ").upper()
            if yes == "YES":
                print("loading...")
                print("\033[31m[shutting down loops]\033[0m")
                running = False
                with open("CarWashSaveFile.txt","r") as save:
                    for line in save:
                        varlist = line.split(":")
                        print(varlist)
                money = int(varlist[0])
                fame = int(varlist[1])
                washlvl = int(varlist[2])
                Q = varlist[3].strip().split(" ")
                front = int(varlist[4])
                rear = int(varlist[5])
                speed = int(varlist[6])
                price = int(varlist[7])
                costF = float(varlist[8])
                costS = float(varlist[9])
                costW = float(varlist[10])
                costP = float(varlist[11])
                carNum = int(varlist[12])
                running = True
                print("\033[31m[loops restarted]\033[0m")
                print("Loaded!")

        if (action == 6):

            print("shutting down...", flush=True)
            running = False
            break

        time.sleep(0.1)

def carArrive():
    global rear,fame,Q,carNum
    while running:
        if not(rear >= len(Q)-1): #while not full
            if(random.randint(1,20) <= fame):
                with lock: #only allows one thread to change the variable at a time, this stops both changing the same variable at the same time
                    rear += 1
                    carNum = carNum + 1
                    Q[rear] = "car" + str(carNum)
                    print("\033[36m A car has arrived!!\033[0m", flush=True)
                    time.sleep(1)
            else:
                time.sleep(1)
        else:
            time.sleep(1)
    print("\033[31m[car loop shut down]\033[0m")


def wash():
    global Q,front,speed,money,rear,price
    while running:
        if not (rear <= -1 or front <= -1): # while not empty
            if(random.randint(1,30) <= speed):
                with lock:
                    print(f"\033[36m{Q[front]} has been cleaned and has paid\033[0m", flush=True)
                    money += price
                    for i in range (front, rear):
                        Q[i] = Q[i+1]
                    Q[rear] = "null"
                    rear -= 1
            else:
                time.sleep(0.5)
        else:
            time.sleep(1)
    print("\033[31m[wash loop shut down]\033[0m")

#this starts the threads, daemon is a backround thread
car_thread = threading.Thread(target = carArrive, daemon =True)
wash_thread = threading.Thread(target = wash, daemon =True)
car_thread.start()
wash_thread.start()

menu()

car_thread.join()
wash_thread.join()

print("Program successfully shut down")
print("Total cars serviced: ",carNum)



