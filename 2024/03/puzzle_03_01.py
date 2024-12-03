import os
import re
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/03/puzzle_input.txt"

document = open(puzzle_input, "r")
data = document.read()

matches = re.findall("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", data)

result = 0
for match in matches:
    numbers = re.findall("[1-9][0-9]{0,2}", match)
    cache = int(numbers[0]) * int(numbers[1])
    result = result + cache

end_time = time.time()
execution_time = end_time - start_time
print(result)
print("Execution time", execution_time)