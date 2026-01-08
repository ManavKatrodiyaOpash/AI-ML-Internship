import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Setting a seed so the "random" data is the same every time you run it
np.random.seed(42)

# Creating a dataset of 100 days of sales for a Tech Store
days = pd.date_range(start='2023-01-01', periods=100)
data = {
    'Date': days,
    'Sales_USD': np.random.normal(500, 100, 100).cumsum(), # Cumulative sales (Trend)
    'Customer_Age': np.random.randint(18, 75, 100),       # Distribution
    'Units_Sold': np.random.randint(1, 10, 100),          # Frequency
    'Discount_Percent': np.random.uniform(0, 30, 100),    # Relationship
    'Category': np.random.choice(['Laptops', 'Phones', 'Accessories', 'Tablets'], 100), # Groups
    'Profit': np.random.normal(50, 20, 100)               # Performance
}

df = pd.DataFrame(data)

# Adding some outliers to Profit for the Box Plot task
df.loc[0, 'Profit'] = 250
df.loc[1, 'Profit'] = -150

print("Dataset is ready! Here is a preview:")
print(df)
print(f"Shape :- {df.shape}")

#1 Line Plot :-
def line_plot():
    plt.plot(df['Date'], df['Sales_USD'], color='blue', linewidth=2, label='Sales USD')#,marker='o'
    plt.title('1. Line Plot')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Sales (USD)')
    plt.xticks(rotation=45)  # Rotate dates so they don't overlap
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

#2 Bar Plot :-
def bar_plot():
    category_data = df.groupby('Category')['Units_Sold'].sum()
    plt.bar(category_data.index, category_data.values, color='skyblue', edgecolor='black',label='Categories')
    plt.xlabel('Product Category')
    plt.ylabel('Total Units Sold')
    plt.title('2. Bar Chart')
    plt.legend()
    plt.show()

#3 Scatter Plot :-
def scatter_plot():
    plt.scatter(df['Discount_Percent'], df['Profit'], alpha=0.6, color='purple')
    plt.axhline(0, color='red', linestyle='--') # Add a line at zero profit
    plt.xlabel('Discount %')
    plt.ylabel('Profit')
    plt.title('3. Scatter Plot')
    plt.show()

# 4. Box Plot :-
def box_plot():
    plt.boxplot(df['Profit'])
    plt.title('4. Box Plot ')
    plt.xlabel('Units_Sold')
    plt.ylabel('Profit')
    plt.show()

# 5. Histogram Plot :-
def histogram_plot():
    plt.hist(df['Profit'],bins=50)
    plt.title('5. Histogram ')
    plt.xlabel('Profit')
    plt.ylabel('Count')
    plt.show()

#6. Pie Chart :-
def pie_chart():
    category_counts = df['Category'].value_counts()
    plt.pie(category_counts,labels=category_counts.index,autopct="%1.1f%%")
    plt.title('6. Pie Chart ')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.legend()
    plt.axis('equal')
    plt.show()

#7. Heatmap :-
def heat_map():
    print("Matplotlib has no heatmap function")

if __name__ == "__main__":
    line_plot()
    bar_plot()
    scatter_plot()
    box_plot()
    histogram_plot()
    pie_chart()
    heat_map()