# class master(object):
#     def __init__(self):
#         self.path = "爷爷"
#
#     def print_info(self):
#         print(self.path)
#
#
# class mine(master):
#     def __init__(self):
#         self.path = "爸爸"
#
#     def print_info(self):
#         print(self.path)
#
#     def print_grandpa(self):
#         super().__init__()
#         super().print_info()
#
#
# class son(mine):
#     def __init__(self):
#         self.path = "儿子"
#
#     @staticmethod
#     def print_info1():
#
#         son().print_dad()
#
#
#
#     def print_dad(cls):
#         super().__init__()
#         super().print_info()
#
# son().print_dad()








class Error(Exception):
    def __init__(self, length, limit):
        super().__init__()
        self.length = length
        self.limit = limit
    def __str__(self):
        return f"数据长度为{self.length},超出限制长度{self.limit}"

try:
    try:
        password = "30000"
        if len(password) > 3:
            raise Error(length=len(password),limit=3)

    except Exception as result:
        print(result)

    else:
        print("密码输入正确")

except Exception as result:
    print(result)













