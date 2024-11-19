import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def sort_files(folder_path):
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return

    try:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                # Get file extension and create a subfolder
                file_extension = file.split('.')[-1].lower() if '.' in file else "No Extension"
                destination_folder = os.path.join(folder_path, file_extension)

                # Create the subfolder if it doesn't exist
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file to the corresponding subfolder
                shutil.move(file_path, os.path.join(destination_folder, file))

        messagebox.showinfo("Success", "Files sorted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)


# Set up the GUI
root = tk.Tk()
root.title("File Sorter")

# Folder selection
folder_var = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

folder_label = tk.Label(frame, text="Folder:")
folder_label.grid(row=0, column=0, sticky="w")

folder_entry = tk.Entry(frame, textvariable=folder_var, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(frame, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Sort button
sort_button = tk.Button(frame, text="Sort Files", command=lambda: sort_files(folder_var.get()))
sort_button.grid(row=1, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
