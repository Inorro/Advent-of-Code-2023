import re

def remover(mylist,value):
    return [i for i in mylist if i != value]

def searcher(x):
    if len(str(x[0])) == 3:
        return [x[1]-1,x[1],x[1]+1,x[1]+2,x[1]+3]
    elif len(str(x[0])) == 2:
        return [x[1]-1,x[1],x[1]+1,x[1]+2]
    elif len(str(x[0])) == 1:
        return [x[1]-1,x[1],x[1]+1]
    
def splitter(x):
    split_list = []
    for str in x:
        split_str = re.findall(r'\d+|\D+', str)
        split_list.extend([s for s in split_str if s.strip()])
    return split_list

with open("Advent 3/input","r") as f:
    lines = []
    for line in f:
        lines.append(line)
    
Total = 0
with open("Advent 3/answer","a") as f:
    for y in range(len(lines)-1):
        lines[y] = lines[y].strip("\n")
        #finds values in line
        halfsplit = splitter(lines[y].split("."))
        x = [int(s) for s in halfsplit if s.isdigit()]
        # Creates list of tuples of a number and the index of its first digit
        newlist = []
        for val in x:
            newlist.append((val,lines[y].find(str(val))))
        correct = []
        # This section checks the surroundings of each value on a line for a symbol
        for l in range(len(newlist)):
            indexes = searcher(newlist[l])
            temp = y
            for i in range(3):
                for index in indexes:
                    if temp-1+i < len(lines):
                        if not(lines[(temp-1)+i][index].isdigit() or lines[(temp-1)+i][index] == "."):
                            Total += int(newlist[l][0])
                            correct.append(newlist[l][0])
                    #print(lines[(temp-1)+i][index])
        f.write(f"\n{lines[y]}\n {newlist} \n {indexes} \n {correct} \n")
        

#print("\n",lines[0],"\n",x,"\n",newlist,"\n",indexes,"\n")
#print("\n",lines[0],lines[1])
print(Total)
