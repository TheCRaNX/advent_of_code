import collections
import itertools
import linecache
import re
from variables import *
calibration_document = open(test, "r")

game_count = 0
red_cubes = 0
green_cubes = 0
blue_cubes = 0
cube_colors = ["red", "green", "blue"]
bag = {'red_cubes':12,'green_cubes':13,'blue_cubes':14}


#DICTIONARY VARIABLES#
red_cube = []
green_cube = []
blue_cube = []

#DICTIONARIES#

games = {}
games[1] = {}




data = calibration_document.read()

def get_ball_position(p_string, p_list):
    l_ball_positions = {}
    for item in p_list:
        #print(item)
        l_pattern = re.compile(f'(?i){re.escape(item)}')
        l_positions = [match.start() for match in l_pattern.finditer(p_string)]
        #print(l_positions)
        l_ball_positions[item] = l_positions
    return(l_ball_positions)

def get_line(p_line_number):
    l_line_number = linecache.getline(test, p_line_number)
    return l_line_number

def create_substring(p_string, p_string_start):
    l_sub_string = p_string[p_string_start - 2:p_string_start]
    return(l_sub_string)

def get_ball_amount(p_string, p_list):
    get_ball_position(p_string, p_list)


rounds_counter = 0
for line in data.split('\n'):
    rounds_counter = 1
    game_count = game_count + 1
    #print("NEW GAME!")
    #print("Game: " + str(game_count) + " and Round: " + str(rounds_counter))
    #print(game_count)
    #print(line)
    for letter in line:
        if letter == ";":
            rounds_counter = rounds_counter + 1
            #print("Game: " + str(game_count) + " and Round: " + str(rounds_counter))
            
#print(games)

game_count = 0

for line in data.split('\n'):
    game_count = game_count + 1
    print(game_count)
    #print(line)
    for letter in line:
        if letter.isnumeric():
            #print(letter)
            pass
        if str(letter) == str(":"):
            break

    #print(get_ball_position(line, cube_colors))
    #print(get_ball_amount(line, cube_colors))
    #for key in get_ball_position(line, cube_colors):
     #   print(key)
      #  key[0]
        
    pos_dict = get_ball_position(line, cube_colors)
    
    for key, value in ( 
        itertools.chain.from_iterable( 
            [itertools.product((k, ), v) for k, v in pos_dict.items()])): 
                print(key, create_substring(line, value))
                amount = key, create_substring(line, value)
                if key == "red":
                    print("its red" + str(amount))
                    red_cube.append(amount[1])
                    red_cubes = red_cubes + int(amount[1])
                    
                if key == "green":
                    print("its green" + str(amount))
                    #green_cubes = green_cubes + int(amount)
                if key == "blue":
                    print("its blue" + str(amount))
                    #blue_cubes = blue_cubes + int(amount)
                    
    print(str(red_cubes) + " red cubes in total")
    red_cubes = 0
            
        
    

    #print(position_amount - 2)
calibration_document.close() 
print(red_cubes)