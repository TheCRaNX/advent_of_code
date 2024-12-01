import linecache
import os
import re

test = os.getcwd()+ "/2023/0036/test.txt"
calibration_document = open(test, "r")



data = calibration_document.read()


def get_line(p_line_number):
    l_line_number = linecache.getline(test, p_line_number)
    return l_line_number


def search_line(p_line, p_word):
    m = re.search('(?<=.)' + p_word, p_line)
    #m.group(0)
    p_word
    print(m)

line_count = 0
for line in data.split('\n'):
    line_count = line_count + 1
    cache = re.findall(r'\b\d+\b', line)
    search_line(str(line), '617')
        
        
    

calibration_document.close() 