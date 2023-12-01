import sys

class Trie:
    def __init__(self):
        self.root = {}

    def add_word(self, word, digit):
        root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root["*"] = digit


def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return
    
    string_digits = [
        ("zero", "0"), 
        ("one", "1"), 
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9")
    ]

    forward_trie = Trie()

    for s, d in string_digits:
        forward_trie.add_word(s, d)

    backward_trie = Trie()

    for s, d in string_digits:
        backward_trie.add_word(reversed(s), d)

    lines = get_input(sys.argv[1])

    sum = 0

    for line in lines:
        first_digit = get_first(line, forward_trie)
        last_digit = get_last(line, backward_trie)

        num_string = first_digit + last_digit

        sum += int(num_string)

    print(sum)
    return 

def get_first(line, trie):
    for i in range(len(line)):
        char = line[i]
        if str.isdigit(char):
            return char

        elif char in trie.root:
            node = trie.root
            next_index = i
            next_char = line[next_index]

            node = node[next_char]

            while next_index < len(line):
                if "*" in node:
                    return node["*"]

                next_index += 1
                next_char = line[next_index]

                if next_char not in node:
                    break

                node = node[next_char]

    return None


def get_last(line, trie):
    for i in range(len(line) - 1, -1, -1):
        char = line[i]
        if str.isdigit(char):
            return char

        elif char in trie.root:
            node = trie.root
            next_index = i
            next_char = line[next_index]

            node = node[next_char]

            while next_index >= 0:
                if "*" in node:
                    return node["*"]

                next_index -= 1
                next_char = line[next_index]

                if next_char not in node:
                    break

                node = node[next_char]

    return None


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
