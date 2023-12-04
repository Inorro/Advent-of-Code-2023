import re

def searcher(myvalue,index):
    if len(str(myvalue)) == 3:
        return [index-1,index,index+1,index+2,index+3]
    elif len(str(myvalue)) == 2:
        return [index-1,index,index+1,index+2]
    elif len(str(myvalue)) == 1:
        return [index-1,index,index+1]

with open("Advent 3\input.txt","r") as f:
    lines = f.readlines()
    newlist = []
    for line in lines:
        newlist.append(line.strip())

total = 0
temp = []
for row in range(len(newlist)):
    # Goes through line and returns the index and values in the row
    values = list(map(int, re.findall('\d+', newlist[row])))
    indexes = []
    for value in values:
        indexes.append(newlist[row].find(str(value)))

    index_to_be_checked = []
    for i in range(len(indexes)):
        index_to_be_checked.append(searcher(values[i],indexes[i]))


    for l in range(len(index_to_be_checked)):
        adjacent = False

        for ind in index_to_be_checked[l]:
            
            if ind < len(newlist[row]):

                if not(newlist[row-1][ind].isdigit() or newlist[row-1][ind] == "."):
                    adjacent = True
                    total += values[l]
                    temp.append(values[l])

                elif not(newlist[row][ind].isdigit() or newlist[row][ind] == "."):
                    adjacent = False
                    total += values[l]
                    temp.append(values[l])

                elif row < len(newlist)-1:
                    if not(newlist[row+1][ind].isdigit() or newlist[row+1][ind] == "."):
                        adjacent = False
                        total += values[l]
                        temp.append(values[l])
        if adjacent and values[l] not in temp:
            total+= values[l]


#print(total,values,index_to_be_checked,"\n",temp)
print(total)
