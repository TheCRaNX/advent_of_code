from variables import *
calibration_document = open(test, "r")

game_count = 0
red_cubes = 0
green_cubes = 0
blue_cubes = 0
bag = {'red_cubes':12,'green_cubes':13,'blue_cubes':14}

data = calibration_document.read()


for line in data.split('\n'):
    print(line)
    for letter in line:
        if letter.isnumeric():
            print(letter)
        if str(letter) == str(":"):
            break
    start_index = sentence.find()
calibration_document.close() 