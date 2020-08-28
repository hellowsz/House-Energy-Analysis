import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts


# class wind():
#     def fadain(self):
#         data = pd.read_csv('energySpider/homec(1).csv')
#         data[['风速','发电 [kW]']].plot(kind='scatter',x='风速',y='发电 [kW]')
#         line3 = Line()
#         line3.add_xaxis(data.风速.values)
#         line3.add_yaxis("能耗",data['发电 [kW]'].values)
#         line3.set_global_opts(title_opts=opts.TitleOpts(title="风速和发电的关系"))
#         line3.render("风力发电折线图.html")
class wind():
    def fadain(self):
        data = pd.read_csv('energySpider/homec(1).csv')
        data[['风速', '发电 [kW]']].plot(kind='scatter', x='风速', y='发电 [kW]')
        line3 = (
            Line()
                .add_xaxis(data.风速.values)
                .add_yaxis("能耗", data['发电 [kW]'].values)
                .set_global_opts(title_opts=opts.TitleOpts(title="风速和发电的关系"))
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .render("风力发电折线图.html")
        )
        return line3
