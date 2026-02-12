players = ["Annie", "Boris", "Hugh", "Paul", "Robby", "Tammy"]

rounds = [
    [70, 10, 23, 3],     # Annie
    [40, 0, 50, 90],     # Boris
    [60, 38, 42, 90],    # Hugh
    [45, 0, 0, 60],      # Paul
    [55, 0, 15, 10],     # Robby
    [51, 60, 20, 90]     # Tammy
]

totals = [106, 180, 230, 105, 80, 221]



def swapRows(arr, K, L): #swaps rows
    arr[K],arr[L] = arr[L],arr[K]
    return arr[K],arr[L]

#selection sort
for i in range(len(totals)):
    minim = i #presume the first thing is minimum
    for j in range(i+1, len(totals)): #scan through the rest to find anything smaller
        if totals[j] < totals[minim]:
            minim = j #if yes set it as new minimum
    if(minim != i): #if the minimum i
        totals[minim], totals[i] = totals[i], totals[minim]
        players[minim],players[i] = players[i],players[minim]
        swapRows(rounds,minim,i)

print(players)
print(rounds)
print(totals)