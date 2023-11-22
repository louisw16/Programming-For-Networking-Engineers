from util import read_devices_info
from util import print_device_info
from util import write_devices_info

devices_list = read_devices_info('devices-02.csv')

for device in devices_list:

    print('==== Device ===============================================')

    device.connect()

    device.get_interfaces()
 
    print_device_info(device)

Write_devices_info('devices-02-out.csv', devices_list)