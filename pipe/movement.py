class Funiture():
    def __init__(self,name,area):
        self.fun_name = name
        self.fun_area = area


class House(Funiture):
    def __init__(self,location,house_area):
        self.location = location
        self.house_area = house_area
        self.etra_area = house_area
        self.funitures = []


    def add_funiture(self,fun_name,fun_area):
        Funiture.__init__(self,fun_name,fun_area)
        if self.etra_area > self.fun_area:
            self.etra_area -= self.fun_area
            self.funitures.append(self.fun_name)
        else:
            print(f"房屋剩余面积不足，家具{self.fun_name}摆放不了")

    def __str__(self):
        return f"房屋位置{self.location}，房屋总面积{self.house_area}，房屋剩余面积{self.etra_area}，房屋摆放的家具列表{self.funitures}"

if __name__ == '__main__':
    house = House(location="大连",house_area=180)
    print(house)
    house.add_funiture(fun_area=10,fun_name="衣柜")
    print(house)
    house.add_funiture(fun_area=20,fun_name="床")
    print(house)
