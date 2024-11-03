import pandas as pd
from skimpy import skim
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_3_titanic_dataset/titanic.csv')

skim(df) 
print(df.head())
print(df.info())
print(df.describe())



