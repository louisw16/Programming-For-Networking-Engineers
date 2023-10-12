from pprint import pprint
from collections import namedtuple

Dev_info = namedtuple('Dev_info', ['name', 'os', 'ip', 'user', 'password'])

devices = {}

file = open('devices-04.txt', 'r')
for line in file:

    device_info = Dev_info(*(line.strip().split(',')))
    print('Device Infomation: ', device_info)
    devices[device_info.name] = device_info

print('')
print('Input converted to a dictionary of named tuples:')
pprint(devices)

file.close()
