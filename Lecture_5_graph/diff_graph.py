'''Plot, using histograms, the distribution of plastic waste per capita faceted by continent. What can you say about how the continents compare to each other in terms of their plastic waste per capita?
Convert your side-by-side box plots from the previous task to violin plots. What do the violin plots reveal that box plots do not? What features are apparent in the box plots but not in the violin plots?
Visualize the relationship between plastic waste per capita and mismanaged plastic waste per capita using a scatterplot. Describe the relationship.
Colour the points in the scatterplot by continent. Does there seem to be any clear distinctions between continents with respect to how plastic waste per capita and mismanaged plastic waste per capita are associated?
Visualize the relationship between plastic waste per capita and total population as well as plastic waste per capita and coastal population. You will need to make two separate plots. Do either of these pairs of variables appear to be more strongly linearly associated?
'''

import pandas as pd
from lets_plot import *

LetsPlot.setup_html()

#dataset = pd.read_csv("https://raw.githubusercontent.com/tidyverse/datascience-box/refs/heads/main/course-materials/lab-instructions/lab-02/data/plastic-waste.csv")

#print(dataset.info())
#print(dataset.head())

#dataset.to_csv ("plastic-waste.csv", 
#				index = None, 
#				header=True) 
	
#read nobel.csv
#df = pd.DataFrame(pd.read_csv("plastic-waste.csv")) 
#print(df)

df = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_5_graph/plastic-waste.csv')

#Plot, using histograms, the distribution of plastic waste per capita faceted by continent. What can you say about how the continents compare to each other in terms of their plastic waste per capita?
df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')
df.dropna(subset=['plastic_waste_per_cap'], inplace=True)

ggplot(df, aes(x='plastic_waste_per_cap')) + \
    geom_histogram(binwidth=0.05, fill='blue', color='black', alpha=0.7) + \
    facet_wrap('continent', scales='free_y') + \
    labs(x='Plastic Waste per Capita (kg)', y='Frequency', title='Distribution of Plastic Waste per Capita by Continent') + \
    theme_minimal()

#Convert your side-by-side box plots from the previous task to violin plots. What do the violin plots reveal that box plots do not? What features are apparent in the box plots but not in the violin plots?
df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')
df.dropna(subset=['plastic_waste_per_cap'], inplace=True)

ggplot(df, aes(x='continent', y='plastic_waste_per_cap')) + \
    geom_violin(trim=False, fill='lightblue', color='black') + \
    facet_wrap('continent', scales='free_y') + \
    labs(x='Continent', y='Plastic Waste per Capita (kg)', title='Distribution of Plastic Waste per Capita by Continent') + \
    theme_minimal()

#Visualize the relationship between plastic waste per capita and mismanaged plastic waste per capita using a scatterplot. Describe the relationship.
df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')
df['mismanaged_plastic_waste_per_cap'] = pd.to_numeric(df['mismanaged_plastic_waste_per_cap'], errors='coerce')
df.dropna(subset=['plastic_waste_per_cap', 'mismanaged_plastic_waste_per_cap'], inplace=True)

ggplot(df, aes(x='plastic_waste_per_cap', y='mismanaged_plastic_waste_per_cap')) + \
    geom_point(alpha=0.7, color='blue') + \
    labs(x='Plastic Waste per Capita (kg)', y='Mismanaged Plastic Waste per Capita (kg)', title='Relationship between Plastic Waste and Mismanaged Plastic Waste per Capita') + \
    theme_minimal()


#Colour the points in the scatterplot by continent. Does there seem to be any clear distinctions between continents with respect to how plastic waste per capita and mismanaged plastic waste per capita are associated?
df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')
df['mismanaged_plastic_waste_per_cap'] = pd.to_numeric(df['mismanaged_plastic_waste_per_cap'], errors='coerce')
df.dropna(subset=['plastic_waste_per_cap', 'mismanaged_plastic_waste_per_cap'], inplace=True)

ggplot(df, aes(x='plastic_waste_per_cap', y='mismanaged_plastic_waste_per_cap', color='continent')) + \
    geom_point(alpha=0.7) + \
    labs(x='Plastic Waste per Capita (kg)', y='Mismanaged Plastic Waste per Capita (kg)', title='Relationship between Plastic Waste and Mismanaged Plastic Waste per Capita by Continent') + \
    theme_minimal() + \
    scale_color_discrete(name='Continent') + \
    guides(color=guide_legend(title='Continent'))

#Visualize the relationship between plastic waste per capita and total population as well as plastic waste per capita and coastal population. You will need to make two separate plots. Do either of these pairs of variables appear to be more strongly linearly associated?
df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')
df['total_pop'] = pd.to_numeric(df['total_pop'], errors='coerce')
df['coastal_pop'] = pd.to_numeric(df['coastal_pop'], errors='coerce')
df.dropna(subset=['plastic_waste_per_cap', 'total_pop', 'coastal_pop'], inplace=True)

ggplot(df, aes(x='coastal_pop', y='plastic_waste_per_cap')) + \
    geom_point(alpha=0.7) + \
    labs(x='Coastal Population', y='Plastic Waste per Capita (kg)', title='Relationship between Plastic Waste per Capita and Coastal Population') + \
    theme_minimal()


#Recreate the following plot, and interpret what you see in context of the data.

df['plastic_waste_per_cap'] = pd.to_numeric(df['plastic_waste_per_cap'], errors='coerce')
df['total_pop'] = pd.to_numeric(df['total_pop'], errors='coerce')
df['coastal_pop'] = pd.to_numeric(df['coastal_pop'], errors='coerce')
df.dropna(subset=['plastic_waste_per_cap', 'total_pop', 'coastal_pop'], inplace=True)

# Calculate coastal population proportion
df['coastal_pop_prop'] = df['coastal_pop'] / df['total_pop']

p = ggplot(df, aes(x='coastal_pop_prop', y='plastic_waste_per_cap', color='continent')) + \
    geom_point(alpha=0.7) + \
    geom_smooth(method='loess', se=True, color='black') + \
    labs(x='Coastal population proportion (Coastal / total population)', y='Plastic waste per capita', title='Plastic waste vs. coastal population proportion by continent') + \
    theme_minimal() + \
    scale_color_discrete(name='Continent')