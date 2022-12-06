def Compute(interval_length):
    start_index = 0
    chars = set()
    test_str = ""
    
    with open("./2022/6/input.txt", "r") as file: 
        test_str = file.read()

    for char in test_str:
        if char not in chars:
            chars.add(char)
            if len(chars) == interval_length:
                return start_index + interval_length
        else:
            while test_str[start_index] != char:
                chars.remove(test_str[start_index])
                start_index += 1
            start_index += 1

    return -1

def main():
    print(Compute(4))
    print(Compute(14))

if __name__ == "__main__":
    main()