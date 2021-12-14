import re
from collections import defaultdict
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class StockCrawler():
    def __init__(self):
        self.url = 'https://www.38.co.kr/html/fund/index.htm?o=k'

    def get_list(self, created=True):
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find("table", {'summary': "공모주 청약일정"})
        data = data.find_all('tr')[2:]

        result = []
        date_now = datetime.now()
        now_year, now_month, now_date = date_now.year, date_now.month, date_now.day
        for row in range(0, len(data)):
            data_list = data[row].text.replace("\xa0", "").replace("\t\t", '').split('\n')[1:-1]
            if len(data_list) < 6:
                continue

            schedule = data_list[1].strip()

            start_str, end_str = schedule.split("~")[0], schedule.split("~")[1]
            start_year, start_month, start_date = map(int, (start_str[:4], start_str[5:7], start_str[8:10]))
            end_month, end_date = end_str.split(".")

            start_dt = datetime.strptime(str(start_year) + '-' + str(start_month) + '-' + str(start_date), '%Y-%m-%d')
            end_dt = datetime.strptime(str(start_year) + '-' + str(end_month) + '-' + str(end_date), '%Y-%m-%d')

            try:
                fixed_price = int(data_list[2].replace(",", ""))
            except ValueError:
                fixed_price = 0

            detail_link = data[row].find('a')['href']
            ipo = defaultdict(dict)
            ipo["ipo_id"] = re.split("=|&l", str(detail_link))[2]
            ipo["name"] = data_list[0].strip()
            ipo["schedule"] = schedule
            ipo["start_date"] = start_dt
            ipo["end_date"] = end_dt
            ipo["hoped_price"] = data_list[3].strip()
            ipo["fixed_price"] = fixed_price
            ipo["compete_rate"] = data_list[4].strip()
            ipo["underwriter"] = data_list[5].split(',')
            ipo["detail_link"] = detail_link
            ipo["is_finished"] = False
            result.append(ipo)
        return result


if __name__ == '__main__':
    from stocks.models import IPO

    s = StockCrawler()
    ipo_list = s.get_list()

    for ipo in ipo_list:
        obj, updated = IPO.objects.update_or_create(
            name=ipo['name'],
            ipo_id=ipo['ipo_id'],
            defaults={**ipo}
        )
        print(obj)
