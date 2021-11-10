# 1. 添加学员
# 2. 删除学员
# 3. 修改学员信息
# 4. 查询学员信息
# 5. 显示所有学员信息
# 6. 退出系统
student_list = []
def print_info():
    while True:
        num = input("""-------------------------
1. 添加学员
2. 删除学员
3. 修改学员信息
4. 查询学员信息
5. 显示所有学员信息
6. 退出系统
-------------------------
请输入你要选择的功能：""")
        try:
            num = int(num)
            if num == 1:
                print("添加学员")
                add_info()
            elif num == 2:
                print("删除学员")
                del_info()
            elif num == 3:
                print("修改学员信息")
                modify_info()
            elif num == 4:
                print("查询学员信息")
                search_info()
            elif num == 5:
                print("显示所有学员信息")
                print_all()
            elif num == 6:
                print("退出系统")
                break
            else:
                print("输入不正确，请重新输入")
        except:
            print("输入不正确，请重新输入")
# 添加学员
def add_info():
    while True:
        global student_list
        name = input("请输入你的名字：")
        age = input("请输入你的年龄：")
        item = {"姓名": name, "年龄": age}
        student_list1 = list(map(lambda x: list(x.values())[0], student_list))
        if name not in student_list1:
            student_list.append(item)
            print("成功添加学员信息")
        else:
            i = int(input("学员信息已存在,如果退出添加请输入0,重新添加请输入1："))
            if i == 0:
                return
        print(student_list)
        num1 = int(input("您是否要继续添加(继续添加输入1，退出输入0）："))
        if num1 == 0:
            return

# 删除学员
def del_info():
    while True:
        global student_list
        name = input("请输入要删除的学生的姓名：")
        student_list1 = list(map(lambda x: list(x.values())[0], student_list))
        if name in student_list1:
            index = student_list1.index(name)
            student_list.pop(index)
            print(f"已删除学员：{name}")
        else:
            i = int(input(f"列表中不存在（{name}）学员信息,如果退出删除请输入0,重新删除请输入1："))
            if i == 0:
                return
        print(student_list)
        num1 = int(input("您是否要继续删除(继续删除输入1，退出输入0）："))
        if num1 == 0:
            return

# 修改信息
def modify_info():
    while True:
        global student_list
        name = input("请输入要修改的学生的姓名：")
        student_list1 = list(map(lambda x: list(x.values())[0], student_list))
        if name in student_list1:
            index = student_list1.index(name)
            while True:
                whether = input("请输入你要修改的信息名称：")
                if whether == "年龄":
                    data = input("请输入你修改后的年龄：")
                    student_list[index]["年龄"] = data
                    print(f"成功修改信息{student_list[index]}")
                    break
                else:
                    num = int(input(f"不存在（{whether}）信息系统（重新输入信息名称请输入1，退出输入0）："))
                    if num == 0:
                        return
            print(student_list)
            num1 = int(input("您是否要继续修改(继续修改输入1，退出输入0）："))
            if num1 == 0:
                return
        else:
            i = int(input(f"（{name}）学员不在系统里面(重新输入姓名请输入1，退出系统请输入0）："))
            if i == 0:
                return




def search_info():
    while True:
        global student_list
        name = input("请输入要查找的学生的姓名：")
        student_list1 = list(map(lambda x: list(x.values())[0], student_list))
        if name in student_list1:
            index = student_list1.index(name)
            while True:
                whether = input("请输入你要查找的信息名称：")
                if whether == "年龄":
                    age = student_list[index]["年龄"]
                    print(f"姓名：{name}")
                    print(f"年龄：{age}")
                    break
                else:
                    num = int(input(f"不存在（{whether}）信息系统（重新输入信息名称请输入1，退出输入0）："))
                    if num == 0:
                        return
            print(student_list)
            num1 = int(input("您是否要继续查找(继续查找输入1，退出输入0）："))
            if num1 == 0:
                return
        else:
            i = int(input(f"（{name}）学员不在系统里面(重新输入姓名请输入1，退出系统请输入0）："))
            if i == 0:
                return

def print_all():
    global student_list
    for student in student_list:
        print(f"姓名：{student['姓名']},年龄：{student['年龄']}")
        print("="*20)
    print(student_list)












if __name__ == '__main__':
    print_info()