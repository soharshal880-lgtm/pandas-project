import pandas as pd
data = {
    "Name": ["Ram", "Ram", "Shyam", "Shyam"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
pivot_df = df.pivot(index="Name", columns="Subject", values="Marks")

stacked = pivot_df.stack()
transposed = pivot_df.T
print(transposed)
