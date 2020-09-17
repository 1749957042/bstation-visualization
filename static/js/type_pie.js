// 视频类型环形图
let type_pie = echarts.init(document.getElementById("right2"))

let type_option = {
    // 图标题
    title: {
		text: "视频类型",
		left: 'right',
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        left: 10,
        data: []
    },
    series: [
        {
            name: '视频类型',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
                show: false,
                position: 'center'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '30',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: false
            },
            // 视频类型数据
            data: []
        }
    ]
};

type_pie.setOption(type_option)