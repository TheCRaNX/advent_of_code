import linecache
import re

from variables import *
import re


def get_line(p_line_number):
    l_line_number = linecache.getline(test, p_line_number)
    return l_line_number


def get_line(p_line, p_char):
    line_number = p_line.find(p_char)
    return(line_number)


def create_substring(p_string, p_string_start, p_string_end):
    l_substring = p_string[p_string_start:p_string_end]
    return(l_substring)


def check_number(p_number_card, p_winning_numbers):
    if p_number_card in p_winning_numbers:
        return(True)
    
def calc_and_save_win_amount(p_winning_number):
    p_win_amount = p_winning_number * 2

games = 0
calibration_document = open(link_to_puzzle_input, "r")
data = calibration_document.read()
result = 0
for line in data.split('\n'):
    split_line = line.split()
    cache_card_numbers = []
    cache_winning_numbers = []
    games = games + 1
    print("Games played " + str(games))
    
    #print(line)
    #print(get_line(line, ':'))
    #print(get_line(line, '|'))
    #print(len(line))
    #print(len(line) - get_line(line, '|'))
    
    string_cards = create_substring(line, get_line(line, ':'), get_line(line, '|')).split()
    string_winning = create_substring(line, get_line(line, '|'), len(line)).split()

    for word in string_cards:
        #print(word)
        wins = 0
        if word.isnumeric():
            cache_card_numbers.append(word)

    for word in string_winning:
        if word.isnumeric():
            cache_winning_numbers.append(word)

    for i in cache_card_numbers:
        if check_number(i, cache_winning_numbers) == True:
            print("success " + str(i) + " is a winning number")
            if wins == 0:
                wins = 1
            else:                
                wins = wins * 2
        else:
            #print("no luck")
            pass
    '''
    print(cache_card_numbers)
    print("######")
    print(cache_winning_numbers)
    '''
    result = result + wins
    
calibration_document.close() 

print(result)