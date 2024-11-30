import linecache
import re
from variables import *
import time


start_time = time.time()
cache_time = []
cache_recordDistance = []
time_recordDistance = {}

calibration_document = open(link_to_puzzle_input, "r")
data = calibration_document.read()
line_count = 1
for line in data.split('\n'):
    for word in line.split():
        if line_count == 1:
            if word.isnumeric():
                cache_time.append(word)
        if line_count == 2:
            if word.isnumeric():
                cache_recordDistance.append(word)
        else:
            pass
    line_count = line_count + 1
calibration_document.close()

for (i, j) in zip(cache_time, cache_recordDistance):
    if i in time_recordDistance:
        time_recordDistance[str(i) + "."] = j    
    else:    
        time_recordDistance[i] = j

result = 1
for key in time_recordDistance:
    cache_result = 0
    for i in range(0, int(key.replace(".", ""))):
        remaining_time = int(key.replace(".", "")) - i
        if (remaining_time * int(i)) > int(time_recordDistance[key]):
            cache_result = cache_result + 1
    result = result * cache_result
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
print(result)