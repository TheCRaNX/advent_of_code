from variables import *

help_dict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9','zero': '0'}
result = 0

calibration_document = open(link_to_calibration_document, "r")
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
print(result)
calibration_document.close() 