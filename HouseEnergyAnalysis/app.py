from flask import Flask,render_template

app = Flask(__name__)
# from waterAnaylysis.流域储水量饼状图 import pieAnalysis
# from waterAnaylysis.topflood_scatter import flood_scatter
# from waterAnaylysis.省份站点数量 import flood_Bar
# from waterAnaylysis.坝顶高程与水位之差 import flood_subdue
from energyAnalysis.词云图 import wordStatistic
from energyAnalysis.饼状图 import pieAnalysis
from energyAnalysis.发电量阶梯散点图 import powerAnalysis
from energyAnalysis.柱状图 import consume_Bar
from energyAnalysis.折线图 import pictLine
from energyAnalysis.雷达图 import Radar_draw
from energyAnalysis.风力发电折线图 import wind
@app.route('/')
def index():
    return render_template('welcome.html')
@app.route('/manage/')
def manage():
    # 实例化对象
    pie = pieAnalysis().pieShow()
    scatter = powerAnalysis().power_scatter()
    # pie = pieAnalysis().pieShow()
    bar = consume_Bar().Bar_show()
    line = pictLine().drawLine()
    wordcloud = wordStatistic().word()
    return render_template(
        "one.html",
        # 数据对应的json格式  进行转型格式  json
        bar_pie=pie.dump_options(),
        # bar_pie=pie.dump_options(),
        bar_scatter=scatter.dump_options(),
        bar_bar=bar.dump_options(),
        bar_line=line.dump_options(),
        bar_word=wordcloud.dump_options()
    )

@app.route('/get_bar')
def get_bar():
    return render_template('show/雷达图显示.html')

@app.route('/get_line')
def get_line():
    return render_template('show/风力发电折线图.html')

@app.route('/get3d')
def get3d():
    return render_template('show/部分能耗3d图3d.html')
# @app.route('/getreli_num')
# def getreli_num():
#     return render_template('others/各省不同汛情的站点数量图.html')

@app.route('/two/')
def two():
    radar = Radar_draw().drawRadar()
    line3 = wind().fadain()
    return render_template(
        "two.html",
        bar_radar=radar.dump_options(),
        bar_line3=line3.dump_options()
    )

@app.route('/three')
def three():
     return render_template('three.html')

# @app.route('/aboutus/')
# def aboutus():
#     return render_template('aboutUs.html')

if __name__ == '__main__':
    app.run()

