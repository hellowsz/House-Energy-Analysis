from pyecharts import options as opts
import pandas as pd
from pyecharts.charts import *
class powerAnalysis():
    def __init__(self):
        pass
    def power_scatter(self):
        data = pd.read_csv('energySpider/homec(1).csv')
        scatter = (
            Scatter(init_opts=opts.InitOpts(theme='dark'))
            .add_xaxis(data['发电 [kW]'])
            .add_yaxis('时间',data['时间'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max',name='最大值')])
                             )
            .set_global_opts(
                legend_opts=opts.LegendOpts(is_show=False),
                title_opts=opts.TitleOpts(title='发电量-时间 散点图'),
                xaxis_opts=opts.AxisOpts(
                    name='发电',
                    type_='value',
                #     去除分割线
                    splitline_opts=opts.SplitLineOpts(is_show=False)
                ),
                yaxis_opts=opts.AxisOpts(
                    name='时间',
                    name_location='middle',
                    is_scale=True,
                    splitline_opts=opts.SplitLineOpts(is_show=False),

                ),
                visualmap_opts=opts.VisualMapOpts(is_show=True,type_='color',min_=100,max_=10000)
            )
        )
        return scatter
#scatter.render('发电量散点图.html')