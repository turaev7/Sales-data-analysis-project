import pandas as pd

def clean_data(input_path="../data/raw/sales_data.csv", output_path="../data/processed/sales_data_clean.csv"):
    # Load raw data
    df = pd.read_csv(input_path)

    # Rename column
    df.rename(columns={"Total": "Sales"}, inplace=True)

    # Fill missing values in Sales
    df['Sales'].fillna(0, inplace=True)

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print("Data cleaning completed and saved to", output_path)

if __name__ == "__main__":
    clean_data()
