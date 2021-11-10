import math

import pandas as pd

list_data_all = []

def deal(list1):
    # 列表


    # list转dataframe
    df = pd.DataFrame(list1, columns=['mass', 'diameter', 'diameter_actual', 'c_actual', 'Re', 'lambda1', 'Pressure_per_length'])

    # 保存到本地excel
    df.to_excel("pipedata1.xlsx", index=False)



p_list = [9360,
3960,
1560,
480,
2400,
2040,
1320,
720,
1800,
1320,
3600,
2340,
1080
]
v_flowrate = 1.5  # 假设水的流速为多少 单位为米每秒
p_denisty = 983  # 水的密度 单位为 克每立方厘米
v = 0.4709 * 10**-6  # 动力粘度系数 Kg*m^2/s
k = 0.007  # 粗糙系数
# k = 0.0015
cq =  4.1868  # 该温度下水的比热容 Kj/Kg*K
ts = 80  # 初始温度  摄氏度
tr = 60  # 结束温度  摄氏度
mass1 = 5.74  # 可以不填给了再填

def mass_calulate(q_heatloss):
    mass = q_heatloss/(cq*(ts-tr))
    print("mass flow rate: %.2f"% mass)
    return mass


def diameter_choice(q_heatloss):
    value = (4*mass_calulate(q_heatloss))/(3.142*p_denisty*v_flowrate)
    diameter = 1000*((value)**0.5)
    diameter = round(diameter,3)
    print("最小管道内径：%.3f"% diameter)
    return diameter


# 这个是备用方法
def diameter_choice1(mass,v_flowrate):
    # value = (4*mass)/(3.142*p_denisty*v_flowrate)
    diameter = 1000*(((4*mass)/(3.142*p_denisty*v_flowrate))**0.5)
    diameter = round(diameter, 3)
    print("最小管道内径：%.3f" % diameter)
    return diameter


def actual_velocity(diameter_actual,q_heatloss):
    diameter_actual = diameter_actual/1000
    c_actual = (4*mass_calulate(q_heatloss))/(3.142*p_denisty*diameter_actual**2)
    c_actual = round(c_actual,3)
    print("用新管道算出来的流速%.3f"%c_actual)
    return c_actual


# 这个也是备用方法
def actual_velocity1(mass,diameter_actual):
    diameter_actual = diameter_actual/1000
    c_actual = (4*mass)/(3.142*p_denisty*diameter_actual**2)
    c_actual = round(c_actual,3)
    print("用新管道算出来的流速%.3f"%c_actual)
    return c_actual




def main(diameter_actual,c_actual):
    diameter_actual1 = diameter_actual / 1000
    Re = (diameter_actual1*c_actual)/v
    Re = round(Re)
    print("雷诺系数:%.2f"%Re)
    if Re > 2000:
        value1 = (6.9/Re) + (k/(diameter_actual*3.71))**1.11
        value2 = math.log10(value1)
        value3 = (-1.8)*value2
        lambda1 = (1/value3)**2
    else:
        lambda1 = 64/Re
    print("lambda值:%f" % lambda1)
    Pressure_per_length = (lambda1/diameter_actual1)*(0.5*p_denisty*c_actual**2)
    print("单位长度所受压力：%.2f"% Pressure_per_length)
    Pressure_per_length = round(Pressure_per_length,2)
    return Pressure_per_length,Re,lambda1


def run_main2():
    diameter_choice1(mass1,v_flowrate)
    diameter_actual = float(input("请输入你选择的管道内径："))
    c_actual = actual_velocity1(mass1,diameter_actual)
    main(diameter_actual,c_actual)


def run_main1():
    for index, p_one in enumerate(p_list):
        mass = mass_calulate(p_one)
        diameter = diameter_choice(p_one)
        # diameter_actual = choice_list[index]
        diameter_actual = float(input("请输入你选择的管道内径："))
        c_actual = actual_velocity(diameter_actual,p_one)
        Pressure_per_length,Re,lambda1 = main(diameter_actual,c_actual)
        list_data_all.append([mass,diameter,diameter_actual,c_actual,Re,lambda1,Pressure_per_length])
        print(f"第{index+1}结束")
        print("="*100)
    print(list_data_all)
    deal(list_data_all)

if __name__ == '__main__':
    run_main1()
    # run_main2()




