import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])

    times = [int(num) for num in lines[0][5:].strip().split()]
    distances = [int(num) for num in lines[1][9:].strip().split()]

    output = 1

    for i in range(len(times)):
        time = times[i]
        distance_to_beat = distances[i]

        min_time = 0
        max_time = 0

        for j in range(1, time):
            if j * (time - j) > distance_to_beat:
                min_time = j
                break

        for j in range(time - 1, 0, -1):
            if j * (time - j) > distance_to_beat:
                max_time = j
                break

        output *= (max_time - min_time + 1)

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
