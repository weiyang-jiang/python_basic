# with open("static/grand.html", "rb") as file:
#     file_data = file.read()
# print(file_data)
#
# a= "123"
# print(a.encode())
# print(a.isalpha())

import pandas
data = pandas.read_excel("2.xlsx")
data1_list = []
data2_list = []
data_list = []
data1_list1 = []
for data1 in data.values:
    data1_list.append(list(data1)[0])
    data2_list.append(list(data1)[1])
data1_list = data1_list[::-1]
data2_list = data2_list[::-1]
print(data1_list)
print(data2_list)
for i in range(len(data2_list)-1):
    value1 = data2_list[i]+data2_list[i+1]
    value2 = data1_list[i+1] - data1_list[i]
    value3 = 0.5*value1*value2
    data_list.append(value3)
for i in range(len(data2_list)):
    value5 = 4*data2_list[i]*data1_list[i]
    data1_list1.append(value5)
datas = sum(data_list)
print(data_list)
print(datas)
print(-sum(data1_list1))

a = "aaa"
print(a.startswith())