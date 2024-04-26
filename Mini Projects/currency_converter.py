import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Dropdown for selecting the source currency
        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=5)
        self.from_currency_var = tk.StringVar()
        self.from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var)
        self.from_currency_combobox['values'] = ['USD', 'EUR', 'GBP', 'INR', 'AUD']  # Add more currencies as needed
        self.from_currency_combobox.grid(row=0, column=1, padx=10, pady=5)
        self.from_currency_combobox.current(0)

        # Dropdown for selecting the target currency
        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=5)
        self.to_currency_var = tk.StringVar()
        self.to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var)
        self.to_currency_combobox['values'] = ['USD', 'EUR', 'GBP', 'INR', 'AUD']  # Add more currencies as needed
        self.to_currency_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.to_currency_combobox.current(1)

        # Entry for entering the amount
        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=5)
        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # Button for performing the conversion
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

        # Label for displaying the result
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, columnspan=2, padx=10, pady=10)


def convert(self):
    amount_str = self.amount_entry.get()
    amount_str = amount_str.replace('$', '').strip()  # Remove dollar sign and leading/trailing whitespace
    try:
        amount = float(amount_str)
    except ValueError:
        self.result_label.config(text="Please enter a valid amount")
        return

    from_currency = self.from_currency_var.get()
    to_currency = self.to_currency_var.get()

    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(api_url)
        data = response.json()
        if response.status_code == 200:
            exchange_rate = data['rates'][to_currency]
            converted_amount = amount * exchange_rate
            self.result_label.config(
                text=f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
        else:
            self.result_label.config(text="Failed to fetch exchange rates")
    except Exception as e:
        self.result_label.config(text="An error occurred")


root = tk.Tk()
app = CurrencyConverterApp(root)
root.mainloop()



