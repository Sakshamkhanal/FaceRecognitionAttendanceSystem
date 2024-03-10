import tkinter as tk
import cv2
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# Firebase initialization
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://faceattendancev2-ac026-default-rtdb.firebaseio.com/"})

# Function to add student information to Firebase
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
        student_id: {
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
    clear_entries()

    # Provide feedback to the user that data has been added
    status_label.config(text="Data added successfully!")

# Function to clear entry fields
def clear_entries():
    student_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    major_entry.delete(0, tk.END)
    starting_year_entry.delete(0, tk.END)
    total_attendance_entry.delete(0, tk.END)
    standing_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

# Function to show camera feed
def show_frame():
    # Capture frame from the camera
    ret, frame = cap.read()

    # Check if the frame is read correctly
    if ret:
        # Resize the frame
        resized_frame = cv2.resize(frame, (720, 360))

        # Convert the frame from OpenCV BGR format to RGB format
        rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a format that Tkinter can display
        img = Image.fromarray(rgb_frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the label with the new frame
        label.imgtk = imgtk
        label.config(image=imgtk)

    # Repeat the process after 10 milliseconds
    label.after(10, show_frame)

# Function to capture image
def capture_image():
    # Capture frame from the camera
    ret, frame = cap.read()

    # Check if the frame is read correctly
    if ret:
        # Resize the frame
        resized_frame = cv2.resize(frame,(216,216))

        # Save the frame to a file
        filename = 'captured_image.jpg'
        cv2.imwrite(filename, resized_frame)
        print("Image captured and saved as:", filename)

# Initialize Tkinter
root = tk.Tk()
root.title("Camera Feed & Student Information")

# Set the size of the Tkinter window
root.geometry("800x500")

# Set background color
root.configure(bg="#913f92")

# Create a label to display the camera feed
label = tk.Label(root)
label.pack()

# Access the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Start showing frames from the camera
show_frame()

# Create input fields for student information
tk.Label(root, text="StudentID:").pack()
student_id_entry = tk.Entry(root)
student_id_entry.pack()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Major:").pack()
major_entry = tk.Entry(root)
major_entry.pack()

tk.Label(root, text="Starting Year:").pack()
starting_year_entry = tk.Entry(root)
starting_year_entry.pack()

tk.Label(root, text="Total Attendance:").pack()
total_attendance_entry = tk.Entry(root)
total_attendance_entry.pack()

tk.Label(root, text="Standing:").pack()
standing_entry = tk.Entry(root)
standing_entry.pack()

tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Create a button to add data to Firebase
add_button = tk.Button(root, text="Add Student", command=add_to_database)
add_button.pack(pady=10)

# Create a button to capture an image
capture_button = tk.Button(root, text="Capture Image", command=capture_image, bg="grey", padx=10, pady=5)
capture_button.pack(pady=10)

# Optional label to show status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the Tkinter event loop
root.mainloop()

# Release the camera
cap.release()
