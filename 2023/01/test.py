from variables import *

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

calibration_document = open(test, "r")
data = calibration_document.read()
result = 0
for line in data.split('\n'):
    cache = []
    number_cache = []
    print(line)
    count = 0
    increment = ''
    for letter in line:
        #print(letter)
        count = count + 1
        #print(count)
        increment = increment + str(letter)
        #print(increment)
        for key in help_dict:
            if key in increment:
                #print(key)
                if str(key) in cache:
                    pass
                else:
                    res = ''.join(help_dict[key])
                    #print(res)                
                    cache.append(key)
                    number_cache.append(res)
                    #print(key)
    #print(cache)
    #print(number_cache)
    first_last = [number_cache[n] for n in (0, -1)]
    number = ''
    for i in first_last:
        number += '' + str(i)
    print(number)
    print('-------')
    result = result + int(number)
    
    
    #for key in help_dict:
    #    print(key)
        #if key in line:
        #    print(key)
        #    print("---------")
        #    cache.append(key)
        #else:
        #    pass
    #first_last = [cache[n] for n in (0, -1)]
    #print(first_last)
print(result)
calibration_document.close() 