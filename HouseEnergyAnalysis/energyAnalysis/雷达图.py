from pyecharts import options as opts
from pyecharts.charts import Radar
import pandas as pd
class Radar_draw():
    def __init__(self):
        pass
    def drawRadar(self):
        df = pd.read_csv('energySpider/homec(1).csv')
        df_luzi1 = df.loc[0, "炉子 1 [kW]"]
        df_luzi2 = df.loc[0, "炉子 2 [kW]"]
        df_jiatingbangongshi = df.loc[0, "家庭办公室 [kW]"]
        df_bingxiang = df.loc[0, "冰箱 [kW]"]
        df_jiujiao = df.loc[0, "酒窖 [kW]"]
        df_chekumen = df.loc[0, "车库门 [kW]"]
        v1 = [[df_luzi1, df_luzi2, df_jiujiao, df_bingxiang, df_jiatingbangongshi, df_chekumen]]
        v2 = [[8.1, 120000, 16000, 7000, 15000, 7000]]



        radar = (
            Radar()
                    # 设置边属性
                .add_schema(
                schema=[
                    opts.RadarIndicatorItem(name='炉子 1', max_=0.45),
                    opts.RadarIndicatorItem(name='炉子 2', max_=0.45),
                    opts.RadarIndicatorItem(name='酒窖', max_=0.45),
                    opts.RadarIndicatorItem(name='冰箱', max_=0.45),
                    opts.RadarIndicatorItem(name='家庭办公室', max_=0.45),
                    opts.RadarIndicatorItem(name='车库门', max_=0.45),
                    ]
                )
                .add(
                '能耗', v1,
                color='green',
                    # 通过颜色属性  将其填充
                areastyle_opts=opts.AreaStyleOpts(
                    opacity=0.5,  # 透明度设置
                    color='green'
                ), )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    # 全局的属性设置 不要一个一个的写出
                .set_global_opts(title_opts=opts.TitleOpts(title='家电能耗对比'))
            )
        return radar


            #radar_base().render('雷达图显示.html')