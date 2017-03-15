# -*-coding:utf8-*-

import requests
import json
import random
import pymysql
from multiprocessing.dummy import Pool as ThreadPool
import sys
import datetime
import time
from imp import reload

def datetime_to_timestamp_in_milliseconds(d):
    current_milli_time = lambda: int(round(time.time() * 1000))
    return current_milli_time()

reload(sys)

def LoadUserAgents(uafile):
    """
    uafile : string
        path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas
uas = LoadUserAgents("user_agents.txt")
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
proxies = {
'http':'http://140.240.81.16:8888',
'http':'http://185.107.80.44:3128',
'http':'http://203.198.193.3:808',
'http':'http://125.88.74.122:85',
'http':'http://125.88.74.122:84',
'http':'http://125.88.74.122:82',
'http':'http://125.88.74.122:83',
'http':'http://125.88.74.122:81',
'http':'http://123.57.184.70:8081'
}
time1 = time.time()
for m in range(1691,2000): #26 ,1000
    urls = []
    for i in range(m*100, (m+1)*100):
        url = 'http://space.bilibili.com/ajax/member/GetInfo?mid=' + str(i)
        urls.append(url)

    def getsource(url):
        payload = {
            '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
            'mid': url.replace('http://space.bilibili.com/ajax/member/GetInfo?mid=', '')
        }
        ua = random.choice(uas)
        head = {'User-Agent':ua,
            'Referer':'http://space.bilibili.com/'+str(random.randint(9000,10000))+'/'
        }
        
        jscontent = requests.session().post('http://space.bilibili.com/ajax/member/GetInfo', headers=head,  data=payload,proxies = proxies).text
        time2 = time.time()
        try:
            jsDict = json.loads(jscontent)
            print(jsDict)
            statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
            if statusJson == True:
                if 'data' in jsDict.keys():
                    jsData = jsDict['data']
                    mid = jsData['mid']
                    name = jsData['name']
                    sex = jsData['sex']
                    face = jsData['face']
                    coins = jsData['coins']
                    regtime = jsData['regtime'] if 'regtime' in jsData.keys() else 0
                    spacesta = jsData['spacesta']
                    birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'nobirthday'
                    place = jsData['place'] if 'place' in jsData.keys() else 'noplace'
                    description = jsData['description']
                    article = jsData['article']
                    fans = jsData['fans']
                    friend = jsData['friend']
                    attention = jsData['attention']
                    sign = jsData['sign']
                    attentions = jsData['attentions']
                    level = jsData['level_info']['current_level']
                    exp = jsData['level_info']['current_exp']

                    regtime_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(regtime))
                    print(regtime_format)
                    print("Succeed: " + mid + "\t" + str(time2 - time1))
                else:
                    print('no data now')
                try:
                    conn = pymysql.connect(host='localhost', user='root', passwd='1565', charset='utf8')
                    cur = conn.cursor()
                    # cur.execute('create database if not exists python')
                    conn.select_db('bilibili')
                    cur.execute('INSERT INTO bilibili_user_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                [mid, mid, name, sex, face, coins, regtime_format, spacesta, birthday, place, description,
                                 article, fans, friend, attention, sign, str(attentions), level, exp])
                except Exception:
                    print("Mysql Error")
            else:
                print("Error: " + url)
        except ValueError:
            print('decoding json has failed')

    pool = ThreadPool(1)
    try:
        results = pool.map(getsource, urls)
    except Exception:
        print('ConnectionError')
        pool.close()
        pool.join()
        time.sleep(10)
        pool = ThreadPool(1)
        results = pool.map(getsource, urls)

    time.sleep(5)

pool.close()
pool.join()
