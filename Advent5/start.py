seeds = ""
others = []
with open("Advent5\input") as f:
    lines = f.readlines()
    first = True
    start = 0
    for line in range(len(lines)):
        #lines[line] = lines[line].strip()
        #print(line)
        if lines[line].isspace() and first == True:
           seeds = lines[start:line]
           first = False
           start = line
        elif lines[line].isspace():
            others.append(lines[start:line])
            start = line
        elif line == len(lines)-1:
            others.append(lines[start:line+1])
                           

seeds = seeds[0].strip()
seeds = seeds.split()
seeds.pop(0)

for i in range(len(others)):
    for j in range(len(others[i])):
        others[i][j] = others[i][j].strip()
    others[i] = list(filter(None,others[i]))

finals = []
for seed in seeds:
    testval = int(seed)
    for maps in others:
        #maps = others[0]
        #print(others[0])
        found = False
        for i in range(1,len(maps)):
            temp = maps[i].split()
            if testval >= int(temp[1]) and testval<= (int(temp[1]) + int(temp[2])):
                #print(int(temp[1]),(int(temp[1]) + int(temp[2])))
                x = testval - int(temp[1])
                testval = int(temp[0]) + x
                found = True
                #print(testval,i,"\n")
            if not(found):
                testval = testval
    finals.append(testval)
            
    #print("\n------------------------------\n")
#print(testval)
#print(others)
# print(seeds)
print(finals,min(finals))