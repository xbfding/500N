# python3
from time import sleep

import requests
from bs4 import BeautifulSoup
import re

# 设置初始页面 URL 和匹配的正则表达式
page = 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Cookie': 'is_tips_version=1; JSESSIONID=CDF7DA02C58A08B4897EC97D2E227363; LAST_LOGINING_USERNAME=wq_18226253613; LS=wq_18226253613'
}
rtgxt = 'waiqicha|beian'

def reBool(str):
    a = re.search(rtgxt, str)
    if a is None:
        return True
    else:
        return False

def write_file(str):
    pwd = '500N_Doman_out.txt'
    with open(pwd, 'a') as file:
        file.write(str + '\n')

# 循环访问页面
while True:
    url = f'https://www.waiqicha.com/fhs?curPageNO={page}&country_id='
    # 获取页面内容
    sleep(10)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取页面中每个标题的超链接
    links = soup.find_all('a', {'class': 'item'})

    # 循环访问每个链接，并提取域名信息
    for link in links:
        sleep(10)
        href = link.get('href')
        response = requests.get(href, headers=headers)

        soupDm = BeautifulSoup(response.text, 'html.parser')
        lines = soupDm.find_all('a', {'target': '_blank', 'rel': 'nofollow'})
        for line in lines:
            doman = line.get('href')
            if reBool(doman):
                write_file(doman)
                print(f'{doman}')


    # 配置页面请求
    page += 1
    print(f'当前第{page}页')
    if page > 24:
        print(f'爬取完成,共{page}页')
        break
