import socket

class UDP:
    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')
        self.port = kwargs.get('port')
        self.listen_ip = kwargs.get('lip')
        self.listen_port = kwargs.get('lport')

    def send(self, message):
        '''
        Simply sends UDP packet to the
        set ip and port, no questions
        asked.
        '''
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode('utf-8'), (self.ip, self.port))
        print(f"hawk.send {message} -> [{self.ip}]")

    def get(self, **kwargs):
        ''' 
        Listens for UDP requests on the
        previously set listen_ip and listen_port.
        Ignores ip and port unless the excl keyword
        argument is set to boolean True.
        '''
        
        buffer = kwargs.get('buffer')
        exclusive = kwargs.get('excl')

        if excl == "y":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(self.listen_ip, self.listen_port)
            while True:
                received_data, address = sock.recvfrom(int(buffer))
                if (address[0] == self.ip):
                    print(f"[{address}] -> hawk.get: {received_data}")    
                else:
                    pass
            sock.close()
        elif excl == "n":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.listen_ip, self.listen_port))
            while True:
                received_data, address = sock.recvfrom(int(buffer))
                print(f"[{address}] -> hawk.get: {received_data.decode('utf-8')}")
            sock.close()
        else:
            print("Bad kwarg used for /exclusive/. Please only enter y/n as a kwarg.")

