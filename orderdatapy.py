import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv(r'C:\Users\ACER\Downloads\orderdata.csv', encoding= 'unicode_escape')

df.shape
df.head(5)
df.info()
pd.isnull(df).sum()
df.columns
df.describe()
df[['Sales', 'Quantity', 'Profit']].describe()


ax = sns.countplot(x = 'Segment',data = df)

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

print()

# Sample data (replace with your actual data)
product_names = ['Product A', 'Product B', 'Product C', 'Product D']
product_counts = [915, 747, 600, 350]  # Example counts

# Create the bar chart
plt.bar(product_names, product_counts)

# Add labels and title (optional but good practice)
plt.xlabel("Product Name")
plt.ylabel("Count")
plt.title("Product Counts")

# Display the plot
plt.show()

print()

ax = sns.countplot(data = df, x = 'Region', hue = 'Category')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()
print()
sales_age = df.groupby(['Sub-Category'], as_index=False)['Profit'].sum().sort_values(by='Profit', ascending=False)

sns.barplot(x = 'Sub-Category',y= 'Profit' ,data = sales_age)
plt.show()

print()
# Get the top 5 most common product names and sort in descending order
top_5_products = df['Product Name'].value_counts().head(5).sort_values(ascending=False)

# Filter the dataframe to include only these top 5 products
filtered_df = df[df['Product Name'].isin(top_5_products.index)]

# Plot the countplot in descending order
sns.set(rc={'figure.figsize': (12, 5)})
ax = sns.countplot(data=filtered_df, x='Product Name', order=top_5_products.index)

# Add labels on bars
for bars in ax.containers:
    ax.bar_label(bars)

plt.show()


