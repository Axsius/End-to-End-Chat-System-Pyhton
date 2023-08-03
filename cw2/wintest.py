import tkinter as tk

def read_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            names = [name.strip() for name in file.readlines()]
        return names
    except FileNotFoundError:
        return []

def create_field_box(root, row, column, names):
    frame = tk.Frame(root, width=400, height=250, bd=1, relief=tk.SOLID, bg="#1A2226")
    frame.grid(row=row, column=column, padx=10, pady=10, sticky="n")

    frame.pack_propagate(False)

    listbox = tk.Listbox(frame, font=('Arial', 14), bg="#1A2226", fg="#ECF0F5", selectbackground="#222D32", selectforeground="#ECF0F5")
    listbox.pack(fill=tk.BOTH, expand=True)

    for name in names:
        listbox.insert(tk.END, name)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Two Field Boxes")
    root.geometry("900x550")
    root.config(bg="#1A2226")

    users_label = tk.Label(root, text="Users", font=('Arial', 18, 'bold'), bg="#222D32", fg="#ECF0F5")
    users_label.grid(row=0, column=0, pady=(20, 5), padx=20, sticky="ew")

    users = read_names_from_file("usernames.txt")
    create_field_box(root, row=1, column=0, names=users)

    groups_label = tk.Label(root, text="Groups", font=('Arial', 18, 'bold'), bg="#222D32", fg="#ECF0F5")
    groups_label.grid(row=0, column=1, pady=(20, 5), padx=20, sticky="ew")

    groups = read_names_from_file("groupname.txt")
    create_field_box(root, row=1, column=1, names=groups)

    root.mainloop()
