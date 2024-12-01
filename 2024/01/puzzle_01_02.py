import os
import time
from variables import *

start_time = time.time()
left_input = []
right_input = []

document = open(puzzle_input, "r")
data = document.read()
result = 0
for line in data.split('\n'):
    left_input.append(int(line[0:5]))
    right_input.append(int(line[8:13]))

for x in left_input:
    count = right_input.count(x)
    if (count != 0):
        result = result + (x * count)
    
    
print(result)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time", execution_time)