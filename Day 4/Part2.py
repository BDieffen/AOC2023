def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def CalculateMatchingNumbers(winning_nums, held_nums):
    matches = 0
    for winning_number in winning_nums.split(" "):
        if winning_number != " " and winning_number != "":
            for held_number in held_nums.split(" "):
                if held_number != " " and held_number != "":
                    if held_number == winning_number:
                        matches += 1
    return matches

def Run():
    input = ReadInput()
    total = 0
    card_matches = {}
    card_instances = {}

    for line in input:
        card_num = int(line.split(": ")[0].split("Card")[1].lstrip())
        card_instances[card_num] = 1

    for line in input:
        card_num = int(line.split(": ")[0].split("Card")[1].lstrip())
        winning_numbers = line.split(": ")[1].split("| ")[0]
        held_numbers = line.split(": ")[1].split("| ")[1]
        matches = CalculateMatchingNumbers(winning_numbers, held_numbers)
        card_matches[card_num] = matches

    # i is the card number
    for i in card_instances.keys():
        matches_on_card = card_matches[i]
        for instance in range(card_instances[i]):
            for index, match in enumerate(range(matches_on_card)):
                target_card = i + index + 1
                card_instances[target_card] += 1

    for x in card_instances.values():
        total += x
    print(str(total) + " scratchcards total")

Run()