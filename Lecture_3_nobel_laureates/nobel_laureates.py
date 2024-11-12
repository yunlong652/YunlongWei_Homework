import pandas as pd 

read_file = pd.read_excel ("/Users/apple/Documents/GitHub/YunlongWei_Homework/Lecture_3_nobel_laureates/nobel.xlsx") 

read_file.to_csv ("nobel.csv", 
				index = None, 
				header=True) 
	
#read nobel.csv
df = pd.DataFrame(pd.read_csv("nobel.csv")) 
#print(df)
 
#information for dataset
infor = df.info()
print(infor)

#new data frame called nobel_living
nobel_living = df[
    df['country'].notna() &
    (df['gender'] != 'org') &
    df['died_date'].isna()        
]
print(nobel_living)
print(nobel_living.shape[0])


#Where were most Nobel laureates based when they won their prizes?
x,y = df['country'].value_counts().idxmax(), df['country'].value_counts().max()
print(x,y)