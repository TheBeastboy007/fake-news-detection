import pandas as pd

csv_file = "C:\fake-news-detection\data-collection\data\data.csv"  # Update this path
df = pd.read_csv(csv_file)

print(df.head())  # Show the first 5 rows
print(df.columns)  # Display column names
