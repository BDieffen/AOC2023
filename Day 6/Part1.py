def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def Run():
    input = ReadInput()
    # when button held, for each millisecond held, speed increases 1 millimeter per second
    spd_increase_step = 1
    race_times = input[0].split(":")[1].strip().split()
    record_distances = input[1].split(":")[1].strip().split()

    variations = 1

    for index, race in enumerate(race_times):
        print("-------------------------")
        print("Race:" + str(index+1))
        race_record = record_distances[race_times.index(race)]
        variations = variations * (Race(race, race_record, spd_increase_step))
    print("variations: " + str(variations))


def Race(time, record, increase_step):
    speed = 0
    dist = 0
    possibilities = 0
    for i in range(1, int(time)+1):
        speed += increase_step
        dist = speed * (int(time) - i)
        if int(dist) > int(record):
            possibilities += 1
    print(possibilities)
    return possibilities

Run()