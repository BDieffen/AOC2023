def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def ReverseString(x):
    return x[::-1]

def FirstNumber(line, typed_nums):
    word = ""
    for char in line:
        if char.isnumeric():
            return char

        word = word + char

        for val in typed_nums.keys():
            if val in word:
                return typed_nums[val]

def LastNumber(line, typed_nums):
    word = ""
    for char in ReverseString(line):
        if char.isnumeric():
            return char

        word = char + word

        for val in typed_nums.keys():
            if val in word:
                return typed_nums[val]

def Run():
    input = ReadInput()
    total = 0
    relation = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    for line in input:
        first_number = FirstNumber(line, relation)
        last_number = LastNumber(line, relation)
        line_total = int((first_number + last_number))
        total += line_total
    print(total)

Run()