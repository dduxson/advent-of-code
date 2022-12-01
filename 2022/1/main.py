def ReadFile():
    with open("./2022/1/input.txt", "r") as file: 
        lines=file.read().splitlines()
    return lines

def GetSortedCalories(lines):
    calorie_values = []
    current_calories = 0

    for line in lines:
        if not line:
            calorie_values.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    
    calorie_values.sort()
    return calorie_values

def main():
    sorted_calories = GetSortedCalories(ReadFile())
    print(sorted_calories[-1])
    print(sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3])

if __name__ == "__main__":
    main()