import pandas as pd
data = {
    "Name": ["Ram", "Ram", "Shyam", "Shyam"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
pivot_df = df.pivot(index="Name", columns="Subject", values="Marks")

melted = pd.melt(pivot_df.reset_index(),id_vars=["Name"],var_name="Subject",
value_name="Marks"
)

print(melted)
