import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting a seed so the "random" data is the same every time you run it
np.random.seed(42)

# Creating a dataset of 100 days of sales for a Tech Store
days = pd.date_range(start='2023-01-01', periods=100)
data = {
    'Date': days,
    'Sales_USD': np.random.normal(500, 100, 100).cumsum(),  # Cumulative sales (Trend)
    'Customer_Age': np.random.randint(18, 75, 100),  # Distribution
    'Units_Sold': np.random.randint(1, 10, 100),  # Frequency
    'Discount_Percent': np.random.uniform(0, 30, 100),  # Relationship
    'Category': np.random.choice(['Laptops', 'Phones', 'Accessories', 'Tablets'], 100),  # Groups
    'Profit': np.random.normal(50, 20, 100)  # Performance
}

df = pd.DataFrame(data)

# Adding some outliers to Profit for the Box Plot task
df.loc[0, 'Profit'] = 250
df.loc[1, 'Profit'] = -150

print("Dataset is ready! Here is a preview:")
print(df)
print(f"Shape :- {df.shape}")

# 1. Line Plot :-
def line_plot():
    sns.lineplot(x="Date", y="Sales_USD", data=df)
    plt.title("1. Line Plot")
    plt.xlabel('Date')
    plt.ylabel('Cumulative Sales (USD)')
    plt.show()

# 2. Bar Plot :-
def bar_plot():
    sns.barplot(x="Category", y="Units_Sold", data=df, hue="Category")
    plt.title("2. Bar Plot")
    plt.show()

# 3. Scatter Plot :-
def scatter_plot():
    sns.scatterplot(x="Discount_Percent", y="Profit", data=df)
    plt.title("3. Scatter Plot")
    plt.show()

# 4. Box Plot :-
def box_plot():
    sns.boxplot(x="Profit", data=df)
    plt.title("4. Box Plot")
    plt.show()

# 5. Histogram Plot :-
def histogram_plot():
    sns.histplot(x="Profit", data=df)
    plt.title("5. Histogram Plot")
    plt.show()

# 6. Pie Chart :-
def pie_chart():
    print("Seaborn has no pie chart function")

# 7. Heatmap :-
def heat_map():
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("7. Heat Map")
    plt.show()

if __name__ == "__main__":
    line_plot()
    bar_plot()
    scatter_plot()
    box_plot()
    histogram_plot()
    pie_chart()
    heat_map()
