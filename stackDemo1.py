#06/10/2025

stack = []

stack.append("friday")
stack.append("thursday")
stack.append("wednesday")
stack.append("tuesday")
stack.append("monday")

print(stack)

print(stack.pop())
print(stack.pop())

print(stack)

stack.append("sunday")
stack.append("saturday")

print(stack)



limitedStack = []
while len(limitedStack) <= 4:
    limitedStack.append(input("Stack limit is 5 - what is your input: "))
    print(limitedStack)
print("stack full")
