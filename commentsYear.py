import matplotlib.pyplot as plt

left = [0, 10, 20, 30, 40]
{"2018": 689659, "2019": 329763, "2020": 92918, "2021": 1338367, "2022": 560843}
# heights of bars
height = [689659, 329763, 92918, 1338367, 560843]
  
# labels for bars
tick_label = ['2018', '2019', '2020', '2021', '2022']
  
plt.rcParams.update({'font.size': 18})

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 3, color = ['green', 'green', 'green', 'red', 'green'])

plt.ticklabel_format(style="plain", axis="y")

# naming the x-axis
plt.xlabel('Years')
# naming the y-axis
plt.ylabel('Comments')
# plt.title('Comments/Years chart')
  
plt.show()