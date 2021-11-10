# 装饰器的使用
import time
def decrator(func):
    def inner(*args,**kwargs):
        sta_time = time.time()
        result = func(*args,**kwargs)
        pro_time = time.time() - sta_time
        print(pro_time)
        return result
    return inner

@decrator
def while_func():
    for i in range(5):
        time.sleep(0.5)


@decrator
def sum_func(a,b):
    print(a+b)

while_func()
sum_func(1,6)