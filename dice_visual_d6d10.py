import plotly.express as px
from die import Die

#创建D6, D10
die_1 = Die()
die_2 = Die(10)

#掷几次骰子并将结果储存在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_results = die_1.sides + die_2.sides
poss_value = range(1, max_results + 1)
for value in poss_value:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

#对结果进行可视化
title = "Result of Rolling One D6 and One D10 1000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_value, y=frequencies,title=title,labels=labels)

#进一步定制图形
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html('dice_visual_d6d.html')