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
                #neighbors = [(i, j + 1)]

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

def dfs(grid, i, j, prev_i, prev_j, count):

    # out of bounds
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return 0
    
    neighbors = []

    if grid[i][j] == "S":
        return count

    elif grid[i][j] == "|":
        #print("|")
        if prev_i == i - 1 and prev_j == j:
            return dfs(grid, i + 1, j, i, j, count + 1)
        elif prev_i == i + 1 and prev_j == j:
            return dfs(grid, i - 1, j, i, j, count + 1)
        else:
            return 0

    elif grid[i][j] == "-":
        #print("-")
        if prev_i == i and prev_j == j + 1:
            return dfs(grid, i, j - 1, i, j, count + 1)
        elif prev_i == i and prev_j == j - 1:
            return dfs(grid, i, j + 1, i, j, count + 1)
        else:
            return 0

    elif grid[i][j] == "L":
        #print("L")
        if prev_i == i - 1 and prev_j == j:
            return dfs(grid, i, j + 1, i, j, count + 1)
        elif prev_i == i and prev_j == j + 1:
            return dfs(grid, i - 1, j, i, j, count + 1)
        else:
            return 0

    elif grid[i][j] == "J":
        #print("J")
        if prev_i == i - 1 and prev_j == j:
            return dfs(grid, i, j - 1, i, j, count + 1)
        elif prev_i == i and prev_j == j - 1:
            return dfs(grid, i - 1, j, i, j, count + 1)
        else:
            return 0

    elif grid[i][j] == "7":
        #print("7")
        if prev_i == i and prev_j == j - 1:
            return dfs(grid, i + 1, j, i, j, count + 1)
        elif prev_i == i + 1 and prev_j == j:
            return dfs(grid, i, j - 1, i, j, count + 1)
        else:
            return 0

    elif grid[i][j] == "F":
        #print("F")
        if prev_i == i + 1 and prev_j == j:
            return dfs(grid, i, j + 1, i, j, count + 1)
        elif prev_i == i and prev_j == j + 1:
            return dfs(grid, i + 1, j, i, j, count + 1)
        else:
            return 0

    """
    elif grid[i][j] == ".":
        #print("F")
        return 0
    """
    return 0






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
