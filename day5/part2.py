import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return

    lines = get_input(sys.argv[1])

    process_steps = []

    seed_input = [int(seed) for seed in (list(lines[0][7:].split(" ")))]

    seed_ranges = []

    for i in range(len(seed_input)):
        if i % 2 != 0:
            seed_ranges.append([seed_input[i - 1], seed_input[i]])

    rules = []
    for line in lines[2:]:
        if str.isnumeric(line[0]):
            rules.append([int(seed) for seed in list(line.split(" "))])
        else:
            process_steps.append(rules)
            rules = []

    process_steps.append(rules)

    # translate rule: destination range start, source range start, range length
    for rules in process_steps:

        not_yet_translated_ranges = seed_ranges
        translated_ranges = []

        while len(not_yet_translated_ranges):
            current_range = not_yet_translated_ranges.pop(0)

            found = False
            for translate_rule in rules:

                # in range for rule
                if current_range[0] >= translate_rule[1] and current_range[0] < (translate_rule[1] + translate_rule[2]):

                    start = current_range[0]
                    # find out how much to
                    end = min(current_range[0] + current_range[1], translate_rule[1] + translate_rule[2] - 1)

                
                    # if rule doesn't cover whole range, we need to split and re-add unknown portion to not_yet_translated_ranges
                    if end != (current_range[0] + current_range[1]):
                        not_yet_found = [end + 1, current_range[1] - (end - start) - 1]
                        not_yet_translated_ranges.append(not_yet_found)

                    translated_ranges.append([(start - translate_rule[1]) + translate_rule[0], end - start])
                    found = True
                    break

                elif (current_range[0] + current_range[1]) >= translate_rule[1] and (current_range[0] + current_range[1]) < translate_rule[2]:
                    end = current_range[0] + current_range[1]

                    start = max(current_range[0], translate_rule[1])

                    if start != current_range[0]:
                        not_yet_found = [current_range[0], start - current_range[0] - 1]
                        not_yet_translated_ranges.append(not_yet_found)

                    translated_ranges.append([(start - translate_rule[1]) + translate_rule[0], end - start])
                    found = True
                    break

            if not found:
                translated_ranges.append(current_range)

        seed_ranges = translated_ranges

    print(min(seed_ranges)[0])
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
