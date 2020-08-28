import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
class pictLine():
    def __init__(self):
        pass
    def drawLine(self):
        df = pd.read_csv('energySpider/homec(1).csv')
        df["时间"] = pd.to_datetime(df['时间'], unit='s')
        df_time = df["时间"].astype(str)
        df = df["房屋整体能耗 [kW]"]
        df = df.tail(15)
        df_time = df_time.tail(15)
        print(df_time)
        # 绘制折线图
        difference = df
        heming = df_time

        x_data = heming.values
        y_data = difference.values
        subdue = (
                Line()

                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="总能耗折线图", title_textstyle_opts=opts.TextStyleOpts(
                        color="black"

                    )),

                    legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="black")),
                    tooltip_opts=opts.TooltipOpts(is_show=False),
                    xaxis_opts=opts.AxisOpts(
                        type_="category",
                        axislabel_opts=opts.LabelOpts(rotate=30, color="black"),
                        axisline_opts=opts.AxisLineOpts(
                            linestyle_opts=opts.LineStyleOpts(
                                color="black"
                            )
                        )
                    ),
                    yaxis_opts=opts.AxisOpts(
                        type_="value",
                        axisline_opts=opts.AxisLineOpts(
                            linestyle_opts=opts.LineStyleOpts(
                                color="black"
                            )
                        ),
                        axislabel_opts=opts.LabelOpts(color="black"),
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    ),
                )
                    .add_xaxis(xaxis_data=x_data)
                    .add_yaxis(
                    series_name="能耗(kW)",
                    y_axis=y_data,
                    symbol="emptyCircle",
                    is_symbol_show=True,
                    label_opts=opts.LabelOpts(is_show=False),
                    color='#9AECDB',
                    symbol_size=5,
                    is_smooth=False,
                    is_hover_animation=True
                )
            )
        return subdue

