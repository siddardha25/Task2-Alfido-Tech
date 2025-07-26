import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------------------
# SETTINGS
# -----------------------------------------------------

csv_path = r"C:\Users\HP\OneDrive\Desktop\task 2\superstore_final_dataset (1).csv"
save_folder = r"C:\Users\HP\OneDrive\Desktop\task 2\graphs"

# Create folder if not exists
os.makedirs(save_folder, exist_ok=True)

# -----------------------------------------------------
# LOAD DATA
# -----------------------------------------------------

# Read CSV
df = pd.read_csv(csv_path, encoding='latin1')

print("[INFO] Data loaded successfully.")
print("[INFO] Columns in your dataset:")
print(df.columns.tolist())

# -----------------------------------------------------
# FIND DATE COLUMN
# -----------------------------------------------------

# Try to find any column containing "date"
date_column = next(
    (col for col in df.columns if "date" in col.lower()),
    None
)

if date_column is None:
    print("[ERROR] No date column found. Exiting.")
    exit()

print(f"[INFO] Using date column: {date_column}")

# -----------------------------------------------------
# PREPARE DATA
# -----------------------------------------------------

df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
df = df.dropna(subset=[date_column])

df['Year'] = df[date_column].dt.year
df['Month'] = df[date_column].dt.month

# -----------------------------------------------------
# PLOT 1 - Monthly Sales Revenue Trend
# -----------------------------------------------------

if 'Sales' not in df.columns:
    print("[ERROR] No 'Sales' column in data. Exiting.")
    exit()

monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(
    data=monthly_sales,
    x='Month',
    y='Sales',
    hue='Year',
    marker='o',
    palette='tab10'
)

plt.title("Monthly Revenue Trends by Year", fontsize=16, weight='bold')
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.legend(title='Year', loc='upper left')
plt.tight_layout()

file_path = os.path.join(save_folder, 'monthly_revenue_trends.png')
plt.savefig(file_path, dpi=300)
plt.show()
plt.close()

print(f"[OK] Saved: {file_path}")

# -----------------------------------------------------
# PLOT 2 - Sales by Product Category
# -----------------------------------------------------

if 'Category' in df.columns:
    category_sales = df.groupby('Category')['Sales'].sum().sort_values()

    plt.figure(figsize=(10,6))
    sns.barplot(
        x=category_sales.values,
        y=category_sales.index,
        palette='viridis'
    )
    plt.title("Sales by Product Category", fontsize=16, weight='bold')
    plt.xlabel("Total Sales (₹)")
    plt.ylabel("Category")
    plt.tight_layout()

    file_path = os.path.join(save_folder, 'sales_by_category.png')
    plt.savefig(file_path, dpi=300)
    plt.show()
    plt.close()

    print(f"[OK] Saved: {file_path}")
else:
    print("[WARN] No 'Category' column found. Skipping Category plot.")

# -----------------------------------------------------
# PLOT 3 - Sales by Region
# -----------------------------------------------------

if 'Region' in df.columns:
    region_sales = df.groupby('Region')['Sales'].sum().sort_values()

    plt.figure(figsize=(10,6))
    sns.barplot(
        x=region_sales.values,
        y=region_sales.index,
        palette='cubehelix'
    )
    plt.title("Sales by Region", fontsize=16, weight='bold')
    plt.xlabel("Total Sales (₹)")
    plt.ylabel("Region")
    plt.tight_layout()

    file_path = os.path.join(save_folder, 'sales_by_region.png')
    plt.savefig(file_path, dpi=300)
    plt.show()
    plt.close()

    print(f"[OK] Saved: {file_path}")
else:
    print("[WARN] No 'Region' column found. Skipping Region plot.")

# -----------------------------------------------------
# PLOT 4 - Sales by Customer Segment
# -----------------------------------------------------

if 'Segment' in df.columns:
    segment_sales = df.groupby('Segment')['Sales'].sum().sort_values()

    plt.figure(figsize=(8,5))
    sns.barplot(
        x=segment_sales.values,
        y=segment_sales.index,
        palette='magma'
    )
    plt.title("Sales by Customer Segment", fontsize=16, weight='bold')
    plt.xlabel("Total Sales (₹)")
    plt.ylabel("Segment")
    plt.tight_layout()

    file_path = os.path.join(save_folder, 'sales_by_segment.png')
    plt.savefig(file_path, dpi=300)
    plt.show()
    plt.close()

    print(f"[OK] Saved: {file_path}")
else:
    print("[WARN] No 'Segment' column found. Skipping Segment plot.")

# -----------------------------------------------------
# PLOT 5 - Top 10 Products by Sales
# -----------------------------------------------------

if 'Product Name' in df.columns:
    top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12,6))
    sns.barplot(
        x=top_products.values,
        y=top_products.index,
        palette='coolwarm'
    )
    plt.title("Top 10 Products by Sales", fontsize=16, weight='bold')
    plt.xlabel("Total Sales (₹)")
    plt.ylabel("Product Name")
    plt.tight_layout()

    file_path = os.path.join(save_folder, 'top_10_products.png')
    plt.savefig(file_path, dpi=300)
    plt.show()
    plt.close()

    print(f"[OK] Saved: {file_path}")
else:
    print("[WARN] No 'Product Name' column found. Skipping Product plot.")

# -----------------------------------------------------
# PRINT Top Customers
# -----------------------------------------------------

if 'Customer Name' in df.columns:
    top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Customers by Sales:")
    print(top_customers)
else:
    print("[WARN] No 'Customer Name' column found. Skipping customer summary.")
