import tkinter as tk
import subprocess

def execute_user_update():
    subprocess.Popen(["python3", "Userupdate.py"])

def execute_encode_generator():
    subprocess.Popen(["python3", "EncodeGenerator.py"])

def execute_main():
    subprocess.Popen(["python3", "main.py"])

root = tk.Tk()
root.title("Execute Files")

button_user_update = tk.Button(root, text="Userupdate", command=execute_user_update)
button_user_update.pack(pady=10)

button_encode_generator = tk.Button(root, text="EncodeGenerator", command=execute_encode_generator)
button_encode_generator.pack(pady=10)

button_main = tk.Button(root, text="Take attendance", command=execute_main)
button_main.pack(pady=10)

root.mainloop()
