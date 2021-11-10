from math import *

class gutter_select(object):
    def __init__(self,width,angle_roof,length,angle_choose,coeff,intensity=0.021):
        self.intensity = intensity
        self.width = width
        self.angle_roof = angle_roof
        self.length = length
        self.angle_choose = angle_choose
        self.coeff = coeff
    def calculate_area(self,value1=None):
        if value1 == None:
            value1 = 1 + (tan(radians(self.angle_choose)) * tan(radians(self.angle_roof)))
        area = value1 * self.width * self.length * self.coeff
        area = round(area,2)

        return area

    def cl_flow_load(self,i):
        flow_load = self.calculate_area() * self.intensity
        print(f"雨水流速容量为：{flow_load}")
        if i == 2:
            print("之前选的流速容量太小现在换一个")
        flow_load = float(input("请输入你选择的流速容量："))
        return flow_load

    def reduction_factor(self):
        i = 1
        print(f"有效面积为{self.calculate_area()}")
        while True:
            flow_load = self.cl_flow_load(i)
            gutter_size = int(input(f"第{i}次循环下,请输入你选择的管道直径："))
            ratio = self.length/(gutter_size*0.5*0.001)
            print(f"第{i}次循环下,管道的比率值为{ratio}")
            a = float(input(f"第{i}次循环下,左上："))
            b = float(input(f"第{i}次循环下,左下："))
            c = float(input(f"第{i}次循环下,右上："))
            d = float(input(f"第{i}次循环下,右下："))
            factor = c + ((d-c)*(ratio-a)/(b-a))
            factor = round(factor,2)
            print(f"第{i}次循环下,factor的值为{factor}")
            new_flow = factor * flow_load
            print(f"第{i}次循环下，新的new_flow值为{new_flow}")
            if new_flow > self.calculate_area() * self.intensity:
                print(f"第{i}次循环下，新的gutter_size值为{gutter_size}")
                return gutter_size
            else:
                print(f"第{i}次循环下，new_flow的值不满足要求")
            i += 1


if __name__ == '__main__':
    # gutter_selects = gutter_select(width=4,length=8,angle_roof=45,angle_choose=26.6)
    # gutter_selects.reduction_factor()
    coeff = (2.532+7.098)/(7.098*2)
    gutter_selects = gutter_select(coeff=coeff, width=4.381, length=7.098, angle_roof=38, angle_choose=26.6)
    # coeff = 0.5
    # gutter_selects = gutter_select(coeff=coeff,width=4.565,length=8.782,angle_roof=38,angle_choose=26.6)
    gutter_selects.reduction_factor()


