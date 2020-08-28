from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
data= pd.read_csv('../energySpider/homec(1).csv')
bar = (
    Bar()  # InitOpts:初始化主题
    # add_xaxis：加入x轴参数  stack——实现数据堆叠,同个类目轴上系列配置相同的stack值可以堆叠放置
    .add_xaxis(data['使用总能耗 [kW]'].tolist())
    .add_yaxis("房屋", data["房屋整体能耗 [kW]"].tolist(), stack="stack1")
    .add_yaxis("地窖", data["酒窖 [kW]"].tolist(), stack="stack1")
    .add_yaxis("水井", data["水井 [kW]"].tolist(), stack="stack1")
    .set_global_opts(title_opts=opts.TitleOpts(title="房屋，地窖，水井耗能"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render("堆叠柱形图.html")
)