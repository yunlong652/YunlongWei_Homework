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
gen_sur = df.groupby(['sex', 'Survived']).size().unstack()

# Plot the gender survival counts as a stacked bar chart
gen_sur.plot(kind='bar', stacked=True)
plt.xticks(rotation=0)
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()


