# B站可视化

#### 介绍
python爬虫，pythonweb，flask框架，B站数据可视化

#### 软件架构
python爬虫+flask+ajax+前端三大件+echarts


#### 数据来源

1.  其中视频信息的数据地址为：https://api.bilibili.com/x/web-interface/view?aid=， 

2.  视频弹幕的数据地址为：https://api.bilibili.com/x/v1/dm/list.so?oid=192968483，

3.  哔哩哔哩网站当前在线人数的数据地址为：https://api.bilibili.com/x/web-interface/online（现已经更改）

4.  案例通过爬虫的方式获取数据，[obtain.py](http://obtain.py/)文件是爬虫文件，里边的函数用来获取到实验需要的各种数据

    - get_header：构造请求头，返回构造的请求头

    - get_proxie：构造IP池，防止频繁访问IP被封

    - get_data(home,end)：获取视频信息

    - main(home,end)：调用get_data方法，返回获取到的所有视频数据

    - get_online：获取当前网站在线人数，返回在线人数

    - get_danmu：获取视频弹幕列表，以字符串的形式返回视频的全部弹幕

5.  为了方便直观的感受每一条数据，另外创建了一个save_[excel.py](http://excel.py/)文件

    - 此程序运行后会调用[obta.py](http://obta.py/)中的get_data方法，创递给其参数，爬取指定av号区间内的视频信息，通过第三方库openpyle库创建Excel工作薄，并将爬取到的数据存储在工作表中，列名为爬取到的视频属性信息。

#### 前端页面

1.  前端的框架支持用到的是HTML，网页的排版，包括布局布局方式等地方用到的技术是css，js作为脚本语言，需要做的是实现网页上的功能，接收数据等。

    - index.html是本次案例实现可视化的只要文件，展示是可视化的所有图表，test.css文件用来修改网页的样式和实现想要的布局方式。

2.  图表的构建采用echarts技术，主要的echarts文件如下

    - average.js：网页左下方的视频平均信息柱形图

    - max_min.js：网页右上方的视频信息极大极小值对比图

    - type_pie：网页右下方的视频类型比例饼图

    - wordcloud.js：网页中心的弹幕此云图

    - get_data.js：用来接受后端发过来的数据，传递给各个图表js文件

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
