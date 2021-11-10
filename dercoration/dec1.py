def func_out(num1):
    def func_in(num2):
        print(num1 + num2)
        return 1
    return func_in

test1 = func_out(2)
print(test1(2))