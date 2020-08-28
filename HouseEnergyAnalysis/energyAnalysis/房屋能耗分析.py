import pandas as pd
import random


data = pd.read_csv('../energySpider/homec.csv',encoding='gbk')
#print(data)

# 去除空值
data = data.dropna()
print(data)

# # 查看列名
print(data.columns)
# # 使用耗能随时间的变化
data[['时间','使用总能耗 [kW]']].plot()

# # 发电量随时间的变化

data[['时间','发电 [kW]']].plot()

data['净耗能量 [kW]'] = -data['发电 [kW]'] + data['使用总能耗 [kW]']
print(data)


 # 净耗能随时间变化

data[['时间','净耗能量 [kW]']].plot()
first_usage = pd.DataFrame(data.iloc[0]).iloc[4:18].to_dict()[0]
print(first_usage)

#-*- coding: utf-8 -*-
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码


# # 开始时耗能占比
labels = []
usage = []
for use in first_usage:
    labels.append(use)
    usage.append(first_usage[use]/3.3299999999999996e-05)
plt.pie(usage,labels=labels,autopct='%3.1f%%')
plt.axis('equal')
plt.show()

last_usage = pd.DataFrame(data.iloc[-1]).iloc[4:18].to_dict()[503909]
print(last_usage)


# # 结束时耗能占比

labels = []
usage = []
for use in last_usage:
    labels.append(use)
    usage.append(last_usage[use]/5e-05)
plt.pie(usage,labels=labels,autopct='%3.1f%%')
plt.axis('equal')
plt.show()


# # 风速和发电的关系


data[['风速','发电 [kW]']].plot(kind='scatter', x='风速', y='发电 [kW]')


# # 风速和发电功率的协方差

data['风速'].corr(data['发电 [kW]'])


# # 天气状况统计

from collections import Counter
counter = Counter(data['总结'])
labels = []
usage = []
for use in counter:
    labels.append(use)
    usage.append(counter[use])
plt.pie(usage,labels=labels,autopct='%3.1f%%')
plt.axis('equal')
plt.show()

status = pd.DataFrame(usage,index=labels)
print(status)


# # 天气情况频率分布图
status.plot(kind='hist')





