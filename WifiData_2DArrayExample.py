wifiData = [
        [0,0,0,8,11,9,15],
        [18,20,97,346,475,433,293,],
        [11,8,63,349,411,522,239,],
        [20,29,89,465,532,529,301,],
        [17,36,96,501,599,0,0,],
        [0,0,0,0,6,3,0,],
        [0,0,1,20,23,17,24,]
]

for r in range (0,7):
    for c in range(0,7):
        print(wifiData[r][c], end= " ")
    print()

maxV = wifiData[0][0]
maxD = 0
maxT = 0

for r in range (0, 7):
    for c in range (0,7):
        if wifiData[r][c]>maxV:
            maxV = wifiData[r][c]
            maxD = r
            maxT = c
print("highest value:", maxV)

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
times=["9am","10am","11am","12am","1pm","2pm","3pm"]

print("what time it occered:", times[maxT])
print("what day it is located in:", days[maxD])

print("")
allAverages = []

for r in range (0, 7):
    total = 0
    for c in range (0,7):
        total += wifiData[r][c]
    average = total/7
    allAverages.append(average)
    print(f"the average number of users on {days[r]} was {average}")
    print("")

H_avg = allAverages[0]
day_of_H_avg = 0

for a in range (0,7):
    if allAverages[a]>H_avg:
        H_avg = allAverages[a]
        day_of_H_avg = a

print(f"the highest amount of network traffic was on {days[day_of_H_avg]} with an average of {H_avg}")