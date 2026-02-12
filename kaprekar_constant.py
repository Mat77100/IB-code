while True:
    try:
        firstNum = int(input("insert a 4 digit number (e.g 2843): "))
        while firstNum < 1000 or firstNum > 9999 or firstNum in [1111,2222,3333,4444,5555,6666,7777,8888,9999]:
            firstNum = int(input("input has to be 4 digits or cant be the same digits >>  Kaprekar consistent."))
        break
    except:
        print("input invalid")

steps = -1

def kap(firstNum):
    
    global steps
    steps = steps +1
    if firstNum == 6174:
        return 6174
    else:
        d1= (firstNum//1000)
        #print(d1)

        d2= ((firstNum%1000)//100)
        #print(d2)

        d3= (((firstNum%1000)%100)//10)
        #print(d3)

        d4= ((((firstNum%1000)%100)%10)//1)
        #print(d4)

        list1 = [d1,d2,d3,d4]
        list1.sort() #sorts them in ascending order
        A_Num = int("".join(str(d) for d in list1)) #joins all the digits in the list without a space
        #print(A_Num)

        list1 = [d1,d2,d3,d4]
        list1.sort(reverse=True) #sorts them in descending order
        D_Num = int("".join(str(d) for d in list1)) #joins all the digits in the list without a space
        #print(D_Num)

        if A_Num > D_Num:
            firstNum = A_Num - D_Num
            print(f"{A_Num}-{D_Num}")
        if A_Num < D_Num:
            firstNum = D_Num - A_Num
            print(f"{D_Num}-{A_Num}")
        print(firstNum)
        print("")
        return kap(firstNum)
        
print(kap(firstNum))
print("amount of steps:",steps)
