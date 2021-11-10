import time

time1 = time.time()
num = 0
for i in range(10):
    num += 1
    time.sleep(0.1)

for i in range(10):
    num += 1
    time.sleep(0.1)
print(time.time()-time1)
print(num)

