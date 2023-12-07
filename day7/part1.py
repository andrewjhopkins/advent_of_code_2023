import sys


def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])
    hands = []

    for line in lines:
        line_split = line.split(" ")
        hands.append((list(line_split[0]), int(line_split[1])))

    # 7 ways (high card, one pair etc.)

    # 0: high card
    # 1: one pair
    # 2: two pair
    # 3: three of a kind
    # 4: full house
    # 5: four of a kind
    hand_types = [[] for _ in range(7)]

    for hand in hands:
        dic = {}
        max_of_kind = 0
        pairs = 0

        for card in hand[0]:
            if card not in dic:
                dic[card] = 1
            else:
                dic[card] += 1
                if dic[card] == 2:
                    pairs += 1

            max_of_kind = max(max_of_kind, dic[card])

        if pairs == 0:
            hand_types[0].append(hand)
        elif pairs == 1 and max_of_kind == 2:
            hand_types[1].append(hand)
        elif pairs == 2 and max_of_kind == 2:
            hand_types[2].append(hand)
        # check full house case first
        elif pairs == 2 and max_of_kind == 3:
            hand_types[4].append(hand)
        elif max_of_kind == 3:
            hand_types[3].append(hand)
        elif max_of_kind == 4:
            hand_types[5].append(hand)
        elif max_of_kind == 5:
            hand_types[6].append(hand)

    for hand_type in hand_types:
        from functools import cmp_to_key
        hand_type.sort(key=cmp_to_key(compare))

    rank = 1
    output = 0

    for hand_type in hand_types:
        for i in range(len(hand_type)):
            output += (hand_type[i][1] * rank)
            rank += 1

    print(output)
    return

card_to_val = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8, 
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def compare(item1, item2):
    index = 0

    item1_list = item1[0]
    item2_list = item2[0]

    while index < len(item1_list):
        if item1_list[index] == item2_list[index]:
            index += 1
        else:
            return 1 if card_to_val[item1_list[index]] > card_to_val[item2_list[index]] else -1

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
