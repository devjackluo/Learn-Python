import threading
from queue import Queue
import time

workTypeOne = 0
workTypeTwo = 0
print_lock = threading.Lock()


def exampleJob(worker):

    time.sleep(0.1)
    with print_lock:
        #print(print_lock)
        print("doing job ___",threading.current_thread().name,worker)
        global workTypeOne
        workTypeOne+=1
    #print(print_lock)


def exampleJobTwo(worker):

    time.sleep(0.5)
    # same is try and finally. trys locks any thread from moving then finally release lock.
    with print_lock:
        print("doing job two",threading.current_thread().name,worker)
        global workTypeTwo
        workTypeTwo+=1




#different threads are given one of these jobs
def threaderTypeTwoJob():
    while True:
        work = q.get()
        exampleJobTwo(work)
        q.task_done()


def threaderTypeOneJob():
    while True:
        work = q.get()
        exampleJob(work)
        q.task_done()


#start = time.time()


#create a queue of work to be done.
q = Queue()

#create x amount of threads(workers) with daemons(managers to tell them to go home/work)
for x in range(20):
    if x < 10:
        t = threading.Thread(target=threaderTypeOneJob)
    else:
        t = threading.Thread(target=threaderTypeTwoJob)
    t.daemon = True
    t.start()


#threads are waiting for queue to work on so you create items for the queue.
for work in range(100):
    q.put(work)

# blocks main queue and 'join'? new tasks to main queue?
q.join()


#print('Entire job took:', time.time()-start)
print(workTypeOne)
print(workTypeTwo)

