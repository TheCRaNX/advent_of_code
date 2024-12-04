import os
import re
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/04/test.txt"

document = open(puzzle_input, "r")

document.seek(40)
char = document.read()
print(char)

end_time = time.time()
execution_time = end_time - start_time
#print(result)
print("Execution time", execution_time)