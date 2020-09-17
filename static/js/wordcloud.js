// 弹幕词云图
var wordcloud = echarts.init(document.getElementById('cent'));

// 样本数据
var a = [{'name': '早', 'value': 3},
{'name': '热乎', 'value': 51},
{'name': '哈哈哈', 'value': 317},
{'name': '哈哈', 'value': 17}]

var wordcloud_option = {
						// title : {
						//     text : "弹幕词云图",
						//     textStyle : {
						//         color : 'white',
						//     },
						//     left : 'left'
						// },
                        tooltip: {
                            show: false
                        },
                        series: [{
                                type: 'wordCloud',
                                // drawOutOfBound:true,
                                // 单词之间间隙
                                gridSize: 5,
                                sizeRange: [12, 55],
                                // 词云图文字旋转角度范围
                                rotationRange: [-90, 90],
                                // 旋转步长
                                rotationStep: 90,    
                                textStyle: {
                                    normal: {
                                        // 词云图中的词随机颜色
                                        color: function () {
                                            return 'rgb(' +
                                                    Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) + ')'
                                        }
                                    }
                                },
                                right: null,
                                bottom: null,
                                // 弹幕列表数据
                                data: a
                            }]
                    }

wordcloud.setOption(wordcloud_option);
