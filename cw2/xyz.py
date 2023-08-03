import tkinter as tk
from tkinter import ttk
import unittest

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
    # Remove the login widgets
    login_box.grid_forget()

    # Create the frame to display users
    users_frame = ttk.Frame(root, padding=20, style="TFrame")
    users_frame.grid(row=0, column=0, sticky="nsew")

    # Create the frame to display groups
    groups_frame = ttk.Frame(root, padding=20, style="TFrame")
    groups_frame.grid(row=0, column=1, sticky="nsew")

    # Add widgets to the users_frame and groups_frame (Dummy data for illustration)
    users_label = ttk.Label(users_frame, text="Users", font=("Arial", 20, "bold"))
    users_label.pack()

    users_list = ttk.Label(users_frame, text="John Doe\nJane Smith\nMichael Johnson\nEmily Brown")
    users_list.pack()

    groups_label = ttk.Label(groups_frame, text="Groups", font=("Arial", 20, "bold"))
    groups_label.pack()

    groups_list = ttk.Label(groups_frame, text="Group A\nGroup B\nGroup C\nGroup D")
    groups_list.pack()

def show_login_error():
    login_error_label.grid(row=4, column=0, columnspan=2, pady=10)

# Create the main tkinter window
root = tk.Tk()
root.title("Admin Panel")
root.geometry("1000x600")  # Set the window size

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TLabel", background="#1A2226", foreground="#ECF0F5", font=("Roboto", 12))
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
username_label = ttk.Label(login_box, text="USERNAME",font=("Arial", 14) )
username_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

username_entry = ttk.Entry(login_box, font=("Tektur", 14))
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = ttk.Label(login_box, text="PASSWORD", font=("Arial", 14))
password_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)

password_entry = ttk.Entry(login_box, show="*", font=("Tektur", 14))
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the login button
login_button = ttk.Button(login_box, text="LOGIN", command=show_admin_panel)
login_button.grid(row=3, column=0, columnspan=2, pady=15)

# Create a label to display login error message
login_error_label = ttk.Label(login_box, text="Invalid username or password.", foreground="red")

# Create the admin panel buttons, initially hidden
users_button = ttk.Button(root, text="Users")
groups_button = ttk.Button(root, text="Groups")


# Set the weight of the rows and columns to make the widgets expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
login_box.grid_rowconfigure(0, weight=1)
login_box.grid_rowconfigure(3, weight=1)
login_box.grid_columnconfigure(0, weight=1)
login_box.grid_columnconfigure(1, weight=1)

class TestAdminPanel(unittest.TestCase):

    def test_login_with_correct_credentials(self):
        username_entry.insert(0, "admin")
        password_entry.insert(0, "admin")
        login_button.invoke()
        self.assertEqual(users_button.grid_info()["row"], 0)
        self.assertEqual(groups_button.grid_info()["row"], 1)

    def test_login_with_incorrect_credentials(self):
        username_entry.insert(0, "wronguser")
        password_entry.insert(0, "wrongpass")
        with self.assertRaises(AssertionError):  # Check for AssertionError in unittests
            login_button.invoke()


# Run the main tkinter event loop
if __name__ == "__main__":
    root.mainloop()
