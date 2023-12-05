import linecache
import re

from variables import *
import re


def get_line_number(p_line, p_char):
    l_line_number = p_line.find(p_char)
    return(l_line_number)

def get_certain_line_of_txt_file(p_link_to_txt_file):
    l_f=open(p_link_to_txt_file)
    l_lines=l_f.readlines()
    return(l_lines)

def write_to_text(p_link_to_txt_file, p_string):
    l_f = open(p_link_to_txt_file, 'a')
    l_f.write(p_string)
    return("written to copy")

def create_substring(p_string, p_string_start, p_string_end):
    l_substring = p_string[p_string_start:p_string_end]
    return(l_substring)


def check_number(p_number_card, p_winning_numbers):
    if p_number_card in p_winning_numbers:
        return(True)
    
def calc_and_save_win_amount(p_winning_number):
    p_win_amount = p_winning_number * 2

#DELETE CONTENT OF COPY.TXT#
open(copy_txt, 'w').close()

games = 0
calibration_document = open(test, "r")
data = calibration_document.read()
result = 0
for line in data.split('\n'):
    split_line = line.split()
    cache_card_numbers = []
    cache_winning_numbers = []
    games = games + 1
    #print("Games played " + str(games))
    
    string_cards = create_substring(line, get_line_number(line, ':'), get_line_number(line, '|')).split()
    string_winning = create_substring(line, get_line_number(line, '|'), len(line)).split()

    for word in string_cards:
        if word.isnumeric():
            cache_card_numbers.append(word)

    for word in string_winning:
        if word.isnumeric():
            cache_winning_numbers.append(word)

    for i in cache_card_numbers:
        if check_number(i, cache_winning_numbers) == True:
            print(games)
            write_to_text(copy_txt, line)
            #print(get_certain_line_of_txt_file(link_to_puzzle_input)[int(i) - 1])
            write_to_text(copy_txt, get_certain_line_of_txt_file(link_to_puzzle_input)[int(i) - 1])
            
        else:
            pass
    '''
    print(cache_card_numbers)
    print("######")
    print(cache_winning_numbers)
    '''
    
    

    
calibration_document.close() 

exit()

calibration_document = open(copy_txt, "r")
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
    
    string_cards = create_substring(line, get_line_number(line, ':'), get_line_number(line, '|')).split()
    string_winning = create_substring(line, get_line_number(line, '|'), len(line)).split()

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