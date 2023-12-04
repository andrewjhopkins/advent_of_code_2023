import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return

    lines = get_input(sys.argv[1])

    winning_numbers = []
    numbers_owned = []

    for line in lines:

        nums_owned = set()
        win_numbers = set()

        index = line.index(":") + 2

        current_num = ""
        while line[index] != "|":

            if str.isnumeric(line[index]):
                current_num += line[index]
            else:
                if len(current_num) != 0:
                    win_numbers.add(int(current_num))
                    current_num = ""

            index += 1

        index += 1

        while index < len(line):
            if str.isnumeric(line[index]):
                current_num += line[index]
            else:
                if len(current_num) != 0:
                    nums_owned.add(int(current_num))
                    current_num = ""
            index += 1

        if len(current_num) != 0:
            nums_owned.add(int(current_num))

        winning_numbers.append(win_numbers)
        numbers_owned.append(nums_owned)


    copies = [1] * len(lines)
    output = 0

    for i in range(len(winning_numbers)):
        count = 0
        for num in numbers_owned[i]:
            if num in winning_numbers[i]:
                count += 1

        if count > 0:
            for j in range(1, count + 1):
                if (i + j) < len(copies):
                    copies[i + j] += copies[i]

    output = 0
    for copy in copies:
        output += copy

    print(output)
    return

def get_input(file_name):
    lines = []
    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip()
            if len(line) != 0:
                lines.append(list(line))

    return lines

if __name__ == "__main__":
    main()
