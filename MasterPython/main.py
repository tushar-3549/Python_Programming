import csv
import pandas as pd
from datetime import datetime 
from data_entry import get_date, get_ammount, get_category, get_description
import matplotlib.pyplot as plt 

# GUI Backend set
import matplotlib
matplotlib.use("TkAgg")

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "ammount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, ammount, category, description):
        new_entry = {
            "date": date,
            "ammount": ammount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("Data Entry Successfully...")
        
    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No Transaction found in the given date range.")
        else:
            print(f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "Income"]["ammount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["ammount"].sum()

            print("Summary:\n")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
        
        return filtered_df

def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = df[df["category"] == "Income"].resample('D').sum().reindex(df.index, fill_value=0)
    expense_df = df[df["category"] == "Expense"].resample('D').sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df["ammount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["ammount"], label="Expense", color="r")

    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.savefig("transactions_plot.png")
    print("Plot saved as 'transactions_plot.png'")


def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for todays date: ", allow_default=True)
    ammount = get_ammount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, ammount, category, description)

# CSV.get_transaction("10-03-2024", "10-05-2025")
# add()

def main():
    while True:
        print("\n1. Add a new Transaction: ")
        print("2. View Transactions and summary within a date range: ")
        print("3. Exit: ")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transaction(start_date, end_date)
            if input("Do you want to see the plot? (y/n): ").lower() =="y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
