import linecache
import os

#VARIABLES#
def get_line(p_text, p_line_number):
    l_line_number = linecache.getline(p_text, p_line_number)
    return l_line_number


def get_line_number(p_line, p_char):
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


def convert_numbers(p_destination, p_source, p_lenght,):
    l_cache_list_y = []
    l_cache_list_z = []
    
    for i in range(p_source, p_lenght):
        l_cache_list_y.append(i + 1)
        
    for i in range(p_destination, p_lenght):
        l_cache_list_y.append(i + 1)
    

    

#LISTS#
seeds = []
maps = ["seed-to-soil","soil-to-fertilizer", "fertelizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]



#START#
games = 0
test = os.getcwd()+ "/2023/05/test.txt"
calibration_document = open(test, "r")
data = calibration_document.read()
result = 0
line_count = 0
for line in data.split('\n'):
    line_count = line_count + 1
    #print(line_count)
    #print(line)
    line_split = line.split()
    for word in maps:
        if word in line:
            print("Line" + str(get_line_number(data, word)) + " and " + str(word))
            
    
calibration_document.close() 




exit()



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