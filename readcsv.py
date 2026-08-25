import pandas as pd  

df=pd.read_csv('d1.txt')
df.loc[len(df)]=[34,100,130,500]
print(df.to_string())
print(df.duplicated())
print(df)

