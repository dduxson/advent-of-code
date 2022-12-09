def MoveHead(dir, head):
    if dir == "R":
        head[0] += 1
    elif dir == "L":
        head[0] -= 1
    elif dir == "U":
        head[1] += 1
    elif dir == "D":
        head[1] -= 1

def MoveTail(head, tail):
    diff = [head[0] - tail[0], head[1] - tail[1]]
    if abs(diff[0]) == 2 or abs(diff[1]) == 2 and abs(diff[0]) == 1:
        tail[0] += 1 if diff[0] > 0 else -1 
    if abs(diff[1]) == 2 or abs(diff[0]) == 2 and abs(diff[1]) == 1:
        tail[1] += 1 if diff[1] > 0 else -1 

def GetLastKnotOccupiedCoordinates(rope_length):
    knots=[]
    for i in range(rope_length):
        knots.append([0,0])
    last_knot_coords = set()

    with open("./2022/9/input.txt", "r") as file: 
        for line in file.read().splitlines():
            dir, count = line.split(" ")
            for i in range(int(count)):
                MoveHead(dir, knots[0])
                
                prev_knot = knots[0]
                for i in range(1, len(knots)):
                    MoveTail(prev_knot, knots[i])
                    prev_knot = knots[i]
                
                last_knot_coords.add(str(prev_knot[0]) + ',' + str(prev_knot[1]))

    return last_knot_coords

def main():
    print(len(GetLastKnotOccupiedCoordinates(2)))
    print(len(GetLastKnotOccupiedCoordinates(10)))

if __name__ == "__main__":
    main()