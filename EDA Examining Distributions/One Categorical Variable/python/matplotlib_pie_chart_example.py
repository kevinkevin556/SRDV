# Pie Chart and Bar Plot: Using matplotlib.pyplot

import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

# read in the data
iris = pd.read_csv('../../../data/iris.csv')
iris_class = list(set(iris['Class']))
count = lambda x: len([i for i, c in enumerate(iris['Class']) if c == x])
iris_count = [count(i) for i in iris_class]

# pie chart
fig, ax = plt.subplots(figsize=(12, 7))
wedges, texts, autotexts = ax.pie(x = iris_count,                           # how many sample from each category 
                                labels = iris_class,
                                colors = ('#F8766D', '#00BA38', '#619CFF'), # color for each wedge
                                explode = (0.01, 0.01, 0.01),               # the fraction of the radius with which to offset each wedge from center
                                autopct = '%.2f%%',                         # format string for printing out the value of each share
                                textprops = dict(color='w'),                # text properties: specifies the font color as white
                                shadow = False,                             # shadow
                                startangle = 30)                            # the degree to start, 0 as default 
ax.legend(wedges, iris_class,
        title = "Class of Iris",
        loc = 'center left',
        bbox_to_anchor = (0.8, 0, 0.5, 0.5))   
ax.axis('equal')                                                           # assign 'equal' for axis to keep the figure in circle
ax.set_title("Number of Samples for Each Iris Class in the Dataset")
plt.setp(autotexts, size=15, weight='bold')
plt.show()
