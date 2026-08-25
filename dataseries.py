import pandas 
my=[5,1,2] 
ot=pandas.Series(my ,index=["x","y","z"])
# print(ot)
print(ot["x"])




import pandas as pd

a = [1, 7, 2]
idx = ["x", "y", "z"]

myvar = pd.Series(a, index=idx)

print(myvar)
