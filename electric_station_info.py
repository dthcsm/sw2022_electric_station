import requests

url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
params ={'serviceKey' : '8vw9k95QJ4Rb88ba9wp2SRUDOzJv1/dE9kvQOFiqkW8M+NqwKJBnRUG3IBmLqLVnIesJnulJYfU4xV90oXoXew=='}

response = requests.get(url, params=params)

from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote

xml_obj = bs4.BeautifulSoup(response.text,'lxml-xml')
rows = xml_obj.findAll('item')

row_list = [] 
name_list = [] 
value_list = []

# xml 안의 데이터 수집
for i in range(0, len(rows)):
    columns = rows[i].find_all()
    for j in range(0,len(columns)):
        if i ==0:
            name_list.append(columns[j].name)
        value_list.append(columns[j].text)
    row_list.append(value_list)
    value_list=[]

#xml값 DataFrame으로 만들기
electric_df = pd.DataFrame(row_list, columns=name_list)

#DataFrame CSV 파일로 저장
electric_df.to_csv('D:\dthcsm\\task\electric_station_info.csv', encoding='utf-8-sig')
print("save done!")

