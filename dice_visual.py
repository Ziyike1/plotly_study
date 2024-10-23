import plotly.express as px
from die import Die

#创建两个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#掷几次骰子并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll() + die_3.roll())

#分析结果
frequencies = []
max_results = die_1.sides + die_2.sides +die_3.sides
poss_value = range(1, max_results + 1)
for value in poss_value:
    frequencies.append(results.count(value))


# print(frequencies)

#对结果进行可视化
title = "Result of Rolling Three D6 1000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_value, y=frequencies,title=title,labels=labels)

#进一步定制图形
fig.update_layout(xaxis_dtick=1)

fig.show()