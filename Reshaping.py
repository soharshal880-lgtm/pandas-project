import pandas as pd

data = {
    "Name": ["A", "A", "B", "B"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [90, 80, 85, 88]
}

df = pd.DataFrame(data)

pivot_df = df.pivot(index="Name", columns="Subject", values="Marks")

print(pivot_df)
