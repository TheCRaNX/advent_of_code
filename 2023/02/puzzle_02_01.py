import collections
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
red_cube = 0
green_cube = 0
blue_cube = 0

#DICTIONARIES#

games = {}
games[1] = {}




data = calibration_document.read()

def get_ball_amount(p_string, p_list):
    for item in p_list:
        print(item)
        l_pattern = re.compile(f'(?i){re.escape(item)}')
        l_positions = [match.start() for match in l_pattern.finditer(p_string)]
        print(l_positions)
    return(print("success"))

def get_line(p_line_number):
    l_line_number = linecache.getline(test, p_line_number)
    return l_line_number

def create_substring(p_string, p_string_start, p_string_end):
    l_sub_string = p_string[p_string_start:p_string_end:1]
    print(l_sub_string)
    return(l_sub_string)




rounds_counter = 0
for line in data.split('\n'):
    rounds_counter = 1
    game_count = game_count + 1
    print("NEW GAME!")
    print("Game: " + str(game_count) + " and Round: " + str(rounds_counter))
    #print(game_count)
    #print(line)
    for letter in line:
        if letter == ";":
            rounds_counter = rounds_counter + 1
            print("Game: " + str(game_count) + " and Round: " + str(rounds_counter))
            
print(games)
exit()


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

    print(get_ball_amount(line, cube_colors))
            
        
    

    #print(position_amount - 2)
calibration_document.close() 