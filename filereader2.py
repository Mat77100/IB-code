data = []

with open("data2.txt","r") as file:
    for line in file: #for every line in the txt doc
        line = line.strip()
        if line: #if the line isnt empty
            line = [item.strip() for item in line.split()] #for every value in line (after the split) get rid of leading spaces
            for i in range(len(line)): #add each value to one big list
                data.append(int(line[i]))
print("decimal:",data)


for j in range (len(data)):
    data[j] = bin(data[j])#converts to binary
print("binary:",data)

with open("binaryData.txt","w") as file: #writes to a new file, w overwrites files with same name
    for e in range(len(data)):
        file.write(data[e])
        file.write(" ")

    