import requests
import re
import time
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

def city_list():
	f = open('city.txt', 'r', encoding='utf-8')
	g = f.read()
	h = re.findall('[0-9]{5,5}', g)
	f.close()
	return h

#获取数据返回字符串
def url_str_re(url):
	request = requests.get(url)
	str_request = request.content.decode('gbk', 'ignore')
	return str_request

def local_time():
	day = time.strftime("%Y-%m-%d", time.localtime())
	return day

#以当前的日期建立文件名
T = '%s.txt' %local_time()

#判断文件是否存在
if os.path.exists(T) == False:

	for i in city_list():
		url= "http://tianqi.2345.com/t/his/" + i + "his.js?"
		g = url_str_re(url)
		weather_txt = open(T, 'a', encoding='utf-8')
		weather_txt.write(g)
	weather_txt.close()
	print('存储成功')
else:
	print('文件已存在')

#获取后从TXT文件中查找关键字
def re_find(STR, FILE=T):
	f = open(FILE, 'r', encoding='utf-8')
	g = f.read()
	j = re.findall(STR, g)
	return len(j)

def  matplotlib_cir():
	# 指定字体为宋体
	zh_font = font_manager.FontProperties(fname=r'c:\windows\fonts\msyh.ttc', size=14)
	labels = '空气优', '空气良', '轻度污染', '中度污染', '重度污染'
	sizes = Wea_quali()
	colors = ['#3778bf', '#3ae57f', '#adf802', '#ab9004', '#8b2e16']
	explode = (0, 0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

	fig1, ax1 = plt.subplots()
	patches, l_text, p_text = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	shadow=True, startangle=90, colors=colors)

	# patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
	# 改变文本的大小
	# 方法是把每一个text遍历。调用set_size方法设置它的属性

	for t in l_text:
		t.set_size = (30)
	for t in p_text:
		t.set_size = (20)
	plt.title('天气情况',fontproperties=zh_font)
	plt.axis('equal', fontproperties=zh_font)
	plt.legend()
	plt.show()
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.show()

def Wea_quali():

	list_0 = ['空气优', '空气良', '轻度污染', '中度污染', '重度污染']
	list_1 = []
	for STR in list_0:
		i = re_find(STR)
		list_1.append(i)

	return list_1

matplotlib_cir()
"""
def re_find(A,txt_path):
	a = re.findall(A, txt_path)
	b = len(a)
	return print(A + str(b))


re_find('空气优', 'T')
re_find('空气良', 'T')
re_find('轻度污染', 'T')
re_find('中度污染', 'T')
re_find('重度污染', 'T')
"""

"""
f = open('citydata.txt', 'r', encoding='utf-8')
a = f.read()
b = set(re.findall('[0-9]{5,5}', a))
f.close()
print(b)
g = open('city.txt', 'a', encoding='utf-8')
for i in b:
	l = str(i) + '\n'
	g.write(l)
g.close()
提取城市代码并写入city.txt中。


re_find = re.findall('中国', str_request)
return re_find
"""