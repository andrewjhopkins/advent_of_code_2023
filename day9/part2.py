import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])
    output = 0

    for line in lines:
        first_num = []

        current = line

        while True:
            new_current = []
            for i in range(len(current) - 1, 0, -1):
                new_current.append(current[i] - current[i - 1])

            new_current = new_current[::-1]

            first_num.append(current[0])

            current = new_current

            all_zeros = True
            for num in current:
                if num != 0:
                    all_zeros = False
                    break

            if all_zeros:
                break

        new_top_num = first_num[-1]

        for i in range(len(first_num) - 2, -1, -1):
            new_top_num = first_num[i] - new_top_num

        output += new_top_num

    print(output)
    return


def get_input(file_name):
    lines = []
    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip()
            if len(line) != 0:
                line_split = line.split(" ")
                lines.append([int(n) for n in line_split])

    return lines

if __name__ == "__main__":
    main()
