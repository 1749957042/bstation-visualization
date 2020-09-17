// 视频极大极小值折线图
let max_min = echarts.init(document.getElementById('r1'))

let option = {
    title: {
        text: '最值对比图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['最大值', '最小值'],
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        // 横轴x轴
        type: 'category',
        boundaryGap: false,
        data: ['播放', '弹幕', '评论', '收藏', '硬币', '转发', '点赞']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '最大值',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '最小值',
            type: 'line',
            stack: '总量',
            // 视频极值数据
            data: []
        }
    ]
};


max_min.setOption(option);