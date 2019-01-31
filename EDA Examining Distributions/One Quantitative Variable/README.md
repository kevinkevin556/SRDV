# One Quantative Variable Distribution

## Measure of Center
- The three main numerical measures for the center of a distribution are the **mode**, **mean**, and the **median**. 
    - The mode is the most frequently occurring value. 
    - The mean is the average value,
    - The median is the middle value.
- **The mean is very sensitive to outliers** (as it factors in their magnitude), while *the median is resistant to outliers*.
- The **mean** is an appropriate measure of center only for **symmetric distributions with no outliers**. 
- **In all other cases, the median** should be used to describe the center of the distribution.

## Measure of Spread
- Range
    - Quantifies the variability by looking at the range covered by *ALL* the data
    - Range = Max - min
- Inter-Quartile Range (IQR)
    - Measures the variability of a distribution by giving us the range covered by the *MIDDLE 50%* of the data.
    - IQR = Q3 - Q1 
    <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    = (Median of [median, Max]) - (Median of [min, median])
    - The IQR should be used as a measure of spread of a distribution only when the median is used as a measure of center.


## Outliers
- **Detection**
    - below Q1 - 1.5(IQR)
    - above Q3 + 1.5(IQR)
- **Three kinds of Outliers**
    - Even though it is an extreme value, if an outlier
        - can be understood to have been produced by **essentially the same sort of physical or biological process** as the rest of the data,
        -  and if such extreme values are **expected to eventually occur again**,
        -  then such an outlier indicates something important and interesting about the process you're investigating, and it **should be kept** in the data.
    - If an outlier
        -  can be explained to have been produced under **fundamentally different conditions** from the rest of the data 
        - (or by a **fundamentally different process**),
        -  such an outlier can be **removed** from the data if your goal is to investigate only the process that produced the rest of the data.
    - An outlier might indicate a **mistake** in the data (like a typo, or a measuring error),
        - it **should be corrected if possible or else removed from the data before calculating** summary statistics or making inferences from the data (and the reason for the mistake should be investigated).


## Side-by-side boxplot
Note that this example provides more intuition about variability by interpreting small variability as consistency, and large variability as lack of consistency. Also, through this example we learned that the center of the distribution is more meaningful as a typical value for the distribution when there is little variability (or, as statisticians say, little "noise") around it. When there is large variability, the center loses its practical meaning as a typical value.

### ［Boxplot］ Python: Matplotlib.pyplot 
```python
fig, ax = plt.subplots(figsize=(12, 7))
result = ax.boxplot(x = quantitatives.values,
                    labels = quantitatives.columns,
                    notch = False)
ax.set_title("Boxplots of Iris' characteristics")
plt.show()
```
![Image of Matplotlib Boxplot Example](https://github.com/kevinkevin556/SRDV/blob/master/EDA%20Examining%20Distributions/One%20Quantitative%20Variable/image/matplotlib_boxplot.png?raw=true)

### ［Boxplot］ Python: Seaborn
```python
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 7))
ax = sns.boxplot(data = quantitatives)
ax.set_title("Boxplots of Iris' characteristics")
plt.show()
```
![Image of Seaborn Boxplot Example](https://github.com/kevinkevin556/SRDV/blob/master/EDA%20Examining%20Distributions/One%20Quantitative%20Variable/image/seaborn_boxplot.png?raw=true)
