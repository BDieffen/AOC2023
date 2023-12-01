def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def ReverseString(x):
    return x[::-1]

def Run():
    input = ReadInput()
    total = 0
    for line in input:
        first_number = ""
        last_number = ""
        for char in line:
            if char.isnumeric():
                first_number = char
                break
        for char in ReverseString(line):
            if char.isnumeric():
                last_number = char
                break
        total = total + int((first_number + last_number))
    print(total)

Run()