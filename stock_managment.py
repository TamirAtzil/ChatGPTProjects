import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
import sqlite3

DATABASE_NAME = "stocks.db"

def create_database():
    """Initialize the database to store stock data."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stocks (date TEXT, amount INTEGER)''')
    connection.commit()
    connection.close()

def insert_stock(date, amount):
    """Insert stock data into the database."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO stocks (date, amount) VALUES (?, ?)''', (date, amount))
    connection.commit()
    connection.close()

def fetch_stocks():
    """Fetch all stock data from the database."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM stocks''')
    stocks = cursor.fetchall()
    connection.close()
    return stocks

def get_cisco_stock_price():
    """Get the current Cisco stock price from the internet using web scraping."""
    url = "https://finance.yahoo.com/quote/CSCO"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_tag = soup.find("span", {"data-reactid": "50"})
    return float(price_tag.text)

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cisco Stock Tracker")

        # Layout
        self.label_tax_rate = ttk.Label(root, text="Tax Rate:")
        self.label_tax_rate.grid(column=0, row=0)
        self.entry_tax_rate = ttk.Entry(root)
        self.entry_tax_rate.grid(column=1, row=0)

        self.label_date = ttk.Label(root, text="Future Date:")
        self.label_date.grid(column=0, row=1)
        self.entry_date = ttk.Entry(root)
        self.entry_date.grid(column=1, row=1)

        self.label_stocks = ttk.Label(root, text="Number of Stocks:")
        self.label_stocks.grid(column=0, row=2)
        self.entry_stocks = ttk.Entry(root)
        self.entry_stocks.grid(column=1, row=2)

        self.btn_add = ttk.Button(root, text="Add Future Stocks", command=self.add_stock)
        self.btn_add.grid(column=1, row=3)

        self.btn_calculate = ttk.Button(root, text="Calculate Value", command=self.calculate_stock_value)
        self.btn_calculate.grid(column=1, row=4)

        self.label_result = ttk.Label(root, text="Value:")
        self.label_result.grid(column=0, row=5)
        self.output_result = ttk.Label(root, text="0")
        self.output_result.grid(column=1, row=5)

    def add_stock(self):
        """Add stock data for future date."""
        date = self.entry_date.get()
        stocks = int(self.entry_stocks.get())
        insert_stock(date, stocks)
        self.entry_date.delete(0, tk.END)
        self.entry_stocks.delete(0, tk.END)

    def calculate_stock_value(self):
        """Calculate the current and future stock value."""
        stocks = fetch_stocks()
        current_price = get_cisco_stock_price()
        tax_rate = float(self.entry_tax_rate.get()) / 100

        total_stocks = sum([stock[1] for stock in stocks])
        value_before_tax = total_stocks * current_price
        value_after_tax = value_before_tax * (1 - tax_rate)

        self.output_result.config(text=f"Before Tax: ${value_before_tax:.2f} | After Tax: ${value_after_tax:.2f}")

if __name__ == "__main__":
    create_database()
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()
