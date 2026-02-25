import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("/Users/abhaykumargupta/Desktop/pythonCA2/Warehouse_and_Retail_Sales.csv")

# Basic information
print(" Dataset Overview")
print(df.info())
print("/n First 5 Rows")
print(df.head())

# Create Date column
df['Date'] = pd.to_datetime(dict(year=df['YEAR'], month=df['MONTH'], day=1))

# Create Total Sales column
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# Check missing values
print("/n Missing Values:")
print(df.isnull().sum())

# Check for duplicates
print("/n Duplicate Records:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Summary statistics
print("/n Summary Statistics:")
print(df.describe())

# Unique product and category info
print("/n Unique Products:", df['ITEM DESCRIPTION'].nunique())
print(" Item Types:", df['ITEM TYPE'].unique())

# Visualization 1: Distribution of Total Sales
plt.figure(figsize=(10, 5))
sns.histplot(df['Total Sales'], bins=50, kde=True, color='blue')
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Visualization 2: Total Sales by Item Type
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df,
    x='ITEM TYPE',
    y='Total Sales',
    estimator=sum,
    hue='ITEM TYPE',
    palette='viridis',
    legend=False,
    errorbar=None
)
plt.title("Total Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Basic information
print(" Dataset Overview")
print(df.info())
print("\n First 5 Rows")
print(df.head())

# Create Date column
df['Date'] = pd.to_datetime(dict(year=df['YEAR'], month=df['MONTH'], day=1))

# Create Total Sales column
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# Check missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\n Duplicate Records:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Summary statistics
print("\n Summary Statistics:")
print(df.describe())

# Unique product and category info
print("\n Unique Products:", df['ITEM DESCRIPTION'].nunique())
print(" Item Types:", df['ITEM TYPE'].unique())

# Visualization 1: Distribution of Total Sales
plt.figure(figsize=(10, 5))
sns.histplot(df['Total Sales'], bins=50, kde=True, color='skyblue')
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
# Visualization 2: Total Sales by Item Type
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df,
    x='ITEM TYPE',
    y='Total Sales',
    estimator=sum,
    hue='ITEM TYPE',
    palette='viridis',
    legend=False,
    errorbar=None
)
plt.title("Total Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Create Date column
df['Date'] = pd.to_datetime(dict(year=df['YEAR'], month=df['MONTH'], day=1))

# Create Total Sales column
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# Check missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\n Duplicate Records:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Summary statistics
print("\n Summary Statistics:")
print(df.describe())

# Unique product and category info
print("\n Unique Products:", df['ITEM DESCRIPTION'].nunique())
print(" Item Types:", df['ITEM TYPE'].unique())

# Visualization 1: Distribution of Total Sales
plt.figure(figsize=(10, 5))
sns.histplot(df['Total Sales'], bins=50, kde=True, color='skyblue')
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Visualization 2: Total Sales by Item Type
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df,
    x='ITEM TYPE',
    y='Total Sales',
    estimator=sum,
    hue='ITEM TYPE',
    palette='viridis',
    legend=False,
    errorbar=None
)
plt.title("Total Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 1: Sales Trend Analysis Over Time
#  Create a proper datetime column from YEAR and MONTH
df['Date'] = pd.to_datetime(dict(year=df['YEAR'], month=df['MONTH'], day=1))

#  Calculate Total Sales
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

#  Group by Date (monthly)
monthly_sales = df.groupby('Date')['Total Sales'].sum().reset_index()

#  Group by Year
yearly_sales = df.groupby('YEAR')['Total Sales'].sum().reset_index()

#  Group by Quarter
df['Quarter'] = df['Date'].dt.to_period('Q')
quarterly_sales = df.groupby('Quarter')['Total Sales'].sum().reset_index()
quarterly_sales['Quarter'] = quarterly_sales['Quarter'].astype(str)  # Convert Period to string

#  Plot Monthly Sales Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Date', y='Total Sales', marker='o', color='steelblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

#  Plot Yearly Sales Summary
plt.figure(figsize=(8, 5))
sns.barplot(
    data=yearly_sales,
    x='YEAR',
    y='Total Sales',
    hue='YEAR',             
    palette='crest',
    legend=False,
    errorbar=None           
)
plt.title("Yearly Total Sales")  

plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()

# Plot Quarterly Sales Trend
plt.figure(figsize=(10, 5))
sns.lineplot(data=quarterly_sales, x='Quarter', y='Total Sales', marker='o', color='green')
plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 2: Comparison Between Warehouse and Retail Sales
# Create Total Sales column if not already present
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# Create a long-form DataFrame for Retail vs Warehouse
sales_by_type = pd.melt(
    df,
    id_vars=['Date'] if 'Date' in df.columns else None,
    value_vars=['RETAIL SALES', 'WAREHOUSE SALES'],
    var_name='Sales Channel',
    value_name='Sales'
)

# Clean channel names
sales_by_type['Sales Channel'] = sales_by_type['Sales Channel'].str.replace(' SALES', '')

# Total and average sales by channel
channel_summary = sales_by_type.groupby('Sales Channel')['Sales'].agg(['sum', 'mean']).reset_index()
print("Sales Summary (Total & Average):")
print(channel_summary)

# Bar Plot: Total Sales by Channel
plt.figure(figsize=(6, 5))
sns.barplot(
    data=channel_summary,
    x='Sales Channel',
    y='sum',
    hue='Sales Channel',
    palette='Set2',
    legend=False,
    errorbar=None
)
plt.title("Total Sales by Channel")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()


# Pie Chart: Contribution of Each Channel
plt.figure(figsize=(6, 6))
plt.pie(
    channel_summary['sum'],
    labels=channel_summary['Sales Channel'],
    autopct='%1.1f%%',
    colors=sns.color_palette('Set2')
)
plt.title("Sales Contribution: Retail vs Warehouse")
plt.tight_layout()
plt.show()

# Objective 3: Top Performing Products

# Create Total Sales column (if not already added)
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# 1️⃣ Top Products by Total Sales
top_products_total = df.groupby('ITEM TYPE')['Total Sales'].sum().sort_values(ascending=False).head(10).reset_index()

# 2️⃣ Top Products by Retail Sales
top_products_retail = df.groupby('ITEM TYPE')['RETAIL SALES'].sum().sort_values(ascending=False).head(10).reset_index()

# 3️⃣ Top Products by Warehouse Sales
top_products_warehouse = df.groupby('ITEM TYPE')['WAREHOUSE SALES'].sum().sort_values(ascending=False).head(10).reset_index()

# 🔹 Horizontal Bar Plot for Top Products by Total Sales
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_products_total,
    y='ITEM TYPE',
    x='Total Sales',
    hue='ITEM TYPE',
    palette='Blues_d',
    legend=False,
    errorbar=None  # remove confidence intervals
)
plt.title("Top 10 Products by Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

# 🔹 Horizontal Bar Plot for Top Products by Retail Sales
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_products_retail,
    y='ITEM TYPE',
    x='RETAIL SALES',
    hue='ITEM TYPE',
    palette='Greens_d',
    legend=False,
    errorbar=None
)
plt.title("Top 10 Products by Retail Sales")
plt.xlabel("Retail Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

# 🔹 Horizontal Bar Plot for Top Products by Warehouse Sales
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_products_warehouse,
    y='ITEM TYPE',
    x='WAREHOUSE SALES',
    hue='ITEM TYPE',
    palette='Oranges_d',
    legend=False,
    errorbar=None
)
plt.title("Top 10 Products by Warehouse Sales")
plt.xlabel("Warehouse Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

# Objective 4:  Correlation Between Product Price and Sales Volume

# Filter out rows with 0 transfers to avoid divide-by-zero
df_valid = df[df['RETAIL TRANSFERS'] > 0].copy()

# Calculate approximate price per unit
df_valid['PRICE PER UNIT'] = df_valid['RETAIL SALES'] / df_valid['RETAIL TRANSFERS']

# Display correlation
correlation = df_valid[['PRICE PER UNIT', 'RETAIL TRANSFERS']].corr()
print("🔗 Correlation Matrix:")
print(correlation)

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(data=df_valid, x='PRICE PER UNIT', y='RETAIL TRANSFERS', scatter_kws={'alpha':0.5})
plt.title("Correlation Between Product Price and Quantity Sold")
plt.xlabel("Price Per Unit ($)")
plt.ylabel("Quantity Sold (Retail Transfers)")
plt.tight_layout()
plt.show()

# Objective 5:  Peak Sales Months

# Create datetime column
df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'].astype(str) + '-01')

# Extract month name for visualization
df['MONTH_NAME'] = df['DATE'].dt.strftime('%B')

# Calculate total sales
df['TOTAL SALES'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# Order the months
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

# Group and sort data
monthly_sales = df.groupby('MONTH_NAME')['TOTAL SALES'].sum().reindex(month_order)

# Plot the result without emoji and FutureWarning
plt.figure(figsize=(10, 6))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
plt.xticks(rotation=45)
plt.title("Total Sales by Month")  
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
