import pandas as pd  # For handling CSVs as DataFrames
import csv           # For low-level CSV writing
from datetime import datetime 
from data_entry import get_amount, get_category, get_date, get_description 

# Define a class to manage CSV operations
class CSV:
    # Class-level constant: file name to store finance data
    CSV_FILE = "finance_data.csv"
    
    # Class-level constant: the expected structure (columns) of the CSV file
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        """
        Ensures the CSV file exists. If not, creates a new one with the correct headers.
        """
        try:
            # Try to read the CSV file to see if it already exists
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If the file does not exist, create an empty DataFrame with column headers
            df = pd.DataFrame(columns=cls.COLUMNS)
            # Save it as a new CSV without writing the index column
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Adds a single entry (row) to the CSV file.
        """
        # Create a dictionary representing one row of data
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # Open the CSV file in append mode to add the new entry
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            # Create a CSV writer object using the correct fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            # Write the dictionary as a new row in the CSV
            writer.writerow(new_entry)
        
        # Confirmation message to the user
        print("Entry added successfully")

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default = True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

add()
