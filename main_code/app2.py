import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime

today = datetime.date.today()
current_date = today-datetime.timedelta(2)
html = urlopen("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%8C%80%ED%9D%A5%EC%A4%91+%EA%B8%89%EC%8B%9D")
bsObject = BeautifulSoup(html, "html.parser")

current_menu = None
whole_date_menus_in_div = bsObject.body.find_all('div', attrs={'class':'school_menu'})
#print(bsObject.body.find('div', attrs={'class':'school_menu'}))
two_date_menus_in_ul = []
for each_two_menu_in_ul in whole_date_menus_in_div:
    two_date_menus_in_ul.append(each_two_menu_in_ul.find('ul'))

def find_current_menu_in_two_menu(two_date_menu_in_ul):
    for each_menu in two_date_menu_in_ul.find_all('li', {'class':'menu_info'}):
        date = str(each_menu.find('strong'))
        pure_date = re.sub('<.+?>', '', date, 0).strip()
        date_element_list = pure_date.split(' ')
        month = date_element_list[0].rstrip('월')
        day = date_element_list[1].rstrip('일')
        int_month = int(month)
        int_day = int(day)
        date_obj = {
            "month":int_month,
            "day": int_day,
        }
        if current_date.month == date_obj['month']:
            if current_date.day == date_obj['day']:
                menus = each_menu.find_all('li')
                
                return menus
for each_two_date_menu_in_ul in two_date_menus_in_ul:
    menu = find_current_menu_in_two_menu(each_two_date_menu_in_ul)
    if  menu != None:
        current_menu = menu
if current_menu != None:
    print(current_menu)
else:
    print('오늘은 급식이 없어요')




        




    

    