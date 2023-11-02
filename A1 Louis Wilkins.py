from netmiko import ConnectHandler
import getpass

host = ''
username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
secret = 'cisco'

choice = input('Would you like to connect by using telnet or ssh?')

if choice.lower == 'telnet':
     device = {
     'device_type': 'cisco_ios_telnet',
     'host': host,
     'username': username,
     'password': password,
     'secret': secret,
     }

elif choice.lower == "ssh":
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


#net_connect = ConnectHandler(**device)
#print('Connection established')

#net_connect.send_command('en')


try:
    net_connect = ConnectHandler(**device)
    print('Conncection eastablished')

    try:
        net_connect.send_command('en')

        try:
            net_connect.send_command(secret)
            print('Privilaged exec mode entered')

            try:
                net_connect.send_command('conf t')
                print('Configuration mode entered')
            
                try:
                    net_connect.send_config_set('hostname R1')
                    print('Hostname changed to R1')

                    try:
                        output = net_connect.send_command('show run')
                        with open('router_config.txt', 'w') as f:
                            f.write(output)

                        print('Configuration saved to router_config.txt.')

                    except Exception as e:
                        print(f'An error occurred while saving the configuration: {e}')

                except Exception as e:
                    print(f'An error occurred while changing the hostname: {e}')

            except Exception as e:
                print(f'An error occurred while entering configuration mode: {e}')

        except Exception as e:
                print(f'An error occurred while entering privilaged exec mode: {e}')
    except Exception as e:
        print(f'An error occured while entering privilaged exec mode: {e}')


        net_connect.disconnect()
        print('The onnection has concluded')

except Exception as e:
    print(f'An error occurred: {e}')
