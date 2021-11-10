from StudentSystemManager.student_system import system_students

# 主要运行窗口
def print_info():
    student1 = system_students()
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
                student1.add_info()
            elif num == 2:
                print("删除学员")
                student1.del_info()
            elif num == 3:
                print("修改学员信息")
                student1.modify_info()
            elif num == 4:
                print("查询学员信息")
                student1.search_info()
            elif num == 5:
                print("显示所有学员信息")
                student1.print_all()
            elif num == 6:
                print("退出系统")
                break
            else:
                print("输入不正确，请重新输入")
        except:
            print("输入不正确，请重新输入")

if __name__ == '__main__':
    print_info()