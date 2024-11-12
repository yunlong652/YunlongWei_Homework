'''Plot, using histograms, the distribution of plastic waste per capita faceted by continent. What can you say about how the continents compare to each other in terms of their plastic waste per capita?
Convert your side-by-side box plots from the previous task to violin plots. What do the violin plots reveal that box plots do not? What features are apparent in the box plots but not in the violin plots?
Visualize the relationship between plastic waste per capita and mismanaged plastic waste per capita using a scatterplot. Describe the relationship.
Colour the points in the scatterplot by continent. Does there seem to be any clear distinctions between continents with respect to how plastic waste per capita and mismanaged plastic waste per capita are associated?
Visualize the relationship between plastic waste per capita and total population as well as plastic waste per capita and coastal population. You will need to make two separate plots. Do either of these pairs of variables appear to be more strongly linearly associated?
'''

import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np
from lets_plot import *

dataset = pd.read_csv("https://raw.githubusercontent.com/tidyverse/datascience-box/refs/heads/main/course-materials/lab-instructions/lab-02/data/plastic-waste.csv")

#print(dataset.info())
#print(dataset.head())

dataset.to_csv ("plastic-waste.csv", 
				index = None, 
				header=True) 
	
#read nobel.csv
df = pd.DataFrame(pd.read_csv("plastic-waste.csv")) 
#print(df)

#Plot, using histograms, the distribution of plastic waste per capita faceted by continent. What can you say about how the continents compare to each other in terms of their plastic waste per capita?
# Data cleaning: remove rows with missing 'plastic_waste_per_cap'
df = df.dropna(subset=['plastic_waste_per_cap'])

# Convert 'plastic_waste_per_cap' to numeric in case it's not
df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')

# Ensure 'continent' is treated as a categorical variable
df['continent'] = df['continent'].astype('category')

# Create the plot
p = (ggplot(df, aes(x='plastic_waste_per_cap')) +
     geom_histogram(binwidth=0.05, fill='blue', color='black', alpha=0.7) +
     facet_wrap('~continent') +
     labs(x='Plastic Waste per Capita (kg)', y='Number of Countries', title='Distribution of Plastic Waste per Capita by Continent') +
     theme_minimal())

# Show the plot
print(p)