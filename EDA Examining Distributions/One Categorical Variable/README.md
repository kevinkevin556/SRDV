# Visualiztion for One Categorical Variable Distribution <br> -- Pie Chart, Bar Plot and Pictograms
You can present the distribution of a categorical variable with **pie chart** or **bar plot**. Pictograms can be distorted sometimes.

### Python: Matplotlib.pyplot example 
```python
ax.pie(x = iris_count,                             # how many sample from each category 
       labels = iris_class,
       colors = ('#F8766D', '#00BA38', '#619CFF'), # color for each wedge
       explode = (0.01, 0.01, 0.01),               # the fraction of the radius with which to offset each wedge from center
       autopct = '%.2f%%',                         # format string for printing out the value of each share
       textprops = dict(color='w'),                # text properties: specifies the font color as white
       shadow = False,                             # shadow
       startangle = 30)                            # the degree to start, 0 as default 
```
![Image of Matplotlib Example](https://github.com/kevinkevin556/SRDV/blob/master/EDA%20Examining%20Distributions/One%20Categorical%20Variable/image/matplotlib_pie.png?raw=true)


### R: ggplot2 example
```r
# Create Pie Chart
pie <- ggplot(iris_class,
            aes(x = "",
            y = count,
            fill = label)) +
            geom_bar(stat='identity') +     # First create a stacked bar plot; stat='identity' is a must
            coord_polar("y")                # Then turn the plot into a circle by axis y
} 
```
![Image of ggplot2 Example](https://github.com/kevinkevin556/SRDV/blob/master/EDA%20Examining%20Distributions/One%20Categorical%20Variable/image/ggplot2_pie.png?raw=true)
