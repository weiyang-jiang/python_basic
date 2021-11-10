# 1. 添加学员
# 2. 删除学员
# 3. 修改学员信息
# 4. 查询学员信息
# 5. 显示所有学员信息
# 6. 退出系统
from StudentSystemManager.students import Students
import re
import ast

# 添加学员
class system_students(object):

    # 读取文件信息
    def read_list(self):
        student_list = []
        f = open("student.txt","wb+")
        while True:
            content = f.readline().decode("utf8")
            content = re.sub("\n","",content)
            if len(content) == 0:
                break
            student_list.append(ast.literal_eval(content))
        f.close()
        return student_list

    # 添加修改文件
    def add_list(self, content,func="write"):
        if func == "write":
            f = open("student.txt","ab")
            f.write(content)
        else:
            f = open("student.txt","wb")
            f.writelines(content)
        f.close()

    # 添加学员
    def add_info(self):
        while True:
            name = input("请输入你的名字：")
            age = input("请输入你的年龄：")
            tel = input("请输入你的手机号：")
            student = Students(name=name,age=age,tel=tel)
            item = {"姓名": student.name, "年龄": student.age, "电话": student.tel}
            student_list2 = self.read_list()
            student_list1 = list(map(lambda x: list(x.values())[0], student_list2))
            if name not in student_list1:
                item = f"{item}" + "\n"
                self.add_list(item.encode("utf8"))
                print("成功添加学员信息")
                num1 = int(input("您是否要继续添加(继续添加输入1，退出输入0）："))
                if num1 == 0:
                    return
            else:
                i = int(input("学员信息已存在,如果退出添加请输入0,重新添加请输入1："))
                if i == 0:
                    return

    # 删除学员
    def del_info(self):
        while True:
            name = input("请输入要删除的学生的姓名：")
            student_list2 = self.read_list()
            student_list1 = list(map(lambda x: list(x.values())[0], student_list2))
            if name in student_list1:
                index = student_list1.index(name)
                student_list2.pop(index)
                student_list3 = list(map(lambda x:f"{x}".encode("utf8")+"\n".encode("utf8"),student_list2))
                self.add_list(student_list3,func="writelines")
                print(f"已删除学员：{name}")
                num1 = int(input("您是否要继续删除(继续删除输入1，退出输入0）："))
                if num1 == 0:
                    return
            else:
                i = int(input(f"列表中不存在（{name}）学员信息,如果退出删除请输入0,重新删除请输入1："))
                if i == 0:
                    return

    # 修改信息
    def modify_info(self):
        while True:
            name = input("请输入要修改的学生的姓名：")
            student_list2 = self.read_list()
            student_list1 = list(map(lambda x: list(x.values())[0], student_list2))
            if name in student_list1:
                index = student_list1.index(name)
                while True:
                    whether = input("请输入你要修改的信息名称：")
                    if whether == "年龄":
                        data = input("请输入你修改后的年龄：")
                        student_list2[index]["年龄"] = data
                        student_list3 = list(map(lambda x: f"{x}".encode("utf8") + "\n".encode("utf8"), student_list2))
                        self.add_list(student_list3,func="writelines")
                        print(f"成功修改信息{student_list2[index]}")
                        num1 = int(input("您是否要继续修改(继续修改输入1，退出输入0）："))
                        if num1 == 0:
                            return
                        elif num1 == 1:
                            break
                    elif whether == "电话":
                        data = input("请输入你修改后的电话：")
                        student_list2[index]["电话"] = data
                        student_list3 = list(map(lambda x: f"{x}".encode("utf8") + "\n".encode("utf8"), student_list2))
                        self.add_list(student_list3, func="writelines")
                        print(f"成功修改信息{student_list2[index]}")
                        num1 = int(input("您是否要继续修改(继续修改输入1，退出输入0）："))
                        if num1 == 0:
                            return
                        elif num1 == 1:
                            break
                    else:
                        num = int(input(f"不存在（{whether}）信息系统（重新输入信息名称请输入1，退出输入0）："))
                        if num == 0:
                            return
            else:
                i = int(input(f"（{name}）学员不在系统里面(重新输入姓名请输入1，退出系统请输入0）："))
                if i == 0:
                    return

    # 查询指定的信息
    def search_info(self):
        while True:
            name = input("请输入要查找的学生的姓名：")
            student_list2 = self.read_list()
            student_list1 = list(map(lambda x: list(x.values())[0], student_list2))
            if name in student_list1:
                index = student_list1.index(name)
                while True:
                    whether = input("请输入你要查找的信息名称：")
                    if whether == "年龄":
                        age = student_list2[index]["年龄"]
                        print(f"姓名：{name}")
                        print(f"年龄：{age}")
                        num1 = int(input("您是否要继续查找(继续查找输入1，退出输入0）："))
                        if num1 == 0:
                            return
                        elif num1 == 1:
                            break
                    elif whether == "电话":
                        tel = student_list2[index]["电话"]
                        print(f"姓名：{name}")
                        print(f"电话：{tel}")
                        num1 = int(input("您是否要继续查找(继续查找输入1，退出输入0）："))
                        if num1 == 0:
                            return
                        elif num1 == 1:
                            break
                    else:
                        num = int(input(f"不存在（{whether}）信息系统（重新输入信息名称请输入1，退出输入0）："))
                        if num == 0:
                            return

            else:
                i = int(input(f"（{name}）学员不在系统里面(重新输入姓名请输入1，退出系统请输入0）："))
                if i == 0:
                    return

    # 查询所有学员信息
    def print_all(self):
        student_list2 = self.read_list()
        for student in student_list2:
            print(f"姓名：{student['姓名']},年龄：{student['年龄']},电话：{student['电话']}")
            print("="*20)













