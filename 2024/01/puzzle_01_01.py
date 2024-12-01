import os
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/01/puzzle_input.txt"
left_input = []
right_input = []

document = open(puzzle_input, "r")
data = document.read()
result = 0
for line in data.split('\n'):
    left_input.append(int(line[0:5]))
    right_input.append(int(line[8:13]))

left_input = sorted(left_input, key=lambda e: int(e))
right_input = sorted(right_input, key=lambda e: int(e))

for (x, y) in zip(left_input, right_input):
    cache = abs(x - y)
    result = result + cache
    
end_time = time.time()
execution_time = end_time - start_time
print(result)
print("Execution time", execution_time)