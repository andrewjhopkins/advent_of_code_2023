import sys
from math import gcd


def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return

    lines = get_input(sys.argv[1])

    nodes = {}

    directions = list(lines[0])

    starting_nodes = []

    for line in lines[1:]:
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]

        if node[2] == "A":
            starting_nodes.append(node)

        nodes[node] = [left, right]

    cycle_steps = []

    for i in range(len(starting_nodes)):
        step_count = 0
        cycle_step = []

        direction_index = 0
        current = starting_nodes[i]

        found_z = False

        while True:
            while (step_count == 0 or current[2] != "Z"):
                next_direction = 1 if directions[direction_index] == "R" else 0

                current = nodes[current][next_direction]

                direction_index += 1
                direction_index %= len(directions)
                step_count += 1

            if not found_z:
                found_z = True
                cycle_step.append(step_count)
                step_count = 0
            else:
                cycle_step.append(step_count)
                break
        cycle_steps.append(cycle_step)

    time_for_each = [cycle[0] for cycle in cycle_steps]

    lcm = time_for_each.pop()

    while len(time_for_each):
        compare_val = time_for_each.pop()
        lcm = lcm * compare_val // gcd(lcm, compare_val)

    print(lcm)
    return

def end(nodes):
    for node in nodes:
        if node[2] != "Z":
            return False

    return True


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
