import tkinter as tk
import json
import requests
import quote_app

# Define the URL you want to make a GET request to
url = "https://api.quotable.io/random"

# Make the GET request
response = requests.get("https://api.quotable.io/random")


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (the data returned by the server)
    print(response.text)
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote")
        self.root.configure(bg="blue")  # Set background color to blue

        self.label = tk.Label(root, text="Click the button to get a random quote!", font=("Helvetica", 14), bg="blue", fg="white")
        self.label.pack(pady=10)

        self.quote_text = tk.Text(root, height=5, width=50, wrap=tk.WORD, font=("Helvetica", 12))
        self.quote_text.pack(pady=10)

        self.button = tk.Button(root, text="Get Quote", command=self.get_quote, bg="white", fg="blue")
        self.button.pack(pady=5)

    def get_quote(self):
        try:
            response = requests.get("https://api.quotable.io/random")
            data = response.json()

            if 'content' in data and 'author' in data:
                content = data['content']
                author = data['author']
                self.display_quote(content, author)
                self.save_quote(data)
            else:
                self.display_error("Failed to retrieve quote data")
        except Exception as e:
            self.display_error(f"An error occurred: {str(e)}")

    def display_quote(self, content, author):
        self.quote_text.delete(1.0, tk.END)
        self.quote_text.insert(tk.END, f"\"{content}\" - {author}")

    def display_error(self, message):
        self.quote_text.delete(1.0, tk.END)
        self.quote_text.insert(tk.END, message)

    def save_quote(self, quote_data):
        with open('quotes.json', 'a') as f:
            json.dump(quote_data, f)
            f.write('\n')

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
