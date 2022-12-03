def GetCharScore(char):
    if char.isupper():
        return ord(char) - ord('A')+27
    return ord(char) - ord('a')+1

def ComputeOne():
    result = 0

    with open("./2022/3/input.txt", "r") as file: 
        for line in file.readlines():
            compartments = line.strip('\n')
            compartment_one, compartment_two = set(line[:len(line)//2]), set(line[len(line)//2:])
            common_char = compartment_one.intersection(compartment_two).pop()
            result += GetCharScore(common_char)

    return result

def ComputeTwo():
    result = 0

    with open("./2022/3/input.txt", "r") as file: 
        rucksacks = []
        for line in file.readlines():
            rucksacks.append(set(line.strip('\n')))
            
            if len(rucksacks) == 3:
                common_char = rucksacks[0].intersection(rucksacks[1]).intersection(rucksacks[2]).pop()
                result += GetCharScore(common_char)
                rucksacks.clear()

    return result

def main():
    print(ComputeOne())
    print(ComputeTwo())

if __name__ == "__main__":
    main()