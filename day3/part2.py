import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return

    lines = get_input(sys.argv[1])
    output = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]
            if not str.isnumeric(char) and char != ".":
                neighbors = [
                        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1), (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                ]

                numbers = []

                for n in neighbors:
                    if n[0] >= 0 and n[0] < len(lines) and n[1] >= 0 and n[1] < len(lines[n[0]]):
                        if str.isnumeric(lines[n[0]][n[1]]):
                            num = get_number(lines, n[0], n[1])
                            numbers.append(num)

                if len(numbers) == 2:
                    output += (numbers[0] * numbers[1])
    print(output)
    return output


def get_number(lines, i, j):
    line = lines[i]

    num_str = "" + line[j]

    lines[i][j] = "."

    start = j - 1
    end = j + 1

    while (start >= 0 and str.isnumeric(line[start])) or (end < len(line) and str.isnumeric(line[end])):
        if start >= 0 and str.isnumeric(line[start]):
            num_str = line[start] + num_str
            lines[i][start] = "."
            start -= 1

        if (end < len(line) and str.isnumeric(line[end])):
            num_str = num_str + line[end]
            lines[i][end] = "."
            end += 1

    return int(num_str)


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
