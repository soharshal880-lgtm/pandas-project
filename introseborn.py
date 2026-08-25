import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8] 

# We reshape the data to a grid format for the heatmap
temp_df = pd.DataFrame({"temperature": temperature}, index=days)

# Plotting
plt.figure(figsize=(2, 6))
sns.heatmap(temp_df, annot=True, cmap="YlOrRd", fmt="g")
plt.title("Temp Heatmap")
plt.ylabel("Days")
plt.show() 