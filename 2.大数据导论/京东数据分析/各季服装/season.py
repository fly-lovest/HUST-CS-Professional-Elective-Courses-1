# 本程序功能：1、利用matplotlib绘图库画出当前京东各季服装数量
#            2、输出夏季及反季服装所占的比例

import xlrd
import matplotlib.pyplot as plt

xl = xlrd.open_workbook(r'C:\Users\LH2019\Desktop\jd_data.xlsx')
mysheet = xl.sheets()[0]

spr_aut = 0
summer = 0
winter = 0
row = 1
while row <= 495376:
    data = mysheet.cell(row,0).value
    if '夏' in data:
        summer += 1
    if '春' in data or '秋' in data:
        spr_aut += 1
    if '冬' in data:
        winter += 1
    row += 1

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

print('夏季服装所占比例：', summer*100/(summer+spr_aut+winter),'%')
print('反季服装所占比例：', winter*100/(summer+spr_aut+winter),'%')
name_list = ['Summer', 'Spring/Autumn', 'Winter']
num_list = [summer, spr_aut, winter]
autolabel(plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list))
plt.show()


    
    

