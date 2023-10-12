from pprint import pprint
from collections import namedtuple

Dev_info = namedtuple('Dev_info', ['name', 'os_type', 'ip', 'user', 'password'])

os_types = set()

file = open('devices-04.txt', 'r')
for line in file:
    device_info = Dev_info(*(line.strip().split(',')))

    print('Device Information: ', device_info)

    if device_info.os_type not in os_types:
        os_types.add(device_info.os_type)

print('')
print('Input converted to a set of OS types present:')
pprint(os_types)

file.close()