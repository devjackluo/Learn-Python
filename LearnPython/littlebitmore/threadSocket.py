import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'youtube.com'

def portscan(port):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port,'is open!')
        con.close()
    except:
        pass

def threader():
    while True:
        work = q.get()
        portscan(work)
        q.task_done()

q = Queue()

for worker in range(800):
    t = threading.Thread(target= threader)
    t.daemon = True
    t.start()

for work in range(1,10001):
    q.put(work)

q.join()