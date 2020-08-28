from pyecharts import options as opts
from pyecharts.charts import Bar3D
import pandas as pd
import numpy as np


def read_do():
    init_data = pd.read_csv('../energySpider/homec(1).csv')
    init_data = np.array(init_data)
    data_tip = ["使用总能耗 [kW]", "发电 [kW]", "洗碗机 [kW]", "炉子 1 [kW]", "房屋整体能耗 [kW]", "冰箱 [kW]", "酒窖 [kW]", "车库门 [kW]"]
    data_year = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    #year = init_data["时间"] = pd.to_datetime(init_data['时间'], unit='s')
    data_pre = []

    num = 0
    N = 0
    for st in data_tip:
        ofr = 0
        for dy in data_year:
            fuck = [st, dy, float(init_data[ofr][num])]
            data_pre.append(fuck)
            N = N + 1
            ofr = ofr + 1
        num = num + 1
    return data_pre


def bar3d_base() -> Bar3D:
    data = read_do()
    data_tip = ["使用总能耗 [kW]", "发电 [kW]", "洗碗机 [kW]", "炉子 1 [kW]", "房屋整体能耗 [kW]", "冰箱 [kW]", "酒窖 [kW]", "车库门 [kW]"]
    data_year = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,2015,2016,2017,2018,2019]

    c = (
        Bar3D()
            .add(
            "",
            data,
            xaxis3d_opts=opts.Axis3DOpts(data_tip, type_="category", max_=8),
            yaxis3d_opts=opts.Axis3DOpts(data_year, max_=2020),
            zaxis3d_opts=opts.Axis3DOpts(type_="value", max_=1),
            grid3d_opts=opts.Grid3DOpts(width="180", height="50")
        )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=1),
            title_opts=opts.TitleOpts(title="部分能耗图"),

        )
    )

    return c


abc = bar3d_base()
abc.render("部分能耗3d图3d.html")