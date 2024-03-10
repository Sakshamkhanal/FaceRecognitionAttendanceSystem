import tkinter as tk
import cv2
from PIL import Image, ImageTk


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
root.title("Camera Feed")

# Set the size of the Tkinter window
root.geometry("10x10")

# Set background color
root.configure(bg="#993299")

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

# Create a button to capture an image
capture_button = tk.Button(root, text="Capture Image", command=capture_image, bg="grey", padx=10, pady=5)
capture_button.pack(pady=10)
# Run the Tkinter event loop
root.mainloop()

# Release the camera
cap.release()
