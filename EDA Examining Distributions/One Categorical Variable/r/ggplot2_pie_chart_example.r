if(!require(ggplot2)){
    install.packages("ggplot2")
    library(ggplot2)
}

iris <- read.csv("../../../data/iris.csv", fileEncoding='UTF-8-BOM')
iris_class <- as.data.frame(table(iris$Class))
names(iris_class) <- c('label', 'count')

# Create Pie Chart
pie <- ggplot(iris_class,
            aes(x = "",
            y = count,
            fill = label)) +
            geom_bar(stat='identity') +     # First create a stacked bar plot; stat='identity' is a must
            coord_polar("y")                # Then turn the plot into a circle by axis y

# Anotate the share Ratio
count <- iris_class$count
share <- count / sum(count) * 100
for(i in 1:nrow(iris_class)){
    pie <- pie + annotate("text",
                        x = 1,                                  # x is now the distance from the original point                
                        y = cumsum(count)[i]-0.5*count[i],      # y is now the angle coordinate
                        label = sprintf("%.2f%%", share[i]), 
                        colour = "white",
                        fontface= "bold") 
} 

# Set labels
pie <- pie + 
    labs(fill = "Class if Iris") +  # Rename the legend label
    labs(x = NULL) +                # Remove x-axis label
    labs(y = NULL)                  # Remove y-axis label

# Set Title
pie <- pie + 
    ggtitle("Number of Samples for Each Iris Class in the Dataset") +
    theme(plot.title = element_text(face="bold", hjust=0.5))

# Show the Figure
pie

   

