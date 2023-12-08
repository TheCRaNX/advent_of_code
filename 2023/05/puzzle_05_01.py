import linecache
import re

from variables import *
import re

#VARIABLES#
def get_line(p_line_number):
    l_line_number = linecache.getline(test, p_line_number)
    return l_line_number


def get_line(p_line, p_char):
    line_number = p_line.find(p_char)
    return(line_number)


def create_substring(p_string, p_string_start, p_string_end):
    l_substring = p_string[p_string_start:p_string_end]
    return(l_substring)


def get_seeds(p_line, p_list):
    l_line_split = p_line.split()
    for word in l_line_split:
        #print(word)
        if word.isnumeric():
            p_list.append(word)


def convert_numbers(p_z, p_y, p_x, p_source_list):
    l_cache_list_y = []
    l_cache_list_z = []
    
    for i in range(0, p_y):
        l_cache_list_y.append(i + 1)
        
    for i in range(0, p_z):
        l_cache_list_y.append(i + 1)
        
    for i in p_source_list:
        l_destination_number = 0
        
        if i in l_cache_list_y:
            l_destination_number = i + p_x
            print(l_destination_number)
            
        if i in l_cache_list_z:
            l_destination_number = i + p_x
            print(l_destination_number)
    

#LISTS#
seeds = []

games = 0
calibration_document = open(test, "r")
data = calibration_document.read()
result = 0
line_count = 0
for line in data.split('\n'):
    line_count = line_count + 1
    #print(line_count)
    #print(line)
    line_split = line.split()
    for word in line_split:
        #print(word)
        if str(word) == "seeds:":
            get_seeds(line, seeds)
            
    
calibration_document.close() 
print(seeds)
#print(result)