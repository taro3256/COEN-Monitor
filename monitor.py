import sys
import time
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import chromedriver_binary
from bs4 import BeautifulSoup

args = sys.argv

APIKEY = '8fdbc6d901ead25d7b611bb14b473287'
ENDPOINT = 'https://api.chatwork.com/v2'
ROOMID = '190985342'

def sendChat(text):
    post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)
    headers = { 'X-ChatWorkToken': APIKEY }
    params = { 'body': text }
    resp = requests.post(post_message_url,
                     headers=headers,
                     params=params)
    print(resp.content)

sendChat("test")
 
options = Options()
# options.add_argument('--disable-gpu')              # headlessモードで暫定的に必要なフラグ(そのうち不要になる)
# options.add_argument('--disable-extensions')       # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
# options.add_argument('--proxy-server="direct://"') # Proxy経由ではなく直接接続する
# options.add_argument('--proxy-bypass-list=*')      # すべてのホスト名
# options.add_argument('--start-maximized')          # 起動時にウィンドウを最大化する
# options.add_argument('--headless')

# if len(args)>1:
#     try:
#         url = 'https://spatial.chat/s/' + args[1]
#         driver = webdriver.Chrome(options=options)
#         driver.implicitly_wait(10)
#         driver.get(url)
#         driver.find_element_by_class_name("name").send_keys("Monitor")
#         driver.find_element_by_class_name("pointer").click()
#         driver.implicitly_wait(10)
#         # time.sleep(5)
#         # print(BeautifulSoup(driver.page_source, "html.parser"))

#         while(True):
#             html = driver.page_source
#             soup = BeautifulSoup(html, "html.parser")
#             members = [m.text for m in soup.find_all(class_='member')]
#             time.sleep(2)
#             print(datetime.datetime.now(), members)

#         driver.quit()
#         exit()

#     except TimeoutException as e:
#         print(e)
#         driver.quit()
#         exit()

# else:
#     print("please roomname")
#     exit()
