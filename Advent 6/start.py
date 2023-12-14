from numpy import prod

def Part1():
    mydict = {}

    with open("Advent 6\input.txt") as f:
        x = f.readlines()
        y = x[0].split()
        z = x[1].split()
        #print(y,z)

        for i in range(1,len(y)):
            mydict[int(y[i])] = int(z[i])

        #print(mydict)

    records = []

    for key in mydict:
        speeds = {}
        for j in range(key):
            remain = key-j
            speeds[j] = j*remain

        recs = []

        for val in speeds.values():
            if int(val) > mydict[key]:
                recs.append(val)

        records.append(len(recs))

    #print(records,"\n",prod(records))

def Part2():
    race = []

    with open("Advent 6\input.txt") as f:
        x = f.readlines()
        y = x[0].split()
        z = x[1].split()
        y.pop(0),z.pop(0)
        
        time = ""
        dis = ""
        for i in range(len(y)):
            time += y[i]
            dis += z[i]
        race = [time,dis]

    records = []
    times = int(race[0])
    dist = int(race[1])
    speeds = {}
    for j in range(times):
        remain = times-j
        speeds[j] = j*remain

    recs = []

    for val in speeds.values():
        if int(val) > dist:
            recs.append(val)

    records.append(len(recs))

    print(prod(records))


Part2()

