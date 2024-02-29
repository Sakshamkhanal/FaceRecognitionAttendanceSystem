import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancev2-ac026-default-rtdb.firebaseio.com/"
})


def add_to_database():
    # Get input values from the entry widgets
    student_id = student_id_entry.get()
    name = name_entry.get()
    major = major_entry.get()
    starting_year = starting_year_entry.get()
    total_attendance = total_attendance_entry.get()
    standing = standing_entry.get()
    year = year_entry.get()
    last_attendance_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Push the data to Firebase Realtime Database
    ref = db.reference('Students')
    data = {
        student_id : {
            "name": name,
            "major": major,
            "starting_year": starting_year,
            "total_attendance": total_attendance,
            "standing": standing,
            "year": year,
            "last_attendance_time": last_attendance_time
        }
    }
    for key, value in data.items():
        ref.child(key).set(value)

    # Clear the entry fields after pushing to the database
    student_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    major_entry.delete(0, tk.END)
    starting_year_entry.delete(0, tk.END)
    total_attendance_entry.delete(0, tk.END)
    standing_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

    # Optionally, provide feedback to the user that data has been added
    status_label.config(text="Data added successfully!")


# Create the Tkinter window
root = tk.Tk()
root.title("Add Student Information")

# Create input fields
tk.Label(root, text="StudentID:").grid(row=0, column=0)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Major:").grid(row=1, column=0)
major_entry = tk.Entry(root)
major_entry.grid(row=1, column=1)

tk.Label(root, text="Starting Year:").grid(row=2, column=0)
starting_year_entry = tk.Entry(root)
starting_year_entry.grid(row=2, column=1)

tk.Label(root, text="Total Attendance:").grid(row=3, column=0)
total_attendance_entry = tk.Entry(root)
total_attendance_entry.grid(row=3, column=1)

tk.Label(root, text="Standing:").grid(row=4, column=0)
standing_entry = tk.Entry(root)
standing_entry.grid(row=4, column=1)

tk.Label(root, text="Year:").grid(row=5, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=5, column=1)

# Create a button to add data to Firebase
add_button = tk.Button(root, text="Add Student", command=add_to_database)
add_button.grid(row=6, column=0, columnspan=2)

# Optional label to show status
status_label = tk.Label(root, text="")
status_label.grid(row=7, column=0, columnspan=2)

root.mainloop()