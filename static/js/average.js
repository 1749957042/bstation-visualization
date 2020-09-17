// 视频平均值信息柱形图
var average = echarts.init(document.getElementById('left2'))

var average_option = {
    title: {
		text: "视频平均信息",
		textStyle: {
			// color: 'white',
		},
		left: 'left',
    },
    color: ['#3398DB'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    xAxis: {
        type: 'category',
        data: ['弹幕数','评论数', '收藏数', '投币数', '转发量', '点赞数']
        // data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        // 视频均值信息数据
        data: [],
        type: 'bar'
    }]
};

average.setOption(average_option);