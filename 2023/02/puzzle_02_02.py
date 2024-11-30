from itertools import *
import itertools
import re
from variables import *
import time

#VARIABLES#
lowest_number = 0
game_count = 0
cube_colors = ["red", "green", "blue"]
bag = {'red':12,'green':13,'blue':14}
result = 0

#FUNCTIONS#
def get_ball_position(p_string, p_list):
    l_ball_positions = {}
    for item in p_list:
        l_pattern = re.compile(f'(?i){re.escape(item)}')
        l_positions = [match.start() for match in l_pattern.finditer(p_string)]
        l_ball_positions[item] = l_positions
    return(l_ball_positions)

def create_substring(p_string, p_string_end, p_return):
    l_string_start = p_string_end - p_return - 1
    l_sub_string = p_string[l_string_start:p_string_end]
    l_sub_string_cleaned = l_sub_string.replace(" ", "")
    return(l_sub_string_cleaned)

def get_ball_amount(p_string, p_list):
    get_ball_position(p_string, p_list)

#START#
start_time = time.time()
calibration_document = open(link_to_puzzle_input, "r")
data = calibration_document.read()

for line in data.split('\n'):
    cache_lowest_number = 0
    for word in line.split():
        for letter in line:
            if letter == ":":
                f_round_start = 1
        if f_round_start == 1:
             if word.isnumeric():
                  cache_lowest_number = int(word)
                  if lowest_number < cache_lowest_number:
                       lowest_number = cache_lowest_number

longest_number = len(str(lowest_number))

for line in data.split('\n'):
    max_bag = []
    game_count = game_count + 1
    for letter in line:
        if letter.isnumeric():
            pass
        if str(letter) == str(":"):
            break
        
    pos_dict = get_ball_position(line, cube_colors)
    red_cubes = []
    green_cubes = []
    blue_cubes = []
    for key, value in (
         itertools.chain.from_iterable( 
            [itertools.product((k, ), v) for k, v in pos_dict.items()])):
                amount = key, create_substring(line, value, longest_number)
                if key == "red":                     
                    red_cubes.append(int(amount[1]))         
                    
                if key == "green":
                    green_cubes.append(int(amount[1])) 

                if key == "blue":
                    blue_cubes.append(int(amount[1]))    
    
    max_bag.append(max(red_cubes))
    max_bag.append(max(green_cubes))
    max_bag.append(max(blue_cubes))
    
    cache_result = 1
    red_cubes = []
    green_cubes = []
    blue_cubes = []
    for i in max_bag:
        print(i)
        cache_result = cache_result * i
    result = result + cache_result
    cache_result = 1
calibration_document.close()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
print(result)