import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])

    ranges = []

    seeds = [int(seed) for seed in (list(lines[0][7:].split(" ")))]

    sub_range = []

    for line in lines[2:]:
        if str.isnumeric(line[0]):
            sub_range.append([int(seed) for seed in list(line.split(" "))])
        else:
            ranges.append(sub_range)
            sub_range = []

    ranges.append(sub_range)

    # destination range start, source range start, range length
    for sub_range in ranges:
        new_seeds = []

        for s in seeds:

            new_seed = s

            for r in sub_range:
                if s >= r[1] and s < (r[1] + r[2]):
                    new_seed = r[0] + (s - r[1])
                    break

            new_seeds.append(new_seed)

        seeds = new_seeds

    print(min(new_seeds))
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
