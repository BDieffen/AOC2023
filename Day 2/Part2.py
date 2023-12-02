def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def GetMinPossibleRedCubes(line):
    min_red_cubes = 0
    initial = True
    shown = line.split(": ")[1]
    handfuls = shown.split("; ")

    for handful in handfuls:
        cubes = handful.split(", ")
        for cube_color in cubes:
            if "red" in cube_color:
                cube_color.strip()
                num_red_cubes = int(cube_color.split(" ")[0])
                if initial:
                    min_red_cubes = num_red_cubes
                    initial = False
                if num_red_cubes > min_red_cubes:
                    min_red_cubes = num_red_cubes
    return min_red_cubes

def GetMinPossibleGreenCubes(line):
    min_green_cubes = 0
    initial = True
    shown = line.split(": ")[1]
    handfuls = shown.split("; ")

    for handful in handfuls:
        cubes = handful.split(", ")
        for cube_color in cubes:
            if "green" in cube_color:
                cube_color.strip()
                num_green_cubes = int(cube_color.split(" ")[0])
                if initial:
                    min_green_cubes = num_green_cubes
                    initial = False
                if num_green_cubes > min_green_cubes:
                    min_green_cubes = num_green_cubes
    return min_green_cubes

def GetMinPossibleBlueCubes(line):
    min_blue_cubes = 0
    initial = True
    shown = line.split(": ")[1]
    handfuls = shown.split("; ")

    for handful in handfuls:
        cubes = handful.split(", ")
        for cube_color in cubes:
            if "blue" in cube_color:
                cube_color.strip()
                num_blue_cubes = int(cube_color.split(" ")[0])
                if initial:
                    min_blue_cubes = num_blue_cubes
                    initial = False
                if num_blue_cubes > min_blue_cubes:
                    min_blue_cubes = num_blue_cubes
    return min_blue_cubes



def Run():
    input = ReadInput()
    sum = 0
    games = []

    for line in input:
        games.append(line)

    for game in games:
        min_red = GetMinPossibleRedCubes(game)
        min_green = GetMinPossibleGreenCubes(game)
        min_blue = GetMinPossibleBlueCubes(game)

        power = min_red * min_green * min_blue
        sum += power
    print(sum)

Run()