import os
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/01/puzzle_input.txt"
left_input = []
right_input = []

document = open(puzzle_input, "r")
data = document.read()
    
    
end_time = time.time()
execution_time = end_time - start_time
#print(result)
print("Execution time", execution_time)