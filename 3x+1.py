while True:
    try:
        number = int(input("Insert whole number: "))
        break
    except:
        print("input invalid")

steps = 0
def fun(x):
    global steps
    if x == 1:
        print("enetered 4, 2, 1 loop")
        print(f"it took {steps} steps to reach the loop")
        return 1
    elif x % 2 == 0:
        x = x/2
        steps += 1
        print("even, divide by 2")
        print(x)
        print()
        return fun(x)
    else:
        x = x*3+1
        steps +=1
        print("odd, multiply by three, add one")
        print(x)
        print()
        return fun(x)

print(fun(number))