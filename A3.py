#A3 - Louis Wilkins

#Getting imports

from netmiko import ConnectHandler
import getpass
import difflib
import logging

#Logging

logging.basicConfig(level=logging.INFO)

#Saving config

def save_config_to_file(config, filename):
    with open(filename, 'w') as config_file:
        config_file.write(config)
    logging.info(f'Configuration saved to {filename}')

#Displaying differences

def show_differences(config1, config2):
    difference = difflib.Differ()
    diff = list(difference.compare(config1.splitlines(), config2.splitlines()))

    for line in diff:
        if line.startswith('- '):
            logging.info(f'Present in ({config1}): {line[2:]}')
        elif line.startswith('+ '):
            logging.info(f'Present in ({config2}): {line[2:]}')

#Config commands

def configure_device(net_connect):
    loopback_config = [
        'en\n'
        'conf t\n'
        'interface Loopback0\n',
        'ip address 192.168.57.101 255.255.255.0\n',
        'exit\n'
    ]

    acl_config = [
        'ip access-list extended MY_ACL\n',
        'permit ip 192.168.56.130 255.255.255.0 any\n',
        'deny ip any any\n',
        'exit\n'
    ]

    interface0_config = [
        'interface GigabitEthernet0/0\n',
        'ip address 192.168.58.101 255.255.255.0\n',
        'exit\n'
    ]

    interface1_config = [
        'interface GigabitEthernet0/1\n',
        'ip address 192.168.59.101 255.255.255.0\n',
        'exit\n'
    ]
    configs = loopback_config + acl_config + interface0_config + interface1_config
    output = net_connect.send_config_set(configs)
    print(output)

#User info and choice of connection type

def main():
    host = '192.168.56.101'
    username = input('Please enter your username: ')
    password = getpass.getpass('Please enter your password: ')
    secret = 'cisco'

    choice = input('Would you like to connect by using telnet or ssh? ')

    if choice.lower() == 'telnet':
        device_type = 'cisco_ios_telnet'
    elif choice.lower() == 'ssh':
        device_type = 'cisco_ios'
    else:
        raise ValueError('Invalid - Please choose either telnet or ssh: ')

    device = {
        'device_type': device_type,
        'host': host,
        'username': username,
        'password': password,
        'secret': secret,
        'port': 22 if device_type == 'cisco_ios' else 23,
        'timeout': 100,
    }

#Connecting to device

    try:
        with ConnectHandler(**device) as net_connect:
            logging.info('Connection established')

#Sending config commands

            configure_device(net_connect)

# Saving config
            running_configuration = net_connect.send_command('show running-config')
            local_config_file_name = 'local_config.txt'
            save_config_to_file(running_configuration, local_config_file_name)
            logging.info(f'The configuration has been saved to {local_config_file_name}')

#comaprign config

            local_config_file_name = 'local_config.txt'

            try:
                with open(local_config_file_name, 'r') as local_config_file:
                    local_config = local_config_file.read()

                if running_configuration and local_config:
                    if running_configuration == local_config:
                        logging.info('The running configuration is the same as the local configuration')
                    else:
                        logging.warning('The running configuration does not match the local configuration: ')
                        show_differences(running_configuration, local_config)
                else:
                    logging.error('Failed to access configurations')

            except FileNotFoundError:
                logging.error(f'The local configurations file, ({local_config_file_name}), could not be found')

    except Exception as e:
        logging.error(f'An error occurred: {e}')

#Ending connection

    logging.info('The connection has concluded')
    net_connect.disconnect()
    
if __name__ == "__main__":
    main()
