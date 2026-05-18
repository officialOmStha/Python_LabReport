# Lab 10:
import pandas as pd
import matplotlib.pyplot as plt


class SalesAnalyzer:

    # Constructor
    def __init__(self, filename):

        # Load CSV file into DataFrame
        self.df = pd.read_csv(filename)

        print("Original Data:")
        print(self.df)

        # Handle missing data
        # Fill numeric missing values with 0
        self.df = self.df.fillna(0)

        # Optionally drop rows with missing values
        # self.df = self.df.dropna()

        print("\nData After Handling Missing Values:")
        print(self.df)

    # Method to calculate total sales per product
    def total_sales_per_product(self):

        total_sales = self.df.groupby("Product")["Sales"].sum()

        print("\nTotal Sales Per Product:")
        print(total_sales)

        return total_sales

    # Method to display top N products
    def top_n_products(self, n):

        top_products = (
            self.df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

        print(f"\nTop {n} Products:")
        print(top_products)

        return top_products

    # Method to plot sales
    def plot_sales(self):

        sales_data = self.df.groupby("Product")["Sales"].sum()

        # Bar Chart
        plt.figure(figsize=(6, 4))
        plt.bar(sales_data.index, sales_data.values)
        plt.title("Sales Per Product")
        plt.xlabel("Products")
        plt.ylabel("Sales")
        plt.show()

        # Pie Chart
        plt.figure(figsize=(6, 6))
        plt.pie(
            sales_data.values,
            labels=sales_data.index,
            autopct="%1.1f%%"
        )
        plt.title("Sales Distribution")
        plt.show()


# Main Program

# Sample CSV filename
filename = "sales_data.csv"

# Create object
analyzer = SalesAnalyzer(filename)

# Call methods
analyzer.total_sales_per_product()

analyzer.top_n_products(2)

analyzer.plot_sales()