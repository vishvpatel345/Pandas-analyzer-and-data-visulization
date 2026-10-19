import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self, file):
        self.data = pd.read_csv(file)

    def explore_data(self):
        print(self.data.head())
        print(self.data.info())
        print(self.data.describe())

    def clean_data(self):
        self.data = self.data.dropna()
        print("Data cleaned successfully")

    def analyze_data(self):
        print("Total Sales:", self.data["Sales"].sum())
        print("Average Sales:", self.data["Sales"].mean())
        print("Maximum Sales:", self.data["Sales"].max())
        print("Minimum Sales:", self.data["Sales"].min())
        print("Standard Deviation:", self.data["Sales"].std())
        print("Variance:", self.data["Sales"].var())
        print("Median:", self.data["Sales"].median())

    def search_data(self):
        product = input("Enter product name: ")
        print(self.data[self.data["Product"] == product])

    def sort_data(self):
        self.data = self.data.sort_values("Sales")
        print(self.data)

    def filter_data(self):
        amount = float(input("Enter minimum sales: "))
        print(self.data[self.data["Sales"] > amount])

    def group_data(self):
        print(self.data.groupby("Region")["Sales"].sum())

    def array_operations(self):
        arr = np.array(self.data["Sales"])

        print("Array:", arr)
        print("First value:", arr[0])
        print("First three values:", arr[:3])
        print("Array + 10:", arr + 10)
        print("Array * 2:", arr * 2)

    def pivot_table(self):
        print(pd.pivot_table(
            self.data,
            values="Sales",
            index="Region",
            columns="Product",
            aggfunc="sum",
            fill_value=0
        ))

    def visualize_data(self):
        self.data.groupby("Product")["Sales"].sum().plot(
            kind="bar", title="Sales by Product"
        )
        plt.tight_layout()
        plt.savefig("sales_chart.png")
        plt.show()

        self.data.plot(
            x="Sales", y="Profit", kind="scatter",
            title="Sales vs Profit"
        )
        plt.tight_layout()
        plt.savefig("sales_scatter.png")
        plt.show()

        self.data["Sales"].plot(
            kind="hist", title="Sales Distribution"
        )
        plt.tight_layout()
        plt.savefig("sales_histogram.png")
        plt.show()

        self.data.groupby("Region")["Sales"].sum().plot(
            kind="pie", autopct="%1.1f%%",
            title="Regional Sales"
        )
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig("sales_pie.png")
        plt.show()

        sns.boxplot(data=self.data, x="Region", y="Sales")
        plt.title("Sales by Region")
        plt.tight_layout()
        plt.savefig("sales_boxplot.png")
        plt.show()

    def export_data(self):
        self.data.to_csv("analyzed_sales.csv", index=False)
        print("Data exported successfully")


def main():

    analyzer = SalesDataAnalyzer("sales.csv")

    while True:
        print("\n--- Sales Data Analyzer ---")
        print("1. Explore Data")
        print("2. Clean Data")
        print("3. Analyze Sales")
        print("4. Search Product")
        print("5. Sort Sales")
        print("6. Filter Sales")
        print("7. Group by Region")
        print("8. NumPy Operations")
        print("9. Pivot Table")
        print("10. Visualize Data")
        print("11. Export Data")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            analyzer.explore_data()
        elif choice == "2":
            analyzer.clean_data()
        elif choice == "3":
            analyzer.analyze_data()
        elif choice == "4":
            analyzer.search_data()
        elif choice == "5":
            analyzer.sort_data()
        elif choice == "6":
            analyzer.filter_data()
        elif choice == "7":
            analyzer.group_data()
        elif choice == "8":
            analyzer.array_operations()
        elif choice == "9":
            analyzer.pivot_table()
        elif choice == "10":
            analyzer.visualize_data()
        elif choice == "11":
            analyzer.export_data()
        elif choice == "12":
            print("Thank you!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()