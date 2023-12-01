def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def Run():
    input = ReadInput()

Run()