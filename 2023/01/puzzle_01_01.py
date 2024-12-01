import os
import time

start_time = time.time()
puzzle_input = os.getcwd()+ "/2023/01/puzzle_input.txt"
calibration_document = open(puzzle_input, "r")
data = calibration_document.read()
result = 0
for line in data.split('\n'):
    cache = []
    for character in range(0, len(line)):
        if line[character].isnumeric():
            x = int(line[character])
            cache.append(x)
        else:
            pass
    first_last = [cache[n] for n in (0, -1)]
    number = ''
    for i in first_last:
        number += '' + str(i)
    result = result + int(number)
print(result)
calibration_document.close() 
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
print(result)