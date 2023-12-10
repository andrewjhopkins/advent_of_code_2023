# Not proud of this solution. Very hacked together
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    grid = get_input(sys.argv[1])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                # try each direction
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

                for n in neighbors:
                    length = dfs(grid, n[0], n[1], i, j, 0)
                    # if no loop return 0
                    if length == 0:
                        continue
                    else:
                        if length % 2 == 0:
                            print(length // 2)
                        else:
                            print((length // 2) + 1)
                        break
    return

def dfs(grid, start_i, start_j, prev_i, prev_j, count):
    i = start_i
    j = start_j

    pi = prev_i
    pj = prev_j

    count = 0

    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):

        if grid[i][j] == "S":
            #print("S")
            return count

        elif grid[i][j] == "|":
            #print("|")
            if pi == i - 1 and pj == j:
                pi = i
                pj = j
                i = i + 1
                count += 1
                continue
            elif pi == i + 1 and pj == j:
                pi = i
                pj = j
                i = i - 1
                count += 1
                continue
            else:
                return 0

        elif grid[i][j] == "-":
            #print("-")
            if pi == i and pj == j + 1:
                pi = i
                pj = j
                j = j - 1
                count += 1
                continue

            elif pi == i and pj == j - 1:
                pi = i
                pj = j
                j = j + 1
                count += 1
                continue
            else:
                return 0

        elif grid[i][j] == "L":
            #print("L")
            if pi == i - 1 and pj == j:
                pi = i
                pj = j
                j = j + 1
                count += 1
                continue
            elif pi == i and pj == j + 1:
                pi = i
                pj = j
                i = i - 1
                count += 1
                continue
            else:
                return 0

        elif grid[i][j] == "J":
            #print("J")
            if pi == i - 1 and pj == j:
                pi = i
                pj = j
                j = j - 1
                count += 1
                continue
            elif pi == i and pj == j - 1:
                pi = i
                pj = j
                i = i - 1
                count += 1
                continue
            else:
                return 0

        elif grid[i][j] == "7":
            #print("7")
            if pi == i and pj == j - 1:
                pi = i
                pj = j
                i = i + 1
                count += 1
                continue
            elif pi == i + 1 and pj == j:
                pi = i
                pj = j
                j = j - 1
                count += 1
                continue
            else:
                return 0

        elif grid[i][j] == "F":
            #print("F")
            if pi == i + 1 and pj == j:
                pi = i
                pj = j
                j = j + 1
                count += 1
                continue
            elif pi == i and pj == j + 1:
                pi = i
                pj = j
                i = i + 1
                count += 1
                continue
            else:
                return 0

        else:
            return 0

    return count

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
