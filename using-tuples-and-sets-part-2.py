from pprint import pprint
file = open('devices-05.txt', 'r')
file_line = file.readline().strip()

print('Read line: ', file_line)

device_info = tuple(file_line.split(','))

print('')
print('Input converted to a tuple:')
pprint(device_info)

file.close()

