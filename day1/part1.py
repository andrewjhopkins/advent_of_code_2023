import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])

    sum = 0

    for line in lines:
        first_digit = None
        for i in range(len(line)):
            char = line[i]
            if str.isdigit(char):
                first_digit = char
                break

        last_digit = None
        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if str.isdigit(char):
                last_digit = char
                break

        num_string = first_digit + last_digit

        sum += int(num_string)

    print(sum)
    return 

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
