import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])
    output = 0

    for i in range(len(lines)):
        if(get_points(lines[i])):
            output += i + 1

    print(output)
    return


def get_points(line):
    current_index = line.find(": ") + 2

    red = 0
    blue = 0
    green = 0

    while (current_index < len(line)):
        if str.isnumeric(line[current_index]):
            str_val = ""

            while(str.isnumeric(line[current_index])):
                str_val += line[current_index]
                current_index += 1

            val = int(str_val)

            if (line[current_index + 1] == "b"):
                blue += val
                current_index += 5
            elif (line[current_index + 1] == "r"):
                red += val
                current_index += 4
            elif (line[current_index + 1] == "g"):
                green += val
                current_index += 6

        if red > 12 or green > 13 or blue > 14:
            return False

        if current_index < len(line) and line[current_index] == ";":
            red = 0
            blue = 0
            green = 0

        current_index += 1

    return True


def get_input(file_name):
    lines = []
    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip()
            if len(line) != 0:
                lines.append(line)

    return lines

if __name__ == "__main__":
    main()
