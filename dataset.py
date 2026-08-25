import pandas as pd

data={
  
  "days":[1,2,3,4,5,6,7],
  "calories":[420,390,520,200,1200,500,400]    
}
td=pd.DataFrame(data)
print(td.loc[6])