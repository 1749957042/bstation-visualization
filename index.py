import flask
from flask import g
from flask import current_app   #当前flask实例，使用时激活
from jieba.analyse import extract_tags # 提取关键字
import string
import obtain   # 调用爬虫程序
import json
from collections import Counter

# 实例化flask对象
app = flask.Flask(__name__)

# 激活上下文
ctx = app.app_context()
ctx.push()

# 运行此文件时需要调用爬虫，所以启动会慢一点
# 设置临时变量g，存储视频播放信息，供全局使用
g = obtain.main(0,100)

# 可视化网页主页
@app.route('/')
def index():
    return flask.render_template("index.html")

# 当前网站在线人数
@app.route('/online')
def online_people():
    online_number = obtain.get_online()
    return json.dumps(online_number)

# 视频平均播放信息数据
@app.route('/all_data')
def get_all_data():
    # view = 0
    # 由于播放量与其他数据相差较大（👍★💰下次一定），在此删除播放量数据，在平均数据表中不再显示，
    danmu = comment = collect = coin = share = like = 0
    # data = obtain.main(625696911,625696912)
    data = g  
    ldata = len(data)
    for i in range(len(data)):
        # view += int(data[i]['view'])
        danmu += int(data[i]['danmu'])
        comment += int(data[i]['comment'])
        collect += int(data[i]['collect'])
        coin += int(data[i]['coin'])
        share += int(data[i]['share'])
        like += int(data[i]['like'])
    data = [danmu,comment,collect,coin,share,like]
    all_data = [int(c/(ldata)) for c in data]   #取平均值
    return json.dumps({"data":all_data})    #封装成json格式传递到前端

# 获取极值数据
@app.route('/max_min')
def get_extreme():
    view,danmu,comment,collect,coin,share,like = [],[],[],[],[],[],[]
    # 将临时变量中g存储的视频数据赋值给data
    data = g
    # 遍历视频全部信息列表，将每项数据存储在列表中
    for i in range(len(data)):
        view.append(data[i]["view"])    # 播放量
        danmu.append(data[i]['danmu'])  # 弹幕数
        comment.append(data[i]['comment'])  # 评论量
        collect.append(data[i]['collect'])  # 收藏数
        coin.append(data[i]['coin'])    # 投币数
        share.append(data[i]['share'])  # 转发数
        like.append(data[i]['like'])    # 点赞数
    total = [view,danmu,comment,collect,coin,share,like]    # 各个属性列表封装在一个列表中
    max_total = [max(i) for i in total]     #取最大值
    min_total = [min(i) for i in total]     #取最小值
    return json.dumps({"max":max_total,"min":min_total})    # 封装成字典，以json格式传递

# 获取视频类型数据
@app.route('/get_type')
def get_type():
    type_list = []
    # 将临时变量中g存储的视频数据赋值给data
    data = g
    for i in data:
        type_list.append(i["type"])
    # 统计列表中每种类型出现的次数
    type_data = Counter(type_list)
    key,value = [],[]
    for a in type_data:
        key.append(a) #类型列表
        value.append(type_data[a]) #类型出现的次数列表
    total_data = []
    for i in range(len(key)):
        total_data.append({"value": value[i],"name": key[i]})
    return json.dumps([total_data,key])

ctx.pop()

# 获取某个视频中的全部弹幕
@app.route('/get_danmu')
def get_danmu():
    # 调用函数获取弹幕列表
    danmu_text = obtain.get_danmu()
    danmu_data = []
    for i in danmu_text:
        danmu_data.append(extract_tags(i))
    # 提取关键字后，每条弹幕可能提取出多条关键字，导致列表内有列表，遍历全部提取出来
    all_danmu = []
    for q in danmu_data:
        for w in q :
            all_danmu.append(w)
    # 分析相同字段出现的次数
    danmu_count = Counter(all_danmu)
    a,b = [],[]
    for i in danmu_count:
        a.append(i) #弹幕内容
        b.append(danmu_count[i]) #出现次数
    total_danmu = []
    for x in range(len(a)):
        total_danmu.append({"name":a[x],"value":b[x]})
    return json.dumps(total_danmu)  # 封装成json格式传给前端

if __name__ == '__main__':
    app.run()
