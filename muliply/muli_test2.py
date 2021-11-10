import threading
import time
time1 = time.time()
num = 0
lock1 = threading.Lock()

def task1():
    lock1.acquire()
    for i in range(10000000):
        global num
        num += 1
    print(num)
    time2 = time.time() - time1
    print(time2)
    lock1.release()

def task2():
    lock1.acquire()
    for i in range(10000000):
        global num
        num += 1
    print(num)
    time2 = time.time() - time1
    print(time2)
    lock1.release()

if __name__ == '__main__':
    threading1 = threading.Thread(target=task1)
    threading2 = threading.Thread(target=task2)
    threading1.start()
    threading2.start()
