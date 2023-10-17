def give_data() -> list:
    raw = open("day2/data.txt").read()

    usable_data = []
    for i in raw.split("\n"):
        temp_use = []

        for j in i.split(" "):
            temp_use.append(j)

        usable_data.append(temp_use)

    return usable_data

def win_status(player, opponent) -> str:
    #win, loss, draw
    pass

def solution() -> None:
    modified = give_data()

    #A = X = 1 = Rock
    #B = Y = 2 = Paper
    #C = Z = 3 = Scissors

    #0 - lost
    #3 - draw
    #6 - won

    key_mapping = {"X": "A","Y": "B","Z": "C"}
    point_mapping = {"AA": 3+1, "BB": 3+2, "CC": 3+3, "AB": 6+2, "AC": 0+3, "BA": 0+1, "BC": 6+3, "CA": 6+1, "CB": 0+2}
    point_mapping2 = {"AA": 0+3, "BB": 3+2, "CC": 6+1, "AB": 3+1, "AC": 6+2, "BA": 0+1, "BC": 6+3, "CA": 0+2, "CB": 3+3}

    point = 0
    point2=0
    for i in give_data():
        player = i[0]
        oppo = key_mapping[i[1]]
        
        point += point_mapping[player+oppo]
        point2 += point_mapping2[player+oppo]

    print(point)
    print(point2)

if __name__ == "__main__":
    solution()
