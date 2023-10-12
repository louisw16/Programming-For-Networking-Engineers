from pprint import pprint

devices = []
file = open('devices-04.txt', 'r')
for line in file:

    device_info = tuple(line.strip().split(','))
    
    print ('Read line: ', device_info)

    devices.append(device_info)

print('')
print('Input converted to a list tuples:')
pprint(devices)

file.close()