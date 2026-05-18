# Lab 12:

import tkinter as tk
from tkinter import messagebox


class UserForm:

    def __init__(self, root):
        self.root = root
        self.root.title("User Form")
        self.root.geometry("400x400")

        # Labels and Entry fields
        tk.Label(root, text="Name").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Age").pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        tk.Label(root, text="City").pack()
        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        # Buttons
        tk.Button(root, text="Save", command=self.save_data).pack(pady=5)
        tk.Button(root, text="Display", command=self.display_data).pack(pady=5)
        tk.Button(root, text="Clear", command=self.clear_fields).pack(pady=5)

        # Text area to display records
        self.text_area = tk.Text(root, height=10, width=40)
        self.text_area.pack(pady=10)

    # Save data to file
    def save_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        city = self.city_entry.get()

        if name == "" or age == "" or city == "":
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            with open("users.txt", "a") as file:
                file.write(f"Name: {name}, Age: {age}, City: {city}\n")

            messagebox.showinfo("Success", "Data saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Display data from file
    def display_data(self):
        self.text_area.delete("1.0", tk.END)

        try:
            with open("users.txt", "r") as file:
                data = file.read()

            self.text_area.insert(tk.END, data)

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Clear input fields
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = UserForm(root)
    root.mainloop()