from pyecharts.charts import  WordCloud
from pyecharts import options as opts
class wordStatistic():
    def __init__(self):
        pass
    def word(self):
        words = [
        ("时间", 100),
        ("发电", 180),
        ("洗碗机", 95),
        ("炉子", 120),
        ("冰箱", 479),
        ("压力", 310),
        ("使用总耗能", 380),
        ("家庭办公室", 165),
        ("温度", 250),
        ("车库门", 179),
        ("客厅", 265),
        ("风速", 242),
        ("房屋整体耗能", 212),
        ("使用总耗能", 327),
        ("酒窖", 221),
        ("厨房", 211),
        ("车库", 120),
        ("太阳能发电", 200),
        ("湿度", 134),
        ("能见度", 231),
        ("总结", 321),
        ("云量", 200),
        ("抗风", 198),
        ("表观温度", 132),
        ("沉淀强度", 211),
        ("沉淀概率", 108),
        ("结露点温度", 292),
        ("icon", 311)
    ]
        wordcloud = (
            WordCloud()
                .add("", words, word_size_range=[5, 80], shape='star')
                .set_global_opts(title_opts=opts.TitleOpts(title="参数词云图"))
         )
        return wordcloud
