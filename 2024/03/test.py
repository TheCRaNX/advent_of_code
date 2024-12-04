import os
import re
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/03/puzzle_input.txt"

document = open(puzzle_input, "r")
data = document.read()

regular = re.findall(r"mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)(.*)don't\(\)", data)
dos = re.finditer(r"do\(\)", data)
donts = re.finditer(r"don't\(\)", data)


result = 0
for match in regular:
    numbers = re.findall(r"[1-9][0-9]{0,2}", match)
    cache = int(numbers[0]) * int(numbers[1])
    result = result + cache

do_start = []
do_end = []
dos_list = []
for do in dos:
    do_start.append(do.start())
    do_end.append(do.end())

dont_start = []
dont_end = []
donts_list = []
for dont in donts:
      dont_start.append(dont.start())
      dont_end.append(dont.end())

do_start = sorted(do_start, key=lambda e: int(e))
do_end = sorted(do_end, key=lambda e: int(e))
dont_start = sorted(dont_start, key=lambda e: int(e))
dont_end = sorted(dont_end, key=lambda e: int(e))

full = []

enabled_ranges = {}
for x in range(len(do_end)):
     for y in range(len(dont_start)):
        if y <= (len(dont_start) -2):
            if dont_start[y] < do_end[x] < dont_start[y + 1]:
                print("Enabled Start :", do_end[x], " Enabled End: ", dont_start[y + 1])
                enabled_ranges[do_end[x]] = dont_start[y + 1]
print(enabled_ranges)
           
for key in enabled_ranges:
    print("Enabled Start :", key, " Enabled End: ", enabled_ranges[key])
    string = data[key:enabled_ranges[key]]
    print(string)
    matches = re.findall(r"mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", string)
    
    for match in matches:
        numbers = re.findall(r"[1-9][0-9]{0,2}", match)
        cache = int(numbers[0]) * int(numbers[1])
        result = result + cache
        
end_time = time.time()
execution_time = end_time - start_time

print(result)
print("Execution time", execution_time)