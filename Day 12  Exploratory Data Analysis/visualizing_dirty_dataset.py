import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dirty_dataset.csv')


# 1. How is Age distributed?
sns.histplot(df['Age'], kde=True, color='blue', bins=15)
plt.title('Distribution of Customer Age')
plt.tight_layout()
plt.show()

# Insight: Is the data "Normal" (bell-shaped) or is it skewed toward younger/older people?

# 2. Does Age affect how much people spend?

sns.scatterplot(data=df, x='Age', y='Price_USD', hue='City')
plt.title('Relationship: Age vs Price (by City)')
plt.tight_layout()
plt.show()

# Insight: If the dots go UP as they go RIGHT, you have a positive correlation.


# 3. Which city generates the most revenue?
# We create a temporary column for Revenue
# df['Revenue'] = df['Price_USD'] * df['Quantity']

# sns.barplot(data=df, x='City', y='Revenue', estimator=sum)
# plt.title('Total Revenue by City')
# plt.tight_layout()

# 4. Checking for Revenue Outliers
# sns.boxplot(x=df['Revenue'])
# plt.title('Detecting Revenue Outliers')
# plt.tight_layout()
# plt.show()

# 5. The Heatmap
plt.figure(figsize=(8, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Cleaned Data')
plt.tight_layout()
plt.show()