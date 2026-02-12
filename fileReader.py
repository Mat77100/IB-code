data = []
name2 = []

with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.replace("name:", "")
        line = line.replace("phone:", "")
        line = line.replace("email;", "")
        print(line)
        if line:
            parts = line.split(",")
            name = parts[0].strip()
            phone = parts[1].strip().replace(" ", "").replace("-","").replace("(","").replace(")","")
            email = parts[2].strip()
            data.append([name,phone,email])
for row in range(len(data)):
    print(data[row][0] + " " + ("-"*10) + " "  + data[row][1] + " " + ("-"*10) + " "  + data[row][2])
    
