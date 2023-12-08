def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()


def Run():
    input = ReadInput()
    # when button held, for each millisecond held, speed increases 1 millimeter per second
    spd_increase_step = 1
    race_time = input[0].split(":")[1].replace(" ", "")
    distance = input[1].split(":")[1].replace(" ", "")
    print(Race(int(race_time), int(distance), spd_increase_step))


def Race(time, record, increase_step):
    speed = 0
    dist = 0
    possibilities = 0
    for i in range(1, int(time)+1):
        speed += increase_step
        dist = speed * (int(time) - i)
        if int(dist) > int(record):
            possibilities += 1
    return possibilities

Run()