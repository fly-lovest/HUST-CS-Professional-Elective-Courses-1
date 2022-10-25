# 程序功能：1、得出京东商品中男包女包所占的比例, 并画出饼图以直观表示
#          2、统计京东商品中男包女包的平均价格

import xlrd
import matplotlib.pyplot as plt

xl = xlrd.open_workbook(r'C:\Users\LH2019\Desktop\jd_data.xlsx') # 读取数据表格文件的地址
mysheet = xl.sheets()[0]

male = 0
price_male = 0
female = 0
price_female = 0
row = 1
interference_list = ['包臀','面包','全包','包头','包边','包邮','表情包','包装','礼包','包芯','包裙']
while row <= 495376:
    data = mysheet.cell(row,0).value
    if data != '' and mysheet.cell(row,1).value != '0.05/千字' and mysheet.cell(row,1).value != '暂无报价' and mysheet.cell(row,1).value != '价格':
        price = float(mysheet.cell(row,1).value)
        if '包' in data:
            flag = 1
            for item in interference_list:
                if item in data:
                    flag = 0
            if flag == 1:
                if '男' in data: 
                    male += 1
                    price_male += price
                if '女' in data:
                    female += 1
                    price_female += price
    row += 1

print('男包比例：', male*100/(male+female),'%')
print('女包比例：', female*100/(male+female),'%')
print('男包平均价格：', price_male/male)
print('女包平均价格：', price_female/female)

# 画饼状图
name_list = ['male', 'female']
num_list = [male, female]
# 保证圆形
plt.axes(aspect=1)
plt.pie(x=num_list, labels=name_list, autopct='%3.1f %%')
plt.show()
