def Part_one():
    with open('input') as f:
        possible_games = 0
        for line in f:
            possible = True
            line = line.split(':')
            game = line[0]
            line[1] = line[1].replace("\n","")
            sections = line[1].split(';')
            for item in sections:
                temp = item.split(",")
                for y in range(len(temp)):
                    if "blue" in temp[y]:
                        x = [int(s) for s in temp[y].split() if s.isdigit()]
                        if x[0] > 14:
                            possible = False
                    elif "red" in temp[y]:
                        x = [int(s) for s in temp[y].split() if s.isdigit()]
                        if x[0] > 12:
                            possible = False
                    elif "green" in temp[y]:
                        # Splits string by whitespaces checks if theres an int in the string
                        #  and then return that int into a new list x
                        x = [int(s) for s in temp[y].split() if s.isdigit()]
                        if x[0] > 13:
                            possible = False
            if possible:
                x = [int(s) for s in game.split() if s.isdigit()]
                possible_games += x[0]
                print("possible", game,sections,possible_games,"\n")
            else:
                print("not possible: ",game,sections,"\n")

def Part_Two():
    with open('input') as f:
        total = 0
        for line in f:
            blu_min,red_min,grn_min = 0,0,0
            line = line.split(':')
            game = line[0]
            line[1] = line[1].replace("\n","")
            sections = line[1].split(';')
            for item in sections:
                temp = item.split(",")
                for y in range(len(temp)):
                    if "blue" in temp[y]:
                        x = [int(s) for s in temp[y].split() if s.isdigit()]
                        if blu_min == 0 or x[0] > blu_min:
                            blu_min = x[0]
                    elif "red" in temp[y]:
                        x = [int(s) for s in temp[y].split() if s.isdigit()]
                        if red_min == 0 or x[0] > red_min:
                            red_min = x[0]
                    elif "green" in temp[y]:
                        # Splits string by whitespaces checks if theres an int in the string
                        #  and then return that int into a new list x
                        x = [int(s) for s in temp[y].split() if s.isdigit()]
                        if grn_min == 0 or x[0] > grn_min:
                            grn_min = x[0]
            total += (red_min * blu_min * grn_min)
            #print(sections,red_min,blu_min,grn_min,"\n")
        print(total)

Part_Two()


