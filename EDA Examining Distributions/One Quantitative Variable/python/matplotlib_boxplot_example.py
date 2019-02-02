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
ax.set_title(label = "Boxplots of Iris' characteristics",
             fontdict = {'fontsize': 24,
                         'fontweight': 'bold'})
plt.show()