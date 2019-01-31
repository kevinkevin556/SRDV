import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in the data
iris = pd.read_csv('../../../data/iris.csv')
quantitatives = iris[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]

# draw boxplot
fig, ax = plt.subplots(figsize=(12, 7))
result = ax.boxplot(x = quantitatives.values,
                    labels = quantitatives.columns,
                    notch = False)
ax.set_title("Boxplots of Iris' characteristics")
plt.show()

# draw violin plot
fig, ax = plt.subplots(figsize=(12, 7))
result = ax.violinplot(dataset = quantitatives.values,
                       showmeans = False,
                       showmedians = True,
                       showextrema = True)

def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)

set_axis_style(ax, quantitatives.columns)
ax.set_title("Violin Plot of Iris' characteristics")
plt.show()