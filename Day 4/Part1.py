def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def CalculateMatchingNumbers(winning_nums, held_nums):
    matches = 0
    points = 0
    for winning_number in winning_nums.split(" "):
        if winning_number != " " and winning_number != "":
            for held_number in held_nums.split(" "):
                if held_number != " " and held_number != "":
                    if held_number == winning_number:
                        matches += 1

    for match in range(matches):
        if match == 0:
            points += 1
        else:
            points = points * 2
    return points

def Run():
    input = ReadInput()
    total = 0

    for line in input:
        card_num = line.split(": ")[0].split(" ")[1]
        winning_numbers = line.split(": ")[1].split("| ")[0]
        held_numbers = line.split(": ")[1].split("| ")[1]
        total += CalculateMatchingNumbers(winning_numbers, held_numbers)
    print(total)

Run()