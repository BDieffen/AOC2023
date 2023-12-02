def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def GetGameNumber(line):
    game_num = line.split(":")[0]
    game_num = game_num.split(" ")[1]
    return int(game_num)

def GetMaxShownRedCubes(line):
    max_red_cubes = 0
    shown = line.split(": ")[1]
    handfuls = shown.split("; ")

    for handful in handfuls:
        cubes = handful.split(", ")
        for cube_color in cubes:
            if "red" in cube_color:
                cube_color.strip()
                num_red_cubes = int(cube_color.split(" ")[0])
                if num_red_cubes > max_red_cubes:
                    max_red_cubes = num_red_cubes
    return max_red_cubes

def GetMaxShownGreenCubes(line):
    max_green_cubes = 0
    shown = line.split(": ")[1]
    handfuls = shown.split("; ")

    for handful in handfuls:
        cubes = handful.split(", ")
        for cube_color in cubes:
            if "green" in cube_color:
                cube_color.strip()
                num_green_cubes = int(cube_color.split(" ")[0])
                if num_green_cubes > max_green_cubes:
                    max_green_cubes = num_green_cubes
    return max_green_cubes

def GetMaxShownBlueCubes(line):
    max_blue_cubes = 0
    shown = line.split(": ")[1]
    handfuls = shown.split("; ")

    for handful in handfuls:
        cubes = handful.split(", ")
        for cube_color in cubes:
            if "blue" in cube_color:
                cube_color.strip()
                num_blue_cubes = int(cube_color.split(" ")[0])
                if num_blue_cubes > max_blue_cubes:
                    max_blue_cubes = num_blue_cubes
    return max_blue_cubes



def Run():
    input = ReadInput()
    sum = 0
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    games = []

    for line in input:
        games.append(line)

    for game in games:
        game_num = GetGameNumber(game)
        highest_red = GetMaxShownRedCubes(game)
        highest_green = GetMaxShownGreenCubes(game)
        highest_blue = GetMaxShownBlueCubes(game)
        if highest_red <= red_cubes and highest_green <= green_cubes and highest_blue <= blue_cubes:
            sum += game_num
    print(sum)

Run()