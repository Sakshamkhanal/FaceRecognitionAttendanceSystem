import tkinter as tk
from tkinter import ttk
import json


class StudentInfoApp:
    def __init__(self, master, file_path):
        self.master = master
        self.master.title("Student Information")

        # Load data from JSON file
        self.data = self.load_data_from_json(file_path)

        # Create card boxes to display data
        self.create_card_boxes()

    def load_data_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def create_card_boxes(self):
        # Create a container frame for card boxes
        self.card_container = ttk.Frame(self.master)
        self.card_container.pack(padx=10, pady=10)

        # Create card boxes for each data entry
        for key, value in self.data.items():
            card_frame = ttk.Frame(self.card_container, borderwidth=2, relief="groove")
            card_frame.pack(side="left", padx=10, pady=10)

            # Display key and value in the card box
            key_label = ttk.Label(card_frame, text=key, font=("Arial", 12, "bold"))
            key_label.pack(pady=(10, 0))

            value_label = ttk.Label(card_frame, text=value, font=("Arial", 12))
            value_label.pack(pady=(0, 10))


def main():
    # Path to the JSON file
    file_path = "data.json"

    # Create Tkinter root window
    root = tk.Tk()

    # Create instance of StudentInfoApp
    app = StudentInfoApp(root, file_path)

    # Run Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
