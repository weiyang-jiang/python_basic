import pandas as pd
import numpy as np
from datetime import datetime

#要处理的文件
file_name = r"C:\python\10 报表统计\账单.csv"
#输出文件名
out_name = "out.xls"
writer = pd.ExcelWriter(out_name)

#读入数据
#数据标题从哪一行开始，就是减1
header = 16
#如果是读取excel文件，请替换为read_excel
data=pd.read_csv(file_name ,header = header)
#处理金额中￥字符
data["金额(元)"] = pd.to_numeric(data["金额(元)"].str[1:], errors='ignore')
#处理时间序列
data["交易时间"] = pd.to_datetime(data["交易时间"], errors='ignore')
#增加两列data["月份"]=data["交易时间"].apply(lambda x : x.strftime('%Y-%m'))
data["时段"]=data["交易时间"].apply(lambda x : x.strftime('%H'))

#输出原始数据
data.to_excel(excel_writer=writer,sheet_name='原始数据')



#按交易时间分析
#横轴
x = ["月份","收/支"]
#纵轴
y = ["金额(元)"]
#关注的函数 次数 len   求和sum  最大max  最小 min  平均 np.mean
func = {len}
data_0 = pd.pivot_table(data,index=x,values=y,aggfunc=func,fill_value=0)
data_0.to_excel(excel_writer=writer,sheet_name='交易时间分析')





#导出数据
writer.save()
writer.close()
print("完成")