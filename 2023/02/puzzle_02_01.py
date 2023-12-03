from variables import *
calibration_document = open(test, "r")

game_count = 0
red_cubes = 0
green_cubes = 0
blue_cubes = 0
bag = {'red_cubes':12,'green_cubes':13,'blue_cubes':14}

data = calibration_document.read()

def get_ball_amount(p_word, p_color):
    position_amount = p_word.find(p_color)


for line in data.split('\n'):
    print(line)
    for letter in line:
        if letter.isnumeric():
            #print(letter)
            pass
        if str(letter) == str(":"):
            break

    for word in line.split():
        l_word = str(word).replace(',','')
        print(l_word)
            
        
    

    #print(position_amount - 2)
calibration_document.close() 