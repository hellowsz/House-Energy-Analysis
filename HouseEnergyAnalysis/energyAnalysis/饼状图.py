from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd
class pieAnalysis():
    def __init__(self):
        pass
    def pieShow(self):
        df = pd.read_csv('energySpider/homec(1).csv')
        #data = df
        print(df)
        lst = []

        xiwanji = df['洗碗机 [kW]'].sum()
        #xiwanji_sum = xiwanji.sum()['电量(kW)']
        xiwanji_list = ['洗碗机', int(xiwanji)]
        lst.append(xiwanji_list)


        luzi1 = df['炉子 1 [kW]'].sum()
        #print(luzi1)
        #luzi1_sum = luzi1[1].sum()['电量(kW)']
        luzi1_list = ['炉子 1', int(luzi1)]
        lst.append(luzi1_list)

        luzi2 = df['炉子 2 [kW]'].sum()
        #luzi2_sum = luzi2.sum()['电量(kW)']
        luzi2_list = ['炉子 2', int(luzi2)]
        lst.append(luzi2_list)

        bignxiang = df['冰箱 [kW]'].sum()
        #bignxiang_sum = bignxiang.sum()['电量(kW)']
        bignxiang_list = ['冰箱', int(bignxiang)]
        lst.append(bignxiang_list)

        weibolu = df['微波炉 [kW]'].sum()
        #weibolu_sum = weibolu.sum()['电量(kW)']
        weibolu_list = ['微波炉', int(weibolu)]
        lst.append(weibolu_list)
        pie = (
            Pie()
            .add(
            "",
            lst,
            radius='40%',
            center=["50%","60%"]
            )
            .set_colors(["#58B19F", "#9AECDB", "#61A0A8", "#D48265", "#D6A2E8"])
            .set_global_opts(
            title_opts=opts.TitleOpts(
            # pos_right="50%",
            title="家电耗能(kW)",
            title_textstyle_opts=(opts.TextStyleOpts(color='red'))
                ),

             )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            )
        return pie

#pie = pieAnalysis()
#pieShow().render('饼状图.html')