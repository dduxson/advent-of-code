def GetPlayerScore(string_to_score):
    player_score = 0
    
    with open("./2022/2/input.txt", "r") as file: 
        for line in file.readlines():
            player_score += string_to_score[line.strip('\n')]

    return player_score

def main():
    string_to_score_1 = {"A X": 4, "A Y": 8,  "A Z": 3, 
                        "B X": 1, "B Y": 5,  "B Z": 9, 
                        "C X": 7,  "C Y": 2,  "C Z": 6}
    string_to_score_2 =  {"A X": 3, "A Y": 4,  "A Z": 8,
                            "B X": 1, "B Y": 5, "B Z": 9,
                            "C X": 2, "C Y": 6, "C Z": 7}

    print(GetPlayerScore(string_to_score_1))
    print(GetPlayerScore(string_to_score_2))

if __name__ == "__main__":
    main()