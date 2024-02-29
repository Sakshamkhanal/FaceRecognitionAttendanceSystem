import tkinter as tk
from tkinter import filedialog
import subprocess


def run_files():
    # Get the selected files
    selected_files = listbox.curselection()
    if not selected_files:
        return

    # Get the file path of the selected file
    index = selected_files[0]  # For SINGLE selectmode
    file_path = listbox.get(index)

    # Run the selected file
    subprocess.Popen(["python3", file_path])


def browse_files():
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()

    # Add selected file to the listbox
    if file_path:
        listbox.insert(tk.END, file_path)


# Initialize Tkinter
root = tk.Tk()
root.title("Run Single File")

# Create a frame to contain the listbox and buttons
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a listbox to display selected file
listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
listbox.pack(fill=tk.BOTH, expand=True)
listbox.files = []  # To keep track of file paths

# Create a button to browse files
browse_button = tk.Button(frame, text="Browse File", command=browse_files)
browse_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button to run selected file
run_button = tk.Button(frame, text="Run Selected File", command=run_files)
run_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
