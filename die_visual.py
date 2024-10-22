import plotly.express as px
from die import Die

#创建一个D6
die = Die()

#掷几次骰子并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
poss_value = range(1, die.sides + 1)
for value in poss_value:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

#对结果进行可视化
fig = px.bar(x=poss_value, y=frequencies)
fig.show()