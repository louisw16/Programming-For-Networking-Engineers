import pexpect

class NetworkDevice():

    def __init__(self, name,ip, user='cisco', pw='cisco123!'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, unknown get interfaces ---'

class NetworkDeviceIOS(NetworkDevice):
    
    def __init__(self, name, ip, user='cisco', pw='cisco123!'):
        NetworkDevice.__init__(self, name, ip, user, pw)
 
    def connect(self):
        print('--- connecting IOS: telnet ' + self.ip_address)
        
        self.session = pexpect.spawn('telnet ' + self.ip_address, encoding='utf-8', timeout=20)
 
        result = self.session.expect(['Username:', pexpect.TIMEOUT, pexpect.EOF])
 
        self.session.sendline(self.username)
 
        result = self.session.expect('Password:')

        self.session.sendline(self.password)
        
        self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
 
        self.session.sendline('terminal length 0')
        result = self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
    
    def get_interfaces(self):
 
        self.session.sendline('show interfaces summary')
        result = self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
 
        self.interfaces = self.session.before

class NetworkDeviceXR(NetworkDevice):

    def __init__(self, name, ip, user='cisco', pw='cisco123!'):
        NetworkDevice.__init__(self, name, ip, user, pw)

    def connect(self):
 
        print('--- connecting XR: ssh '+ self.username + '@' + self.ip_address)

    self.session = pexpect.spawn('ssh ' + self.username + '@' + self.ip_address, encoding='utf-8', timeout=20)
    
    result = self.session.expect(['password:', pexpect.TIMEOUT, pexpect.EOF])

    if result != 0:
        print('--- Timout or unexpected reply from device')
        return 0
 
        print('--- password:', self.password)
        self.session.sendline(self.password)
        self.session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
 
    def get_interfaces(self):
 
        self.session.sendline('show interface brief')
        result = self.session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
 
        self.interfaces = self.session.before
        