#created 07/11/2025
#minesweeper

import time

Bgrid = ["O","O","O","O","O","O","O",],["O","O","O","O","O","O","O",],["O","O","O","O","O","O","O",],["O","O","O","O","O","O","O",],["O","O","O","O","O","O","O",],["O","O","O","O","O","O","O",],
Pgrid = ["■","■","■","■","■","■","■",],["■","■","■","■","■","■","■",],["■","■","■","■","■","■","■",],["■","■","■","■","■","■","■",],["■","■","■","■","■","■","■",],["■","■","■","■","■","■","■",],


#FOR FILE BOMB LOCATIONS
with open("bombLocations.txt", "r") as file:
    for line in file:
        if line:
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace("\n", "")
            line = line.split(",")
            bx = int(line[0])
            by = int(line[1])
            Bgrid[bx][by] = "X"
#END FILE LOCATIONS

'''
#FOR NON FILE LOCATIONS
nonfileBomblocations = [ "(0, 0)",
    "(1, 4)",
    "(2, 1)",
    "(3, 6)",
    "(4, 2)",
    "(5, 5)",
    "(0, 3)",
    "(2, 5)",
    "(1, 0)",
    "(3, 2)",
    "(5, 1)",
    "(4, 6)",
    "(0, 4)",
    "(2, 3)",
    "(1, 6)",
    "(3, 0)",
    "(5, 3)",
    "(4, 1)"]

for i in range(len(nonfileBomblocations)):
    xy = nonfileBomblocations[i]
    xy = xy.replace("(","").replace(")","").replace(" ","")
    xy = xy.split(",")
    bx = int(xy[0])
    by = int(xy[1])
    Bgrid[bx][by] = "X"
#END NON FILE LOCCATIONS
'''



for row in range(len(Bgrid)): #for every element in the bomb array
    for col in range(len(Bgrid[0])):
        if Bgrid[row][col] == "X":
            continue
        else:
            count = 0
            for b in range(row-1, row+2): #scan a 3 x 3 grid around it
                for n in range(col-1,col+2):
                    if b<0 or b>=len(Bgrid) or n<0 or n>=len(Bgrid[0]): #if any indicies are out of range skip them
                        continue
                    elif Bgrid[b][n] == "X": #and increase count by one if theres a bomb
                        count += 1
            Bgrid[row][col] = str(count)



def adjcheck(x,y):
    if (x<0 or x>5) or (y<0 or y>6) or (Bgrid[x][y] == "X"):
        return x,y
    if Pgrid[x][y] != "■":
        return x,y
    if Bgrid[x][y] != "X":
        Pgrid[x][y] = Bgrid[x][y]
        return adjcheck(x+1,y),adjcheck(x-1,y),adjcheck(x,y+1),adjcheck(x,y-1)

num = 0
print("index    1    2    3    4    5    6    7")
for p in range(len(Pgrid)):
    num += 1
    print(num," -- ",Pgrid[p])



while True:
    try:
        Py = int(input("Insert x num(1-7)"))-1
        Px = int(input("Insert y num(1-6)"))-1
        flagmode = str(input("would you like to flag this square? (if yes input y) "))
    except:
        print("input invalid")
        continue

    if Px<0 or Px>5 or Py<0 or Py>6:
        print("values out of range")

    elif flagmode == "y":
        if Pgrid[Px][Py] == "■":
            Pgrid[Px][Py] = "♦"
        else:
            print("tile already uncovered")

    elif Pgrid[Px][Py] == "♦":
        print("tile is flagged, would you like to unflag it?")
        if str(input("(input y to unflag it)")) == "y":
            Pgrid[Px][Py] = "■"

    elif Bgrid[Px][Py] != "X":
        adjcheck(Px,Py)

    else:
        for i in range(20):
            print("\033[0;31m\033[1m\033[5mBOOM\033[0m")
            time.sleep(0.05)

        print("you have lost :(")

        for p in range(len(Bgrid)):
            print(Bgrid[p])
        break

    num = 0
    print("index    1    2    3    4    5    6    7")
    for p in range(len(Pgrid)):
        num += 1
        print(num," -- ",Pgrid[p])




