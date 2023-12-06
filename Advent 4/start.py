def Part1():
    winnum = []
    yournum = []

    with open("Advent 4\input","r") as f:
        for line in f:
            line = line.strip()
            game = line.split(":")
            game = game[1].split("|")
            winnum.append(game[0].split())
            yournum.append(game[1].split())

    total = 0
    for i in range(len(winnum)):
        count = 1
        for item in winnum[i]:
            if item in yournum[i]:
                #print(count)
                count = count*2
        count = int(count/2)
        total += count

    print(total)

def Part2():
    winnum = []
    yournum = []
    games = []

    with open("Advent 4\input","r") as f:
        for line in f:
            line = line.strip()
            game = line.split(":")
            x = game[0].split()
            games.append(x[1])
            game = game[1].split("|")
            winnum.append(game[0].split())
            yournum.append(game[1].split())    
    
    instances = []
    for i in range(len(games)):
        instances.append(1)

    for i in range(len(winnum)):
        for n in range(instances[i]):
            count = 0
            for item in winnum[i]:
                if item in yournum[i]:
                    count += 1
            for _ in range(count):
                instances[_+i+1] += 1

    print(sum(instances))

    

Part2()
