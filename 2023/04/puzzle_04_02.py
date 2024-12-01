import os


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

def count_matches(p_number_list, p_winners_list):
    l_win_count = 0
    for i in p_number_list:
        if check_number(i, p_winners_list) == True:
            l_win_count = l_win_count + 1
        else:
            #print("no luck")
            pass
    #print(l_win_count)
    return(l_win_count)

def add_match_to_dict(p_winners_list, p_match_dict):
    for i in p_winners_list:
        #print("---------MATCH AT------------" + str(i))
        #print("OLD: " + str(p_match_dict[i]))
        p_match_dict[i] = p_match_dict[i] + 1
        #print("NEW: " + str(p_match_dict[i]))
        #p_cache_list.append(i)
card_matches = {}


#DELETE CONTENT OF COPY.TXT#
copy_txt = os.getcwd()+ "/2023/04/copy.txt"
open(copy_txt, 'w').close()

games = 0
test = os.getcwd()+ "/2023/04/test.txt"
calibration_document = open(test, "r")
data = calibration_document.read()
result = 0

for line in data.split('\n'):
    games = games + 1
    card_matches[games] = 0

print(card_matches)

games = 0

for line in data.split('\n'):
    split_line = line.split()
    cache_card_numbers = []
    cache_winning_numbers = []
    games = games + 1
    
    winning_cards = []
    
    #print("Games played " + str(games))
    
    string_cards = create_substring(line, get_line_number(line, ':'), get_line_number(line, '|')).split()
    string_winning = create_substring(line, get_line_number(line, '|'), len(line)).split()

    for word in string_cards:
        if word.isnumeric():
            cache_card_numbers.append(word)

    for word in string_winning:
        if word.isnumeric():
            cache_winning_numbers.append(word)
            
    #print(cache_card_numbers, cache_winning_numbers)
    matches = count_matches(cache_card_numbers, cache_winning_numbers)
    if matches == 0:
        break
    
    l_games = games
    for i in range(0, matches):
        l_games = l_games + 1
        #print(games)
        winning_cards.append(l_games)
    
    print(winning_cards)
    #print(cache_winning_cards)
    
    add_match_to_dict(winning_cards, card_matches)
    
    cache_winning_cards = winning_cards
    
    '''
    print(cache_card_numbers)
    print("######")
    print(cache_winning_numbers)
    '''
    
    

    
calibration_document.close() 
print(card_matches)
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