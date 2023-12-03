from variables import *
from itertools import *
import linecache
import re
calibration_document = open(test, "r")




search_line('467..114..', '467')

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
'def'
#print(m)

data = calibration_document.read()

print(linecache.getline(test, 5))