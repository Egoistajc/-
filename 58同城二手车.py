import requests
import xlwt
from bs4 import BeautifulSoup as bs
n = "1"
a = 0
b=1
calc=0 #用于计数的变量
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")
sheet.write(0, 0, '二手车品牌')
sheet.write(0, 1, '二手车系列')
sheet.write(0, 2, '二手车年份')
sheet.write(0, 3, '二手车价格')
url = "https://bj.58.com/ershouche/pn" + n + "/?pane=true&PGTID=0d30001d-0000-1c2d-c765-e266ab6bfc82&ClickID=29"
positionList = [] # 存放爬取的所有内容
position = [] # 存放单次爬取的内容
primary = [] # 这个是后面用的列表，存取positionList[]里面的多个字符串转化成的多个浮点型的数据
for i in range(1, 250): # 这里是个循环，循环爬取250 页的数据.
    n = str(i) # 此处的i 是循环次数，需要先转化成字符才可以
    url = "https://bj.58.com/ershouche/pn" + n + "/?pane=true&PGTID=0d30001d-0000-1c2d-c765-e266ab6bfc82&ClickID=29"

    response = requests.get(url)
    soup = bs(response.text,"html.parser")
    ul = soup.find(attrs={"class": "car_pane clearfix ac_container"})
    lis = ul.find_all("li")
    i=1
    for li in lis:
        list=(li.find('h5').text).replace(' ', ' ').replace('\n', '').replace('\r', '').strip().split()
        list2=li.find('h4').text
        sheet.write(b, 0, list[0])
        sheet.write(b, 1, list[1])
        sheet.write(b, 2, list[2])
        sheet.write(b, 3, list2)
        b+=1
        i+=1
    workbook.save("58_old_car.xls")
print("10000 条数据爬取完成，已经存入与该文件同级目录下的58_old_car.xls")