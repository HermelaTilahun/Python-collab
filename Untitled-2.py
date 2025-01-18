import tkinter as tk
from tkinter import messagebox
# Initialize the main application window
root = tk.Tk()
root.title("Student List Manager")
root.geometry("400x500")
# Initial list of student names
student_names = ['Muluken', 'Bethelhem', 'Samuel', 'Workneh']
# Function to update the list display
def update_display():
    listbox.delete(0, tk.END)  # Clear the listbox
    for student in student_names:
        listbox.insert(tk.END, student)  # Add each name to the listbox
# Function to add a new student
def add_student():
    new_student = name_entry.get().strip()
    if new_student:
        student_names.append(new_student)
        update_display()
        name_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"'{new_student}' has been added.")
    else:
        messagebox.showerror("Error", "Please enter a valid name.")
# Function to extend the list with multiple students
def extend_list():
    additional_names = extend_entry.get().split(',')
    additional_names = [name.strip() for name in additional_names if name.strip()]
    if additional_names:
        student_names.extend(additional_names)
        update_display()
        extend_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Added: {', '.join(additional_names)}")
    else:
        messagebox.showerror("Error", "Please enter valid names separated by commas.")
# Function to remove a selected student
def remove_student():
    try:
        selected_index = listbox.curselection()[0]
        removed_student = student_names.pop(selected_index)
        update_display()
        messagebox.showinfo("Success", f"'{removed_student}' has been removed.")
    except IndexError:
        messagebox.showerror("Error", "Please select a student to remove.")
# GUI Widgets
# Title
title_label = tk.Label(root, text="Student List Manager", font=("Arial", 16, "bold"))
title_label.pack(pady=10)
# Listbox to display students
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)
# Entry for adding a single student
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)
add_button = tk.Button(root, text="Add Student", font=("Arial", 12), command=add_student)
add_button.pack(pady=5)
# Entry for extending the list
extend_entry = tk.Entry(root, width=30, font=("Arial", 12))
extend_entry.pack(pady=5)
extend_button = tk.Button(root, text="Extend List", font=("Arial", 12), command=extend_list)
extend_button.pack(pady=5)
# Button to remove selected student
remove_button = tk.Button(root, text="Remove Selected Student", font=("Arial", 12), command=remove_student)
remove_button.pack(pady=10)
# Button to exit the application
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy, bg="red", fg="white")
exit_button.pack(pady=10)
# Initialize the display
update_display()
# Run the application
root.mainloop()
        