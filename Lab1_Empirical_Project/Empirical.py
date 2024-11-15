import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pingouin as pg
from lets_plot import *

LetsPlot.setup_html(no_js=True)


### You don't need to use these settings yourself
### — they are just here to make the book look nicer!
# Set the plot style for prettier charts:
#plt.style.use(
#    "https://raw.githubusercontent.com/aeturrell/core_python/main/plot_style.txt"
#)

#Python Walkthrough 1.1
df = pd.read_csv(
    "https://data.giss.nasa.gov/gistemp/tabledata_v4/NH.Ts+dSST.csv",
    skiprows=1,
    na_values="***",
)

#print(df.head())
#print(df.info())

#Python Walkthrough 1.2

df = df.set_index("Year")
df.head()
df.tail()

fig, ax = plt.subplots()
df["Jan"].plot(ax=ax)
ax.set_ylabel("y label")
ax.set_xlabel("x label")
ax.set_title("title")
plt.show()

fig, ax = plt.subplots()
ax.plot(df.index, df["Jan"])
ax.set_ylabel("y label")
ax.set_xlabel("x label")
ax.set_title("title")
plt.show()