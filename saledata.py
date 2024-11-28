# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Users\lenovo\Downloads\sales_data_sample.csv'
sales_data = pd.read_csv(file_path, encoding='latin1')

# Data Cleaning
# Convert ORDERDATE to datetime format
sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce')

# Handle missing values
sales_data['ADDRESSLINE2'].fillna('', inplace=True)  # Fill ADDRESSLINE2 with an empty string
sales_data['STATE'].fillna('Unknown', inplace=True)  # Fill STATE with 'Unknown'
sales_data['TERRITORY'].fillna('Unknown', inplace=True)  # Fill TERRITORY with 'Unknown'
sales_data['POSTALCODE'].fillna('00000', inplace=True)  # Fill POSTALCODE with '00000'

# Summary and total data count
print("Dataset Summary:")
print(sales_data.describe(include='all'))  # Provide summary statistics for all columns
print("\nTotal Number of Records:", sales_data.shape[0])  # Display total number of rows

# Exploratory Data Analysis (EDA)
# 1. Distribution of SALES
plt.figure(figsize=(10, 6))
sns.histplot(sales_data['SALES'], bins=30, kde=True, color='blue')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# 2. Count of orders by DEALSIZE
plt.figure(figsize=(8, 5))
sns.countplot(data=sales_data, x='DEALSIZE', order=sales_data['DEALSIZE'].value_counts().index, palette='viridis')
plt.title('Order Count by Deal Size')
plt.xlabel('Deal Size')
plt.ylabel('Count')
plt.show()

# Data Aggregation
# Total sales
total_sales = sales_data['SALES'].sum()

# Average sales per customer
average_sales_per_customer = sales_data.groupby('CUSTOMERNAME')['SALES'].mean()

# Total sales by product line
sales_by_productline = sales_data.groupby('PRODUCTLINE')['SALES'].sum()

# Total sales by deal size
sales_by_dealsize = sales_data.groupby('DEALSIZE')['SALES'].sum()

# Total sales per year
sales_by_year = sales_data.groupby('YEAR_ID')['SALES'].sum()

# Print Aggregated Results
print(f"\nTotal Sales: ${total_sales:,.2f}")
print("\nAverage Sales Per Customer (Top 5):")
print(average_sales_per_customer.head())
print("\nTotal Sales by Product Line:")
print(sales_by_productline)
print("\nTotal Sales by Deal Size:")
print(sales_by_dealsize)
print("\nTotal Sales by Year:")
print(sales_by_year)

# Key Insights
print("\n--- Key Insights ---")
print("1. Classic Cars and Vintage Cars contribute the highest revenue among product lines.")
print("2. Medium-sized deals account for the majority of the sales.")
print("3. Sales peaked in 2004, followed by a significant decline in 2005.")
print("4. Most orders are of medium and small deal sizes, while large deals are rare.")
print("5. Customer spending varies widely, with some customers averaging high sales figures.")

# Visualization of Total Sales by Product Line
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_productline.index, y=sales_by_productline.values, palette="viridis")
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization of Total Sales by Deal Size
plt.figure(figsize=(8, 5))
sns.barplot(x=sales_by_dealsize.index, y=sales_by_dealsize.values, palette="coolwarm")
plt.title('Total Sales by Deal Size')
plt.xlabel('Deal Size')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.show()

# Visualization of Total Sales by Year
plt.figure(figsize=(8, 5))
sns.lineplot(x=sales_by_year.index, y=sales_by_year.values, marker='o', color='green')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.show()
