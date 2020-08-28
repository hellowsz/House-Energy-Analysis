from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
class consume_Bar():
    def __init__(self):
        pass
    def Bar_show(self):
        data= pd.read_csv('energySpider/homec(1).csv')
        data['净耗能量 [kW]'] = -data['发电 [kW]'] + data['使用总能耗 [kW]']
        data["时间"] = pd.to_datetime(data['时间'], unit='s')
        print(data)
         # 净耗能随时间变化(柱状)

        bar =(
            Bar(init_opts=opts.InitOpts(width='1200px',height='800px'))
            .add_xaxis(data['时间'].tolist())
            .add_yaxis(data.columns[1],data['使用总能耗 [kW]'].tolist())
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return bar
