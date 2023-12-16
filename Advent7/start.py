mydict = {
    "A":14,
    "K":13,
    "Q":12,
    "J":11,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
    "1":1,
}

def find_duplicate(x):
    list1 = []
    for char in set(x):
        counts=x.count(char)
        list1.append((char,counts))
    return list1

def tosort(e):
    return int(e[1])

def bubsort(arr):
    n = len(arr)
    for q in range(n-1):
        for t in range(n-1-q):
            if arr[t][1] == arr[t+1][1]:
                for r in range(5):
                    if not(arr[t][0][r] == arr[t+1][0][r]):
                        if mydict[arr[t][0][r]] > mydict[arr[t+1][0][r]]:
                            temp = arr[t+1]
                            arr[t+1] = arr[t]
                            arr[t] = temp
                            break
                        else:
                            break
                else:
                    continue

lines = []
bid = []

with open("Advent7\input") as f:
    #counter = 0
    for line in f:
        #counter +=1
        lines.append(line.split()[0])
        bid.append(line.split()[1])
        #if counter == 20:
            #break

ordered = []
for line in lines:
    hand = ""
    dup = find_duplicate(line)
    #print(dup)
    if len(dup) == 1:
        hand = "6"
    elif len(dup) == 2:
        if (dup[0][1] == 4) or (dup[1][1] == 4):
            hand = "5"
        elif (dup[0][1] == 3 and dup[1][1] == 2) or (dup[0][1] == 2 and dup[1][1] == 3):
            hand = "4"
    elif len(dup) == 3:
        pair = 0
        for i in range(len(dup)):
            if dup[i][1] == 2:
                pair +=1
        if pair == 0:
            hand = "3"
        if pair == 2:
            hand = "2"
    elif len(dup) == 4:
        hand = "1"
    elif len(dup) == 5:
        hand = "0"

    toadd = (line,hand)
    ordered.append(toadd)

ordered.sort(key=tosort)
#print(ordered)
bubsort(ordered)
#print(ordered)       
for num in range(len(ordered)):
    ordered[num] = ordered[num][0]
total = 0

for val in range(len(ordered)):
    num = lines.index(ordered[val])
    total += (int(bid[num]) * (val+1))

print(total)
    
        
    