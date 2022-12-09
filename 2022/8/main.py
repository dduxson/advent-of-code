def GetHeightsMatrix():
    result = []
    
    with open("./2022/8/input.txt", "r") as file: 
        for line in file.read().splitlines():
            result.append([])
            for char in line:
                result[len(result)-1].append(int(char))
    
    return result

def UpdateVisibleTrees(matrix, row, col, visible_matrix, highest_value, count):
    if matrix[row][col] > highest_value:
        if visible_matrix[row][col] != 1:
            count += 1
            visible_matrix[row][col] = 1
        highest_value = matrix[row][col]
    return highest_value, count

def CountVisibleTrees(matrix):
    visible_matrix = []
    count = 0

    for i in range(len(matrix)):
        visible_matrix.append([0] * len(matrix[0]))

    for row in range (0, len(matrix)):
        highest_value = -1
        #Visible from left
        for col in range(0, len(matrix[i])):
            highest_value, count = UpdateVisibleTrees(matrix, row, col, visible_matrix, highest_value, count)

        highest_value = -1
        #Visible from right
        for col in range(len(matrix[0])-1, -1, -1):
            highest_value, count = UpdateVisibleTrees(matrix, row, col, visible_matrix, highest_value, count)

    for col in range (0, len(matrix[0])):
        highest_value = -1
        #Visible from top
        for row in range(0, len(matrix)):
            highest_value, count = UpdateVisibleTrees(matrix, row, col, visible_matrix, highest_value, count)

        highest_value = -1
        #Visible from bottom
        for row in range(len(matrix)-1, -1, -1):
            highest_value, count = UpdateVisibleTrees(matrix, row, col, visible_matrix, highest_value, count)

    return count

def HighestScenicScore(heights_matrix):
    result = 0

    for row in range (1, len(heights_matrix)-1):
        for col in range(1, len(heights_matrix[row])-1):
            val = heights_matrix[row][col]

            up_score = 0
            for i in range(row-1, -1, -1):
                up_score+=1
                if heights_matrix[i][col] >= val:
                    break

            down_score = 0
            for i in range(row+1, len(heights_matrix)):
                down_score+=1
                if heights_matrix[i][col] >= val:
                    break

            left_score = 0
            for i in range(col-1, -1, -1):
                left_score+=1
                if heights_matrix[row][i] >= val:
                    break

            right_score = 0
            for i in range(col+1, len(heights_matrix[row])):
                right_score+=1
                if heights_matrix[row][i] >= val:
                    break
            
            score = right_score*left_score*down_score*up_score
            if score > result:
                result = score

    return result

def main():
    heights_matrix = GetHeightsMatrix()
    print(CountVisibleTrees(heights_matrix))
    print(HighestScenicScore(heights_matrix))

if __name__ == "__main__":
    main()