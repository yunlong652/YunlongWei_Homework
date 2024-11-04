'''Which major has the lowest unemployment rate?
Which major has the highest percentage of women?
How do the distributions of median income compare across major categories?
Do women tend to choose majors with lower or higher earnings?'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
lowest_unemp_rate = allages.loc[allages['Unemployment_rate'].idxmin()]
print(f"Major with the lowest unemployment rate: {lowest_unemp_rate['Major']} with a rate of {lowest_unemp_rate['Unemployment_rate']}")

plt.figure(figsize=(10, 8))
plt.bar(allages['Major'], allages['Unemployment_rate'], color='blue')
plt.xlabel('Major')
plt.ylabel('Unemployment Rate')
plt.title('Unemployment Rate by Major')
plt.xticks(rotation=90)
plt.show()

print("----------------------------------------------------------------")

#Which major has the highest percentage of women
womenstem['ShareWomen'] = (womenstem['Women'] / (womenstem['Men'] + womenstem['Women'])) * 100
max_women_major = womenstem.loc[womenstem['ShareWomen'].idxmax()]
print(f"Major with the highest percentage of women: {max_women_major['Major']} with {max_women_major['ShareWomen']}% women")

plt.figure(figsize=(10, 8))
plt.bar(womenstem['Major'], womenstem['ShareWomen'], color='pink')
plt.xlabel('Major')
plt.ylabel('Percentage of Women')
plt.title('Percentage of Women by Major')
plt.xticks(rotation=90)
plt.show()


print("----------------------------------------------------------------")

#How do the distributions of median income compare across major categories
median_income_by_category = allages.groupby('Major_category')['Median'].median()
print("Median income by major category:")
print(median_income_by_category)

plt.figure(figsize=(12, 8))
sns.boxplot(x='Major_category', y='Median', data=allages)
plt.xlabel('Major Category')
plt.ylabel('Median Salary')
plt.title('Median Salary by Major Category')
plt.xticks(rotation=45)
plt.show()

print("----------------------------------------------------------------")

#Do women tend to choose majors with lower or higher earnings?
threshold = 50
high_women_median_income = womenstem[womenstem['ShareWomen'] > threshold]['Median'].median()
low_women_median_income = womenstem[womenstem['ShareWomen'] <= threshold]['Median'].median()

if high_women_median_income > low_women_median_income:
    print("Women tend to choose majors with higher earnings.")
else:
    print("Women tend to choose majors with lower earnings.")


plt.figure(figsize=(10, 8))
plt.scatter(womenstem['ShareWomen'], womenstem['Median'], color='purple')
plt.xlabel('Percentage of Women')
plt.ylabel('Median Salary')
plt.title('Median Salary vs. Percentage of Women')
plt.grid(True)
plt.show()

