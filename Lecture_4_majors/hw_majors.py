'''Which major has the lowest unemployment rate?
Which major has the highest percentage of women?
How do the distributions of median income compare across major categories?
Do women tend to choose majors with lower or higher earnings?'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

allages = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_4_majors/archive/all-ages.csv')
gardstu = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_4_majors/archive/grad-students.csv')
major_list = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_4_majors/archive/majors-list.csv')
recgards = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_4_majors/archive/recent-grads.csv')
womenstem = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_4_majors/archive/women-stem.csv')

#print(allages.info())
#print(gardstu.info())
#print(major_list.info())
#print(recgards.info())
#print(womenstem.info())

#Which major has the lowest unemployment rate
# Sort the data by the unemployment rate in ascending order
df_sorted = allages.sort_values(by='Unemployment_rate')

# Find the major with the lowest unemployment rate
lowest_unemployment_major = df_sorted.head(1)

# Print the result
print("Major with the lowest unemployment rate:")
print(lowest_unemployment_major[['Major', 'Unemployment_rate']])

print("----------------------------------------------------------------")

#Which major has the highest percentage of women
# Calculate the proportion of women for each major
womenstem['Proportion_of_Women'] = womenstem['Women'] / womenstem['Total']

# Sort the data in descending order with respect to the proportion of women
df_sorted = womenstem.sort_values(by='Proportion_of_Women', ascending=False)

# Display only the top 3 majors
top_3_women_majors = df_sorted.head(3)[['Major', 'Total', 'Proportion_of_Women']]

# Print the result
print("Top 3 majors with the highest percentage of women:")
print(top_3_women_majors)

print("----------------------------------------------------------------")

#How do the distributions of median income compare across major categories
'''The median is often chosen over the mean 
because it is less affected by outliers or extreme values in the data set. 
The mean can be skewed by very high or very low incomes, 
while the median represents the middle value, 
providing a more robust measure of central tendency for skewed distributions.'''


# Calculate bin edges
min_income = allages['Median'].min()
max_income = allages['Median'].max()
bin_edges = np.arange(min_income, max_income + 1000, 1000)  # Adjust the step size as needed

# Plot the histogram with specified bin edges
plt.figure(figsize=(12, 6))
plt.hist(allages['Median'], bins=bin_edges, edgecolor='black')
plt.title('Histogram of Median Income (Binwidth = $1000)')
plt.xlabel('Median Income')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of median income by major category with a bin width of $1000
sns.histplot(data=allages, x='Median', hue='Major_category', binwidth=1000, element='step', stat='count', common_norm=False)
plt.title('Distribution of Median Income by Major Category')
plt.xlabel('Median Income')
plt.ylabel('Frequency')
plt.show()

print("----------------------------------------------------------------")

#All STEM fields aren't the same
stem_categories = [
    'Engineering', 'Computers & Mathematics', 'Biology & Life Science', 
    'Physical Sciences', 'Agriculture & Natural Resources'
]

allages['Is_STEM'] = allages['Major_category'].apply(lambda x: x in stem_categories)

overall_median_income = allages['Median'].median()

stem_majors_below_median = allages[(allages['Is_STEM']) & (allages['Median'] <= overall_median_income)]

result = stem_majors_below_median[['Major', 'Median', 'P25th', 'P75th']].sort_values(by='Median', ascending=False)

print(result)

print("----------------------------------------------------------------")

#Do women tend to choose majors with lower or higher earnings?
# Define STEM categories
stem_categories = [
    'Engineering', 'Computers & Mathematics', 'Biology & Life Science', 
    'Physical Sciences', 'Agriculture & Natural Resources'
]

# Create a new column to indicate if the major is STEM
allages['Is_STEM'] = allages['Major_category'].apply(lambda x: 'Yes' if x in stem_categories else 'No')

# Calculate the proportion of women for each major
allages['Proportion_of_Women'] = allages['Employed'] / allages['Total']

# Create a scatterplot
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Median', y='Proportion_of_Women', hue='Is_STEM', style='Is_STEM', data=allages, palette='coolwarm', s=100)

# Add regression line if desired
sns.regplot(x='Median', y='Proportion_of_Women', scatter=False, data=allages, color='gray')

# Add titles and labels
plt.title('Median Income vs. Proportion of Women by STEM Field')
plt.xlabel('Median Income')
plt.ylabel('Proportion of Women')
plt.legend(title='Is Major STEM?', labels=['No', 'Yes'], loc='upper right', bbox_to_anchor=(1.05, 1), frameon=False)

# Show the plot
plt.show()

print("----------------------------------------------------------------")

# Further exploration
'''How does the choice of college major affect 
both the unemployment rate and median income of graduates, 
and is there a correlation between these two economic outcomes?'''

# Calculate average unemployment rate and median income for each major
major_summary = allages.groupby('Major').agg({
    'Unemployment_rate': 'mean',
    'Median': 'median'
}).reset_index()

# Scatter plot of median income vs. unemployment rate for each major
plt.figure(figsize=(10, 8))
sns.scatterplot(data=major_summary, x='Unemployment_rate', y='Median', hue='Major', size='Major', palette='viridis', alpha=0.6)
plt.title('Unemployment Rate vs. Median Income by Major')
plt.xlabel('Average Unemployment Rate (%)')
plt.ylabel('Median Income ($)')
plt.xscale('log')  # Using a log scale for better visibility of data spread
plt.show()
