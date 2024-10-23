import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loads and reads the dataset
df = pd.read_csv('car_data.csv')
print("Data Loaded Successfully")
print(df)

# Checks for any missing values and print them out
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check for duplicate rows and displays the number of duplicated rows but ignores them when visualizing the data
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")

# Check the data types in the DataFrame
print("\nData types in the DataFrame:")
df.info()

# This where you get the summary of the data 
summary_stats = df.describe()
print("\nSummary statistics:")
print(summary_stats)

# Count the number of cars produced each year
production_by_year = df['year'].value_counts().sort_index()

# Set figure size
plt.figure(figsize=(15, 8))

# Create a line plot of car production by year
sns.lineplot(x=production_by_year.index, y=production_by_year.values, marker='o')

# Title and labels
plt.title('Car Production by Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Cars Produced', fontsize=14)
plt.xticks(rotation=45)  
plt.grid()  
plt.tight_layout() 

# Annotate the summary statistics on the side
textstr = '\n'.join([f"{col}: {summary_stats[col]['mean']:.2f}" for col in summary_stats.columns])
plt.gca().text(1.05, 0.5, textstr, fontsize=10, transform=plt.gca().transAxes,
                verticalalignment='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

# This where we display data
plt.show()
