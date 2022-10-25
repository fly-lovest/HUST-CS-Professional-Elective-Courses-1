# 本程序功能：算出帽、恤、裙、裤、鞋在京东在售服装中所占的比例，最终用饼状图呈现

import xlrd
import matplotlib.pyplot as plt

xl = xlrd.open_workbook(r'C:\Users\LH2019\Desktop\jd_data.xlsx') # 读取数据表格文件的地址
mysheet = xl.sheets()[0]
hat = 0
shirt = 0
skirt = 0
trousers = 0
shoes = 0
row = 1
while row <= 495376:
    data = mysheet.cell(row,0).value
    if '帽' in data:
        hat += 1
    if '恤' in data:
        shirt += 1
    if '裙' in data:
        skirt += 1
    if '裤' in data:
        trousers += 1
    if '鞋' in data:
        shoes += 1
    row += 1

# 画饼状图
name_list = ['hat', 'shirt', 'skirt', 'trousers', 'shoes']
num_list = [hat, shirt, skirt, trousers, shoes]
# 保证圆形
plt.axes(aspect=1)
plt.pie(x=num_list, labels=name_list, autopct='%3.1f %%')
plt.show()
