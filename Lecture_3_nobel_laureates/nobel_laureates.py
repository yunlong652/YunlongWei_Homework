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
#print(infor)

#???

#Where were most Nobel laureates based when they won their prizes?
location_most_nobel = df['born_country'].value_counts().head(10) 
#print(location_most_nobel)