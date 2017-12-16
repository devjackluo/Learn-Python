import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(s)
server = 'pythonprogramming.net'


'''
port = 80
server_ip = socket.gethostbyname(server)
request = 'GET / HTTP/1.1\nHost: '+server+"\n\n"
s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)
#print(result)
while(len(result) > 0):
    print(result)
    result = s.recv(2)
'''

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print("Port",x,'is closed')