#method 1
friends = {"Sarah", "Tom", "Emma","Alex"}
#method 2
numbers = set([1,2,3,4,5])
#method 3
empty_set = set()

#might print randomly, theres no indecies
print(friends)

#Check if in set
print("Sarah" in friends) #'True
print("John" in friends) #'false

#adding to the set
friends.add("John")
print(friends)

#attemt adding a duplicate
friends.add("Sarah")
print(friends)

#removing something from the set
friends.discard("Tom")
print(friends)

A = {"Sarah", "Tom",}
B = {"Sarah", "Tom", "Emma","Alex"}

#is A inside B?
print(A.issubset(B)) #True
print(B >= B) #True, shorthand

#is B bigger than A
print(B.issuperset(A)) #True


