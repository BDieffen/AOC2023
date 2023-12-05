def ReadInput():
    with open('input.txt') as f:
        return f.read().splitlines()

def GetMap(input, req_map):
    map_contents = []
    start_index = input.index(req_map)
    for line in range(start_index+1, len(input)):
        if input[line] == "":
            break
        map_contents.append(input[line])
    return map_contents

def MapSeed(start_point, current_map):
    final_destination = None
    start_point = int(start_point)

    for line in current_map:
        temp_line = line.split(" ")
        destination_range_start = int(temp_line[0])
        source_range_start = int(temp_line[1])
        range_length = int(temp_line[2])

        if source_range_start <= start_point <= (source_range_start + range_length):
            step = start_point - source_range_start
            final_destination = destination_range_start + step

    if final_destination is None:
        final_destination = start_point
    return final_destination

def PassSeedsThrough(input, seed_list):
    book = []
    seed_to_soil = GetMap(input, "seed-to-soil map:")
    soil_to_fertilizer = GetMap(input, "soil-to-fertilizer map:")
    fertilizer_to_water = GetMap(input, "fertilizer-to-water map:")
    water_to_light = GetMap(input, "water-to-light map:")
    light_to_temperature = GetMap(input, "light-to-temperature map:")
    temperature_to_humidity = GetMap(input, "temperature-to-humidity map:")
    humidity_to_location = GetMap(input, "humidity-to-location map:")

    for seed in seed_list:
        current_number = int(seed)
        current_seed_info = "Seed " + str(current_number)

        current_number = MapSeed(current_number, seed_to_soil)
        current_seed_info = current_seed_info + ", soil " + str(current_number)

        current_number = MapSeed(current_number, soil_to_fertilizer)
        current_seed_info = current_seed_info + ", fertilizer " + str(current_number)

        current_number = MapSeed(current_number, fertilizer_to_water)
        current_seed_info = current_seed_info + ", water " + str(current_number)

        current_number = MapSeed(current_number, water_to_light)
        current_seed_info = current_seed_info + ", light " + str(current_number)

        current_number = MapSeed(current_number, light_to_temperature)
        current_seed_info = current_seed_info + ", temperature " + str(current_number)

        current_number = MapSeed(current_number, temperature_to_humidity)
        current_seed_info = current_seed_info + ", humidity " + str(current_number)

        current_number = MapSeed(current_number, humidity_to_location)
        current_seed_info = current_seed_info + ", location " + str(current_number)

        book.append(current_seed_info)

    return book

def RetrieveLowestSeedLocation(seed_book):
    lowest_location = None
    for page in seed_book:
        location = int(page.split("location ")[1])
        if lowest_location is None:
            lowest_location = location
        if location < lowest_location:
            lowest_location = location
    return lowest_location

def Run():
    input = ReadInput()
    seeds = input[0].split(": ")[1].split(" ")
    seed_book = PassSeedsThrough(input, seeds)
    lowest_location = RetrieveLowestSeedLocation(seed_book)
    print(lowest_location)

Run()