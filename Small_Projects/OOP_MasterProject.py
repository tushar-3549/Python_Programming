import json

class Transaction:
    def __init__(self, title, amount, trans_type, note=""):
        self.title = title
        self.amount = amount
        self.trans_type = trans_type
        self.note = note

    def display_info(self):
        return (
            f"Transaction:\n"
            f" Title : {self.title}\n"
            f" Amount: {self.amount}\n"
            f" Type  : {self.trans_type}\n"
            f" Note  : {self.note}"
        )


class Book:
    def __init__(self):
        self.wallet = []

    def add_transaction(self, trans):
        self.wallet.append(trans)

    def del_transaction(self, title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f"{title} has been removed..."
        return f"{title} is not found..."

    def display(self):
        if not self.wallet:
            return f"No transaction in your wallet!"
        return f"\n".join([trans.display_info() for trans in self.wallet])

    def search(self, keyword):
        res = [trans for trans in self.wallet if keyword.lower() in trans.title.lower()]
        if not res:
            return f"No transaction found in {keyword}"
        return "\n".join([trans.display_info() for trans in res])

    def save_file(self, filename="wallet.json"):
        data = [{
            'Expense': transaction.title,
            'Amount': transaction.amount,
            'Type': transaction.trans_type,
            'Note': transaction.note
        } for transaction in self.wallet]

        with open(filename, "w") as file:
            json.dump(data, file)

        return "Data saved successfully!"

    def load_file(self, filename="wallet.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.wallet = []
            for trans in data:
                transaction = Transaction(
                    trans['Expense'],
                    trans['Amount'],
                    trans['Type'],
                    trans['Note']
                )
                self.wallet.append(transaction)
        except FileNotFoundError:
            print("We don't have that file...")


def main():
    book = Book()
    book.load_file()

    while True:
        print("\n==== Wallet Menu ====")
        print("1. Add Transaction")
        print("2. Delete Transaction")
        print("3. Display All Transactions")
        print("4. Search Transactions")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            amount = float(input("Amount: "))
            trans_type = input("Type (e.g., Food, Transport): ")
            note = input("Note (optional): ")
            t = Transaction(title, amount, trans_type, note)
            book.add_transaction(t)
            print("Transaction added.")

        elif choice == "2":
            title = input("Enter title to delete: ")
            print(book.del_transaction(title))

        elif choice == "3":
            print("\n" + book.display())

        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            print("\n" + book.search(keyword))

        elif choice == "5":
            print(book.save_file())
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
