import matplotlib.pyplot as plt

# x-coordinates of left sides of bars 
left = [0, 10, 20, 30, 40]
  
# heights of bars
height = [29738, 12885, 31858, 129693, 56838]
  
# labels for bars
tick_label = ['2018', '2019', '2020', '2021', '2022']

plt.rcParams.update({'font.size': 18})
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 3, color = ['green', 'green', 'green', 'red', 'green'])
  
# naming the x-axis
plt.xlabel('Years')
# naming the y-axis
plt.ylabel('Submissions')
# plt.title('Submissions/Years chart')
  
# function to show the plot
plt.show()