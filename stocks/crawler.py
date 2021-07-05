import re

import requests
from bs4 import BeautifulSoup


class StockCrawler():
    def __init__(self):
        self.url = 'https://www.38.co.kr/html/fund/index.htm?o=k'

    def get_list(self):
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find("table", {'summary': "공모주 청약일정"})
        data = data.find_all('tr')[2:]

        result=[]
        for row in range(0, len(data)):
            detail_link = data[row].find('a')['href']

            data_list = data[row].text.replace("\xa0", "").replace("\t\t", '').split('\n')[1:-1]
            if len(data_list) < 6:
                continue
            name = data_list[0]
            schedule = data_list[1]
            try:
                fixed_price = int(data_list[2].replace(",", ""))
            except ValueError:
                fixed_price = 0
            hoped_price = data_list[3]
            compete_rate = data_list[4]
            underwriter = data_list[5]
            detail_link = detail_link
            ipoid = re.split("=|&l", detail_link)[2]
            # print(name, schedule, fixed_price, hoped_price, compete_rate, underwriter)
            from stocks.models import IPO
            ipo, updated = IPO.objects.update_or_create(
                name=name,
                ipo_id=ipoid,
                defaults={
                    "schedule": schedule,
                    "fixed_price": fixed_price,
                    "hoped_price": hoped_price,
                    "compete_rate": compete_rate,
                    "underwriter": underwriter,
                    "detail_link": detail_link,
                    "is_finished": False if fixed_price==0 else True,
                }
            )
            result.append(ipo)
        return result