import time
import telegram
from config.settings import BASE_DIR, get_secret
from stocks.crawler import StockCrawler

def job():
    bot = telegram.Bot(token=get_secret("my_token"))

    s = StockCrawler()
    result = s.get_list()

    bot.sendMessage(chat_id=get_secret("chat_id"), text=str(result))

    now = time.localtime()
    print("current_time=", str(now))
