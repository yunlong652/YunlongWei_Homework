import pandas as pd
from skimpy import skim
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_3_titanic_dataset/titanic.csv')

skim(df) 
#print(df.head())
#print(df.info())
#print(df.describe())

sur_counts = df['Survived'].value_counts()
sur_counts.plot(kind='bar')
plt.xticks(ticks=[0, 1], labels=['no', 'yes'], rotation = 0)
plt.show

gen_sur = df.groupby(['sex', 'Survived']).size().unstack()
gen_sur.plot(kind='bar', stacked=True)
plt.xticks(rotation = 0)
plt.show()

