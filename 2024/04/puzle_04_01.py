import os
import re
import time

start_time = time.time()

puzzle_input = os.getcwd()+ "/2024/04/puzzle_input.txt"

def get_char(p_text, p_x, p_y):

    if 1 <= p_y <= len(p_text):
        l_line = p_text[p_y -1]
        if 1 <= p_x <= len(l_line):
            return l_line[p_x - 1]
        else:
            return None
    else:
        return None
    
def walk(p_data, p_allowed_words, p_x, p_y, p_max_width, p_max_length):
    #print("Function: p_allowed_words = ", p_allowed_words, ", p_x = ", p_x, ", p_y = " , p_y, ", p_max_width = ", p_max_width, ", p_max_length = ", p_max_length)

    c_x = int(p_x)
    c_y = int(p_y)
    c_max_width = int(p_max_width)
    c_max_length = int(p_max_length)
    
        
    count = 0
    # WALK ALL DIRECTIONS #
    positions = set()
    for direction in directions.keys():
        word_cache = ""
        position_cache = []
        
        for i in directions[direction]:
            #print(direction, ": ", count)
            #print(n[0], n[1])
            #print(c_x, length)
            #print(char)
            char = get_char(p_data, c_x + i[0], c_y + i[1])
            word_cache = str(word_cache) + str(char)
            position_cache.append((c_x + i[0], c_y + i[1]))
        
        if word_cache in p_allowed_words:

            if tuple(position_cache) not in positions:
                print(direction + " in  (x: " + str(c_x) + ", y: " + str(c_y), position_cache)
                print(word_cache)
                count += 1
                positions.add(tuple(position_cache))
            
    # END WALK ALL DIRECTIONS #



    #print(positions)
    return count


        

words = ["XMAS"]
words_length = len(words)


# x:y
directions = {
    "North": [(0, 0), (0, -1), (0, -2), (0, -3)],

    "NorthEast": [(0, 0), (1, -1), (2, -2), (3, -3)],

    "East": [(0, 0), (1, 0), (2, 0), (3, 0)],

    "SouthEast": [(0, 0), (1, 1), (2, 2), (3, 3)],

    "South": [(0, 0), (0, 1), (0, 2), (0, 3)],

    "SouthWest": [(0, 0), (-1, 1), (-2, 2), (-3, 3)],

    "West": [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    
    "NorthWest": [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
}

try:
    with open(puzzle_input, "r") as document:
        data = document.readlines()

    c_max_width = 0
    c_max_height = 0
    for line in data:
        c_max_height += 1
        if len(line) > c_max_width:
            c_max_width = len(line)


    result = 0

    y = 0
    for line in data:
        y += 1
        for x in range(len(line)):
            count = 0
            count = walk(data, words, x + 1, y, c_max_width, c_max_height)
            result = result + count



    end_time = time.time()
    execution_time = end_time - start_time
    print(c_max_width, c_max_height)
    print(result)
    print("Execution time", execution_time)

except FileNotFoundError:
    print("File not found.")