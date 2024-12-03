import os
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/02/puzzle_input.txt"

document = open(puzzle_input, "r")
data = document.read()

reports = []

line_count = 0
for line in data.split('\n'):
    report = []
    
    numbers = line.split()
    
    count = 0
    for number in numbers:
        #print(number)
        level = 0
        if count > 0:
            level = int(cache) - int(number)
            report.append(level)
            
        cache = number
        count += 1
    
    reports.append(report)

result = 0


probably_safe = []
for report in reports:
    count = 0
    for i in report:
        if -3 <= i <= 3 & i != 0:
            count += 1
    
    if count == len(report):
        probably_safe.append(report)


result = 0
for prob in probably_safe:
    positive = 0
    negative = 0
    
    for int in prob:
        if int > 0:
            positive  += 1
        else:
            negative += 1
    
    if positive == len(prob) or negative == len(prob):
        result += 1


end_time = time.time()
execution_time = end_time - start_time
print(result)
print("Execution time", execution_time)