link_to_calibration_document = "/home/paddi/Documents/projekte/python projects/adven_of_code/01/calibration_document.txt"
calibration_document = open(link_to_calibration_document, "r")
data = calibration_document.read()
result = 0
for line in data.split('\n'):
    cache = []
    for character in range(0, len(line)):
        if line[character].isnumeric():
            x = int(line[character])
            cache.append(x)
        else:
            pass
    first_last = [cache[n] for n in (0, -1)]
    number = ''
    for i in first_last:
        number += '' + str(i)
    result = result + int(number)
print(result)
calibration_document.close() 