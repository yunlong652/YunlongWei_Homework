import pandas as pd
from skimpy import skim
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_3_titanic_dataset/titanic.csv')

# Display a summary of the dataset
skim(df) 

# to view the first few rows, info, and descriptive statistics
print(df.head())
print(df.info())
print(df.describe()) 

sur_age = df.groupby(['Age', 'Survived']).size().unstack()

# Creating a stacked bar plot
ax = sur_age.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xticks(rotation=0)
plt.title('Survival by Age', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Adding a legend for better interpretation
plt.legend(title='Survived', labels=['No', 'Yes'], title_fontsize='13', fontsize='12')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()  # Adjusts plot to make room for labels
plt.show()


# Count the number of survivors and non-survivors
sur_counts = df['Survived'].value_counts()

# Plot the survival counts as a bar chart
sur_counts.plot(kind='bar')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'], rotation=0)
plt.title('Survival Counts')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# Group data by gender and survival status, then count occurrences
gen_sur = df.groupby(['Sex', 'Survived']).size().unstack()

# Plot the gender survival counts as a stacked bar chart
gen_sur.plot(kind='bar', stacked=True)
plt.xticks(rotation=0)
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()


