import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the data
iris = pd.read_csv('../../../data/iris.csv')
quantitatives = iris[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]

# draw boxplot
# sns.set(style="whitegrid")
sns.set(style="ticks")
fig, ax = plt.subplots(figsize=(12, 7))
ax = sns.boxplot(data = quantitatives,      # Create boxplot
                palette="vlag")             # palette: Control the series of color        
ax = sns.swarmplot(data = quantitatives,    # Add points
                   color = ".4",            # color: one float number is for the grey level
                   size = 3.5 )             # size: the size for the marker
ax.set_title(label = "Boxplots of Iris' characteristics",
             fontsize = 24,
             fontweight = 'bold')
plt.show()