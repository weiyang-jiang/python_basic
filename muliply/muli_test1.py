from multiprocessing import Process
import time
import os
def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(1)

def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(1)

# if os.getppid() == 11532:
if __name__ == '__main__':
    dance_process = Process(target=dance)
    dance_process.start()
    sing_process = Process(target=sing)
    sing_process.start()

