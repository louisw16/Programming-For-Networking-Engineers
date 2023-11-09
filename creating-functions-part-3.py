def read_device_info(devices_file):

    file = open(devices_file, 'r')
    for line in file:

        device_info_list = line.strip().split(',')
        devices_list.append(device_info_list)

    file.close()

def print_device_info(list_of_devices):

    print('')
    print('Name     OS-type  IP address           Software              ')
    print('-------- -------- ---------------      ---------------')

    for device in list_of_devices:

        print('{0:8} {1:8} {2:20} {3:20}'.format(device[0], device[1], device[3], device[3]))

    print('')

#main
devices_list = []

print('')

device_file = input('Enter devices filename: ')

read_device_info(devices_file)

print_device_info(devices_list)

