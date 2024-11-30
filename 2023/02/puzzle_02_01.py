import itertools
import re
from variables import *
import time

#VARIABLES#
highest_number = 0
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
    cache_highest_number = 0
    for word in line.split():
        for letter in line:
            if letter == ":":
                f_round_start = 1
        if f_round_start == 1:
             if word.isnumeric():
                  cache_highest_number = int(word)
                  if highest_number < cache_highest_number:
                       highest_number = cache_highest_number

longest_number = len(str(highest_number))

for line in data.split('\n'):
    game_count = game_count + 1
    for letter in line:
        if letter.isnumeric():
            pass
        if str(letter) == str(":"):
            break
        
    pos_dict = get_ball_position(line, cube_colors)
    highest_red_cube = 0
    highest_green_cube = 0
    highest_blue_cube = 0
    for key, value in (
         itertools.chain.from_iterable( 
            [itertools.product((k, ), v) for k, v in pos_dict.items()])):
                amount = key, create_substring(line, value, longest_number)
                if key == "red":
                    cache_highest_red_cube = int(amount[1])
                    if highest_red_cube < cache_highest_red_cube:
                         highest_red_cube = cache_highest_red_cube                 
                    
                if key == "green":
                    cache_highest_green_cube = int(amount[1])
                    if highest_green_cube < cache_highest_green_cube:
                         highest_green_cube = cache_highest_green_cube  

                if key == "blue":                  
                    cache_highest_blue_cube = int(amount[1])
                    if highest_blue_cube < cache_highest_blue_cube:
                         highest_blue_cube = cache_highest_blue_cube    

    yes = 0
    
    if int(bag["red"]) >=  int(highest_red_cube):
        yes = yes + 1

    if int(bag["green"]) >=  int(highest_green_cube):
        yes = yes + 1

    if int(bag["blue"]) >=  int(highest_blue_cube):
        yes = yes + 1

    if yes == 3:
        result = result + game_count

    yes = 0
    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0
    
calibration_document.close()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
print(result)