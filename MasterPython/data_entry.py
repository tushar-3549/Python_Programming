from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    usr_input = input(prompt)
    if allow_default and not usr_input:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(usr_input, date_format)
        return valid_date.strftime(date_format)
    except Exception as e:
        print(e)
        return get_date(prompt, allow_default)

def get_ammount():
    try:
        ammount = float(input("Enter the ammount: "))
        if ammount <= 0:
            raise ValueError("Ammount must be non negative and non zero value.")
        return ammount
    except ValueError as e:
        print(e)
        return get_ammount()


def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense.): ")

    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid Category.")
    return get_category()

def get_description():
    des = input("Enter a description (optional): ")
    return des 