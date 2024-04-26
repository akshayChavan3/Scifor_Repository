import requests
import random
import tkinter as tk

# Define the URL of the API endpoint
url = "https://api.quotable.io/random"

# Send a GET request to the API endpoint
response = requests.get("https://api.quotable.io/random")


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()
    # Process the data as needed
    print(data)
else:
    # Print an error message if the request was unsuccessful
    print("Error:", response.status_code)

window = tk.Tk()
window.title("Random Quote Generator")
label = tk.Label(window, text=" ")
label.pack(pady=10)

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return data["content"]

def show_quote():
    quotes = get_quote()
    label.config(text=quotes)


button1 = tk.Button(window, text=" CLICK TO GET A RANDOM QUOTE", command=show_quote)
button1.pack()

window.mainloop()







