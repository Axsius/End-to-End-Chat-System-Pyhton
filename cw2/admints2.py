import tkinter as tk
from tkinter import ttk
import unittest

users_frame = None  # Declare global variables for users_frame and groups_frame
groups_frame = None

def login():
    # Replace this function with your login logic
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        show_admin_panel()
    else:
        # Show the error message
        login_error_label.config(text="Invalid credentials")
        login_error_label.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        raise AssertionError("Invalid login credentials")  # Raise AssertionError for unittest


def show_admin_panel():
    global users_frame, groups_frame
    # Remove the login widgets
    login_box.grid_forget()

    # Create the admin panel frame
    admin_panel_frame.grid(row=0, column=0, sticky="nsew")

    # Create separate frames for users and groups
    global users_frame, groups_frame  # Declare them as global variables
    users_frame = ttk.Frame(admin_panel_frame, width=400, height=300)
    users_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    groups_frame = ttk.Frame(admin_panel_frame, width=400, height=300)
    groups_frame.grid(row=1, column=2, padx=10, pady=10, sticky="e")

    users_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    users_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    groups_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    groups_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
def show_login_error():
    login_error_label.grid(row=4, column=0, columnspan=2, pady=10)

# Create the main tkinter window
root = tk.Tk()
root.title("Admin Panel")
root.geometry("800x600")  # Set the window size

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TLabel", background="#1A2226", foreground="#0DB8DE", font=("Roboto", 12))
style.configure("TButton", background="#0DB8DE", foreground="#1A2226", font=("Roboto", 12))
style.configure("TEntry", fieldbackground="#1A2226", foreground="#1A2226")  # Set entry background and foreground color
style.configure("TFrame", background="#222D32")  # Set background color for login box

# Create the login box using ttk widgets
login_box = ttk.Frame(root, padding=20)
login_box.grid(row=0, column=0, sticky="nsew")

# Create the login key
login_key = ttk.Label(login_box, text="ADMIN PANEL", font=("Roboto", 30, "bold"))
login_key.grid(row=0, column=0, columnspan=2, pady=15)

# Create the username and password input fields
username_label = ttk.Label(login_box, text="USERNAME")
username_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

username_entry = ttk.Entry(login_box)
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = ttk.Label(login_box, text="PASSWORD")
password_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)

password_entry = ttk.Entry(login_box, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the login button
login_button = ttk.Button(login_box, text="LOGIN", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=15)

# Create a label to display login error message
login_error_label = ttk.Label(login_box, text="Invalid username or password.", foreground="red")


# Create the admin panel frame, initially hidden
admin_panel_frame = ttk.Frame(root, padding=20)

# Create the admin panel labels and entry widgets
users_label = ttk.Label(users_frame, text="Users")
users_entry = ttk.Entry(users_frame, width=50)  # Set the width of the entry field

groups_label = ttk.Label(groups_frame, text="Groups")
groups_entry = ttk.Entry(groups_frame, width=50)  # Set the width of the entry field

# Set the weight of the rows and columns to make the widgets expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
login_box.grid_rowconfigure(0, weight=1)
login_box.grid_rowconfigure(3, weight=1)
login_box.grid_columnconfigure(0, weight=1)
login_box.grid_columnconfigure(1, weight=1)

class TestAdminPanel(unittest.TestCase):
    def test_login_with_correct_credentials(self):
        show_admin_panel()  # Ensure the admin panel is created before running the test
        username_entry.insert(0, "admin")
        password_entry.insert(0, "admin")
        login_button.invoke()
        self.assertEqual(users_label.grid_info()["row"], 0)
        self.assertEqual(groups_label.grid_info()["row"], 1)

    def test_login_with_incorrect_credentials(self):
        show_admin_panel()  # Ensure the admin panel is created before running the test
        username_entry.insert(0, "wronguser")
        password_entry.insert(0, "wrongpass")
        with self.assertRaises(AssertionError):  # Check for AssertionError in unittests
            login_button.invoke()

# Run the main tkinter event loop
if __name__ == "__main__":
    root.mainloop()
