import os
import time

start_time = time.time()

cache_time = ''
cache_recordDistance = ''
puzzle_input = os.getcwd()+ "/2023/06/puzzle_input.txt"
calibration_document = open(puzzle_input, "r")

data = calibration_document.read()
line_count = 1
for line in data.split('\n'):
    for word in line.split():
        if line_count == 1:
            if word.isnumeric():
                cache_time = str(cache_time) + str(word)
        if line_count == 2:
            if word.isnumeric():
                cache_recordDistance = str(cache_recordDistance) + str(word)
        else:
            pass
    line_count = line_count + 1
calibration_document.close()

race_time = int(cache_time)
record_distance = int(cache_recordDistance)
result = 0
for i in range(0, race_time):
    remaining_time = race_time - i
    if (remaining_time * int(i)) > int(record_distance):
        result = result + 1
        
print(result)
print("Race time: " + str(race_time), "Record time: " + str(record_distance))
print("Execution time: %s seconds ---" % (time.time() - start_time))