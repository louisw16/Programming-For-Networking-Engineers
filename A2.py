from netmiko import ConnectHandler
import getpass
import difflib

def save_config_to_file(config, filename):
    with open(filename, 'w') as config_file:
        config_file.write(config)
    print(f'Configuration saved to {filename}')

def show_differences(config1, config2):
    difference = difflib.Differ()
    diff = list(difference.compare(config1.splitlines(), config2.splitlines()))

    for line in diff:
        
        if line.startswith('- '):
            print(f'Present in ({config1}): {line[2:]}')

        elif line.startswith('+ '):
            print(f'Present in ({config2}): {line[2:]}')

host = '192.168.56.101'
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
secret = 'cisco'

choice = input('Would you like to connect by using telnet or ssh? ')

if choice.lower() == 'telnet':
     device = {
     'device_type': 'cisco_ios_telnet',
     'host': host,
     'username': username,
     'password': password,
     'secret': secret,
     }

elif choice.lower() == 'ssh':
    device = {
    'device_type': 'cisco_ios',
    'host': host,
    'username': username,
    'password': password,
    'secret': secret,
    'port': 22,
    }

else:
    raise ValueError('Invalid - Please choose either telnet or ssh: ')


try:
    net_connect = ConnectHandler(**device)
    print('Connection established')

    running_configuration = net_connect.send_command('show running-config')

    local_config_file_name = 'local_config.txt'
    save_config_to_file(running_configuration, local_config_file_name)
    print(f'The configuration has been saved to {local_config_file_name}')

    try:
        net_connect.send_command('en')
        print('Privilaged exec mode entered')

        try:
            net_connect.send_command('terminal length 0')

            try:
                running_config = net_connect.send_command('show run')

                try:
                    startup_config = net_connect.send_command('show start')

                    if running_config and startup_config:

                        if running_config == startup_config:
                            print('The running configuration is the same as the startup configuration')

                        else:
                            print('The running configuration does not match the startup configuration: ')
                            show_differences(running_config, startup_config)

                    else:
                        print('Failed to access configurations')

                except Exception as e:
                    print(f'An error occured while showing the startup configuration: {e}')

            except Exception as e:
                print(f'An error occured while showing the running configuration: {e}')

        except Exception as e:
            print(f'An error occured while altering the terminal length: {e}')

    except Exception as e:
        print(f'An error occured while entering privilaged exec mode: {e}')



    local_config_file_name = 'local_config.txt'

    try:
        with open(local_config_file_name, 'r') as local_config_file:
            local_config = local_config_file.read()

        if running_config and local_config:
            
            if running_config == local_config:
                print('The running configuration is the same as the local configuration')

            else:
                print('The running configuration does not match the local configuration: ')
                show_differences(running_config, local_config)

        else:
            print('Failed to access configurations')

    except FileNotFoundError:
        print(f'The local configurations file, ({local_config_file_name}), could not be found')

except Exception as e:
    print(f'An error occurred: {e}')

net_connect.disconnect()
print('The connection has concluded')