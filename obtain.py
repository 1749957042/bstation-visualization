#导入相关库
import requests as reqs 
import urllib
import json
import re
import random

# 构造请求头
def get_header(): 
    #请求头列表
    user_agent_list = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
    user_agent = random.choice(user_agent_list)  #随机获取请求头
    header = {
        'User-Agent':user_agent
    }
    return header

#设置代理IP，防止IP被封
def get_proxie():
    # IP池列表
    proxies = [
        '112.95.20.107:8888',
        '118.212.105.79:9999',
        '123.163.97.8:9999',
        '110.243.26.131:9999',
        '112.95.23.122:8888',
        '125.123.152.148:3000'
    ]
    proxie_handler = urllib.request.ProxyHandler({'http':random.choice(proxies)})   #设置随机获取的IP
    opener = urllib.request.build_opener(proxie_handler)    #构建opener对象，使用handler
    #获取请求头
    header = get_header() 
    head = []
    for key,value in header.items():
        elem = (key,value)
        head.append(elem)
    opener.addheaders = head
    return opener

all_data = []   #有效视频的所有列表
invalid_data = [] #失效视频信息，但是后续没有用到

# 获取视频所有信息并存储在all_data字典中
def get_data(home,end):
    invalid_count = 0   #失效视频数量
    invalid = []    #失效视频av号列表
    for av in range(home,end):
        opener = get_proxie()
        # 要爬取的视频信息链接
        video_text = opener.open("https://api.bilibili.com/x/web-interface/view?aid="+str(av)) 
        # 转码
        video_data = video_text.read().decode('utf-8')
        video_data = json.loads(video_data) #转换为字典形式

        #经过多次测试得到结果，当code=0时，视频正常；当code=-404时，视频不存在。
        #为了保证数据的有效性，当code！=0时，表示此视频不存在或不可访问，这些情况的视频信息均跳过，不收集
        if video_data['code'] != 0:
            invalid_count += 1  #收集失效视频的数量
            invalid.append(av)
            continue

        # video_data内包含多种数据，实验所需要的主要数据在video_data['data']字典中
        # video_data['data']字典中包含owner字典和stat字典，分别记录作者信息和视频播放情况
        data = video_data['data']

        title = data['title']   #视频标题
        name = data['owner']['name']    #作者ID
        v_type = data['tname']  #视频分区
        bv = data['bvid']   #视频BV号
        view = data['stat']['view']     #播放量
        danmu = data['stat']['danmaku'] #弹幕数
        comment = data['stat']['reply'] #评论数
        collect = data['stat']['favorite']  #收藏数
        coin = data['stat']['coin'] #投币数
        share = data['stat']['share']   #转发量
        like = data['stat']['like']     #点赞数
        # 将有效视频的信息存储到all_data列表中
        all_data.append({"title":title,"name":name,"av":av,"bv":bv,"type":v_type,"view":view,"danmu":danmu,"comment":comment,"collect":collect,"coin":coin,"share":share,"like":like})
    # 封装所有视频的信息
    invalid_data.append({"count":invalid_count,"invalid_list":invalid})

# 调用函数，home与end分别为视频的起始av号和结束av号
def main(home,end):
    get_data(home,end)
    # 返回有效视频的信息列表
    return all_data

#获取当前在线人数
def get_online():
    opener = get_proxie()
    online_text = opener.open('https://api.bilibili.com/x/web-interface/online')
    online_data = json.loads(online_text.read().decode('utf-8'))
    online_number = online_data['data']['all_count']
    return online_number

# 获取弹幕数据
def get_danmu():
    headers = get_header()
    response = reqs.get("https://api.bilibili.com/x/v1/dm/list.so?oid=192968483", headers=headers)
    html_doc = response.content.decode('utf-8')
    format = re.compile("<d.*?>(.*?)</d>")
    DanMu = format.findall(html_doc)
    danmu = []
    # 将每条弹幕逐个存储在列表中
    for i in DanMu:
        danmu.append(i)
    # 返回弹幕列表
    return danmu


