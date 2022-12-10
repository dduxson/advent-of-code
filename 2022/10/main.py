def getCycleValues():
    cycle_to_value = {}
    current_value = 1
    current_cycle = 1

    with open("./2022/10/input.txt", "r") as file: 
        for line in file.read().splitlines():
            if(line == "noop"):
                cycle_to_value[current_cycle] = current_value
                current_cycle += 1
            elif line.startswith("addx"):
                new_value = current_value + int(line[5:])
                cycle_to_value[current_cycle] = current_value
                cycle_to_value[current_cycle+1] = current_value
                cycle_to_value[current_cycle+2] = new_value
                current_cycle += 2
                current_value = new_value
    
    return cycle_to_value

def renderPixels(cycle_values):
    line_length = 40
    pixel_line = ""

    for i in range(0, len(cycle_values)):
        render_pixel = i % line_length
        sprit_pixel = cycle_values[i+1]
        if render_pixel >= sprit_pixel-1 and render_pixel <= sprit_pixel+1:
            pixel_line += "#"
        else:
            pixel_line += "."
        if len(pixel_line) == line_length:
            print(pixel_line)
            pixel_line = ""

def main():
    cycle_values = getCycleValues()
    sum = 0
    for i in range(20, 221, 40):
        sum += (i * cycle_values[i])
    print(sum)

    renderPixels(cycle_values)
    

if __name__ == "__main__":
    main()