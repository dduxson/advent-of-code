def GetRange(range_str):
    nums = range_str.split("-")
    return range(int(nums[0]), int(nums[1])+1)

def ComputeOne():
    result = 0

    with open("./2022/4/input.txt", "r") as file: 
        for line in file.readlines():
            ranges = line.strip('\n').split(',')
            range_one, range_two = GetRange(ranges[0]), GetRange(ranges[1])
            if (range_one.start in range_two and range_one[-1] in range_two) or \
                (range_two.start in range_one and range_two[-1] in range_one):
                result += 1

    return result

def ComputeTwo():
    result = 0

    with open("./2022/4/input.txt", "r") as file: 
        for line in file.readlines():
            ranges = line.strip('\n').split(',')
            range_one, range_two = GetRange(ranges[0]), GetRange(ranges[1])
            if range_one.start <= range_two[-1] and range_two.start <= range_one[-1]:
                result += 1

    return result

def main():
    print(ComputeOne())
    print(ComputeTwo())

if __name__ == "__main__":
    main()