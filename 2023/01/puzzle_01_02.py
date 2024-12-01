import os
import time

start_time = time.time()
puzzle_input = os.getcwd()+ "/2023/01/puzzle_input.txt"
help_dict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9','zero': '0'}
result = 0
calibration_document = open(puzzle_input, "r")
data = calibration_document.read()
for line in data.split('\n'):
    cache = []
    letter_increment = ''
    for letter in line:
        if letter.isnumeric():
            cache.append(letter)
        else:
            letter_increment = letter_increment + str(letter)
        for key in help_dict:
            if key in letter_increment:
                cache.append(help_dict[key])
                letter_increment = '' + letter
    first_last = [cache[n] for n in (0, -1)]
    number = ''
    for i in first_last:
        number += '' + str(i)
    result = result + int(number)
calibration_document.close() 
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
print(result)