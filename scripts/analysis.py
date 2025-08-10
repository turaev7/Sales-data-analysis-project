import pandas as pd

def analyze_data(input_path="../data/processed/sales_data_clean.csv"):
    df = pd.read_csv(input_path)
    df['Date'] = pd.to_datetime(df['Date'])

    # Basic KPIs
    total_sales = df['Sales'].sum()
    sales_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

    print("\nTotal Sales:", total_sales)
    print("\nSales by Product:\n", sales_by_product)

    # Best product
    best_product = sales_by_product.idxmax()
    best_sales = sales_by_product.max()

    # Monthly sales
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum()

    print("\nBest Month:", monthly_sales.idxmax(), "with sales", monthly_sales.max())

    # Return these values if needed
    return {
        "total_sales": total_sales,
        "sales_by_product": sales_by_product,
        "best_product": best_product,
        "best_sales": best_sales,
        "monthly_sales": monthly_sales
    }

if __name__ == "__main__":
    analyze_data()
