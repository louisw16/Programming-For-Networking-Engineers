import csv
from pprint import pprint
from devclass import NetworkDevice
from devclass import NetworkDeviceIOS
from devclass import NetworkDeviceXR

def read_devices_info(devices_file):
    devices_list = []

    file = open(devices_file, 'r')

    csv_devices = csv.reader(file)
 
    for device_info in csv_devices:

        if device_info[1] == 'ios':
 
            device = NetworkDeviceIOS(device_info[0], device_info[2], device_info[3], device_info[4])
 
        elif device_info[1] == 'ios-xr':
 
            device = NetworkDeviceXR(device_info[0],device_info[2], device_info[3], device_info[4])

        else:
            device = NetworkDevice(device_info[0], device_info[2], device_info[3], device_info[4])
 
        devices_list.append(device)
    
    return devices_list

def print_device_info(device):
    print('-------------------------------------------------------')
    print(' Device Name: ', device.name)
    print(' Device IP: ', device.ip_address)
    print(' Device username: ', device.username,)
    print(' Device password: ', device.password)
    print('-------------------------------------------------------')
    print('')
    print(device.interfaces)
    print('')

def write_devices_info(devices_file, devices_list):
    print('---- Printing CSV output ------------------------------')

    devices_out_list = [] 
 
    for device in devices_list:
        dev_info = [device.name, device.ip_address, device.interfaces != ""]
        
        devices_out_list.append(dev_info)
 
    pprint(devices_out_list)
    print('')
 
    with open(devices_file, 'w') as file:
        csv_out = csv.writer(file)
        csv_out.writerows(devices_out_list)

