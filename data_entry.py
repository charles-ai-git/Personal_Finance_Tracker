from datetime import datetime

# Define the expected date format and the allowed categories
date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    """
    Prompt the user for a date and validate the input.
    If allow_default is True and no input is provided, return today's date.
    Re-prompts on invalid input.
    """
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    """
    Prompt the user to enter a positive, non-zero amount.
    Re-prompts on invalid input or non-numeric values.
    """
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    """
    Prompt the user to select a category: 'I' for Income, 'E' for Expense.
    Converts input to uppercase and validates it against allowed categories.
    Re-prompts on invalid input.
    """
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    """
    Prompt the user for an optional description.
    Returns the input as-is (can be empty).
    """
    return input("Enter a description (optional): ")

