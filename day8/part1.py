import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])

    nodes = {}

    directions = list(lines[0])

    for line in lines[1:]:
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]

        nodes[node] = [left, right]

    current = "AAA"
    output = 0
    direction_index = 0

    while current != "ZZZ":
        next_direction = 1 if directions[direction_index] == "R" else 0
        current = nodes[current][next_direction]
        output += 1
        direction_index += 1
        direction_index %= len(directions)

    print(output)
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
