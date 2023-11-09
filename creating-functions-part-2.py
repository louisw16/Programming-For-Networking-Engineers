#fuction to read device info from file
def read_device_info ():
    
    #read in the devices from the file
    file = open('devices-08.txt', 'r')
    for line in file:

        #get device info into list
        device_info_list = line.strip().split(',')
        devices_list.append(device_info_list)

    #close the file
    file.close()

#function to go through devices desplaying them in table
def print_device_info():
    
    print('')
    print('Name     OS-type  IP address           Software              ')
    print('-------- -------- ---------------      ---------------')

    #go through the list of devices, displaying values in nice format
    for device in devices_list:

        print('{0:8} {1:8} {2:20} {3:20}'.format(device[0], device[1], device[3], device[3]))

    print('')

#main
#create the outer list for all devices
devices_list = []

#read device info
read_device_info()

#display info
print_device_info()

