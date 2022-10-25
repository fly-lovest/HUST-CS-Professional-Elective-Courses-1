# 程序功能：统计出京东在售商品中各码数服装所占比例，以饼状图展示

import xlrd
import matplotlib.pyplot as plt

xl = xlrd.open_workbook(r'C:\Users\LH2019\Desktop\jd_data.xlsx') # 读取数据表格文件的地址
mysheet = xl.sheets()[0]

s = 0
m = 0
l = 0
xl = 0
xxl = 0
xxxl = 0
row = 1
while row <= 495376:
    data = mysheet.cell(row,0).value
    if 'S' in data:
        s += 1
    if 'M' in data:
        m += 1
    if 'XXXL' in data or '3XL' in data:
        xxxl += 1
    elif 'XXL' in data or '2XL' in data:
        xxl += 1
    elif 'XL' in data:
        xl += 1
    elif 'L' in data:
        l += 1
    else:
        pass
    row += 1

# 画饼状图
name_list = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
num_list = [s, m, l, xl, xxl, xxxl]
# 保证圆形
plt.axes(aspect=1)
plt.pie(x=num_list, labels=name_list, autopct='%3.1f %%')
plt.show()