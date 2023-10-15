def get_data() -> list:
    file_data = open("day1/data.txt", 'r').read()       ### CHANGE FILE PATH, if running in folder 
    usable = []
    for i in file_data.split("\n\n"):
        usable.append(list(map(int, i.split('\n'))))

    return usable

def solution():
    
    each_total = []

    for i, val in enumerate(get_data()):
        each_total.append(sum(val))

    print(f"Solution of :{max(each_total)}")

    #To calculate part 2 of the question, there are two approch:
    #1) we can either remove max value from list and find the other 2 values
    #2) or we can just run a loop and compare value

    #1)
    top1 = max(each_total)
    each_total.remove(top1)

    top2 = max(each_total)
    each_total.remove(top2)

    top3 = max(each_total)

    print(f"solution of part2: {top1+top2+top3}")

    #2) 
    #you use brain?
    

if __name__ == "__main__":
    solution()