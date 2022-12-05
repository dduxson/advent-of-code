from collections import deque

def ReadFile():
    with open("./2022/5/input.txt", "r") as file: 
        lines=file.read().splitlines()
    return lines

def GetTopElements(stacks):
    result = ""
    for stack in stacks:
        if stack:
            result += stack[0]

    return result

def Compute(lines, multi_mover):
    stacks = [deque()  for i in range(0, (len(lines[0])+1)//4)]

    for line in lines:
        if line and (line.startswith(" ") or line.startswith("[")):
            for i in range(0, len(line), 4):
                if line[i] == '[':
                    stacks[i//4].append(line[i+1])
    
        elif line.startswith("move"):
            components = line.split(' ')
            start_index = int(components[3])-1
            end_index = int(components[5])-1
            num_to_move = int(components[1])
            
            if multi_mover:
                buffer = []
                for i in range(num_to_move):
                    buffer.append(stacks[start_index].popleft())
                for i in range(len(buffer)-1, -1, -1):
                    stacks[end_index].appendleft(buffer[i])
            else:
                for i in range(num_to_move):
                    stacks[end_index].appendleft(stacks[start_index].popleft())
    
    return stacks


def main():
    print(GetTopElements(Compute(ReadFile(), False)))
    print(GetTopElements(Compute(ReadFile(), True)))

if __name__ == "__main__":
    main()