import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the data
iris = pd.read_csv('../../../data/iris.csv')
quantitatives = iris[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]

# draw boxplot
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 7))
ax = sns.boxplot(data = quantitatives)
ax.set_title("Boxplots of Iris' characteristics")
plt.show()