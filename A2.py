from netmiko import ConnectHandler
import getpass

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
    print('Conncection eastablished')

    try:
        net_connect.send_command('en')

        #try:
            #net_connect.send_command(secret)
            #print('Privilaged exec mode entered')

        try:
            net_connect.send_command('conf t')
            print('Configuration mode entered')
        
            try:
                net_connect.send_config_set('hostname R1')
                print('Hostname changed to R1')

            except Exception as e:
                print(f'An error occurred while changing the hostname: {e}')

        except Exception as e:
            print(f'An error occurred while entering configuration mode: {e}')

        #except Exception as e:
                #print(f'An error occurred while entering privilaged exec mode: {e}')
    
    except Exception as e:
        print(f'An error occured while entering privilaged exec mode: {e}')


    net_connect.disconnect()
    print('The connection has concluded')

except Exception as e:
    print(f'An error occurred: {e}')
