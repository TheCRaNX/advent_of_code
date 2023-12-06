import linecache
import re

from variables import *
import re


def get_line_number(p_line, p_char):
    l_line_number = p_line.find(p_char)
    return(l_line_number)

def get_line(p_line_number):
    l_line = linecache.getline(test, p_line_number)
    return l_line

def create_substring(p_string, p_string_start, p_string_end):
    l_substring = p_string[p_string_start:p_string_end]
    return(l_substring)

def calc_speed(p_distance, p_time):
    l_speed = int(p_distance) / int(p_time)
    print("The speed is " + str(l_speed) + "mm/ms")
    return(l_speed)



cache_time = []
cache_recordDistance = []
time_recordDistance = {}

calibration_document = open(test, "r")
data = calibration_document.read()
line_count = 1
for line in data.split('\n'):
    for word in line.split():
        if line_count == 1:
            if word.isnumeric():
                cache_time.append(word)
        if line_count == 2:
            if word.isnumeric():
                cache_recordDistance.append(word)
        else:
            pass

    line_count = line_count + 1
calibration_document.close()

for (i, j) in zip(cache_time, cache_recordDistance):
    time_recordDistance[i] = j

print(time_recordDistance)

for key in time_recordDistance:
    for i in range(0, int(key)):
        print(i + 1)
        print(time_recordDistance[key])