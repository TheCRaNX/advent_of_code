import os
import re
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/03/puzzle_input.txt"

document = open(puzzle_input, "r")
data = document.read()

regulars = re.finditer("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", data)
dos = re.finditer("do\(\)", data)
donts = re.finditer("don't\(\)", data)

result = 0

regular_start = []
regular_end = []
regular_list = []
for regular in regulars:
    regular_start.append(regular.start())
    regular_end.append(regular.end())

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

regular_start = sorted(regular_start, key=lambda e: int(e))
regular_end = sorted(regular_end, key=lambda e: int(e))
do_start = sorted(do_start, key=lambda e: int(e))
do_end = sorted(do_end, key=lambda e: int(e))
dont_start = sorted(dont_start, key=lambda e: int(e))
dont_end = sorted(dont_end, key=lambda e: int(e))



end_time = time.time()
execution_time = end_time - start_time
print(result)
print("Execution time", execution_time)