import tkinter as tk
import os
from google.cloud import datastore

# Set the path to your service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./serviceAccountKey.json"

# Initialize Datastore client
datastore_client = datastore.Client()



def fetch_data_from_datastore():
    # Fetch data from Datastore
    query = datastore_client.query(kind='321654')  # Replace 'Students' with your kind name
    docs = list(query.fetch())

    # Iterate over documents and extract data
    data = []
    for doc in docs:
        entity_data = doc.to_dict()
        entity_data['id'] = doc.id
        data.append(entity_data)

    return data

def display_data():
    # Fetch data from Datastore
    data = fetch_data_from_datastore()

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Datastore Data")

    # Display data in a Tkinter listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Insert data into the listbox
    for item in data:
        listbox.insert(tk.END, item)

    # Run the Tkinter event loop
    root.mainloop()

# Call the display_data function to fetch data from Datastore and display it using Tkinter
display_data()

