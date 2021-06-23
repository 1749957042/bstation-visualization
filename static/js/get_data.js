// 获取当前在线人数
function get_online() {
    $.ajax({
        url:"/online",
        success:function(data) {
            $(".online p").text(data)
        },
        error:function(xhr, type, errorThrown){

        }
    })
}

// 获取均值数据
function get_all_data() {
    $.ajax({
		url: "/all_data",
		success: function(data) {
            data = JSON.parse(data)
            average_option.series[0].data = data.data
            average.setOption(average_option)
		},
		error: function(xhr, type, errorThrown) {
		}
	})
}

// 获取极值
function get_extreme() {
    $.ajax(
        {
            url:'/max_min',
            success: function(data) {
                data = JSON.parse(data)
                option.series[0].data = data.max
                option.series[1].data = data.min
                max_min.setOption(option)
            },
            error: function(xhr, type, errorThrown) {

            }
        }
    )
}

// 获取视频类型数据
function get_type() {
    $.ajax(
        {
            url:'/get_type',
            success: function(data) {
                data = JSON.parse(data)
                // for(i = 0;i < data.type.lenght;i++) {
                //     type_option.series[0].data[i].value = data.count[i]
                //     type_option.series[0].data[i].name = data.type[i]
                // }
                type_option.legend.data = data[1]
                type_option.series[0].data = data[0]
                type_pie.setOption(type_option)
            },
            error: function(xhr, type, errorThrown) {

            }
        }
    )
}

// 弹幕词云图数据
function get_danmu() {
    $.ajax(
        {
            url:'/get_danmu',
            success: function(data) {
                data = JSON.parse(data)
                wordcloud_option.series[0].data = data
                wordcloud.setOption(wordcloud_option)
            },
            error: function(xhr, type, errorThrown) {

            }
        }
    )
}

get_all_data()
get_online()
get_extreme()
get_type()
get_danmu()
// 没个1s中动态刷新一次网站当前在线人数
setInterval(get_online,1000)