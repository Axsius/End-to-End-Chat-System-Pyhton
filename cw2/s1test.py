import socket
import threading
import subprocess
import tkinter as tk

HOST = '127.0.0.1'
PORT = 1234

def run_user_program():
    try:
        subprocess.Popen(['python', r"C:\Users\anish\OneDrive\Documents\sem 3\Algo2\cw2\c1.py"])
    except FileNotFoundError:
        print("Program not found.")

def run_admin_program():
    try:
        subprocess.Popen(['python', r"C:\Users\anish\OneDrive\Documents\sem 3\Algo2\cw2\admints2.py"])
    except FileNotFoundError:
        print("Program not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def start_server():
    LISTENER_LIMIT = 5
    active_clients = []

    def listen_for_messages(client, username):
        while True:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                final_msg = username + '~' + message
                send_messages_to_all(final_msg)
            else:
                print(f"The message sent from client {username} is empty")

    def send_message_to_client(client, message):
        client.sendall(message.encode())

    def send_messages_to_all(message):
        for user in active_clients:
            send_message_to_client(user[1], message)

    def client_handler(client):
        while True:
            username = client.recv(2048).decode('utf-8')
            if username != '':
                active_clients.append((username, client))
                prompt_message = "SERVER~" + f"{username} added to the chat"
                send_messages_to_all(prompt_message)
                break
            else:
                print("Client username is empty")

        threading.Thread(target=listen_for_messages, args=(client, username)).start()

    def run_server():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server.bind((HOST, PORT))
            print(f"Running the server on {HOST} {PORT}")
        except:
            print(f"Unable to bind to host {HOST} and port {PORT}")

        server.listen(LISTENER_LIMIT)

        while True:
            client, address = server.accept()
            print(f"Successfully connected to client {address[0]} {address[1]}")
            threading.Thread(target=client_handler, args=(client,)).start()

    run_server()


 
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True  # Set the server thread as a daemon thread to close it when the main thread exits.
server_thread.start()



# Start the Tkinter program
root = tk.Tk()
root.geometry("300x450")
root.configure(bg="#336699")  # Set the fancy background color (you can change it to your preferred color)
root.title("Server")

host_label = tk.Label(root, text=f"HOST: {HOST}", fg="white", bg="#336699", font=("Tektur", 10))
host_label.pack()

port_label = tk.Label(root, text=f"PORT: {PORT}", fg="white", bg="#336699",  font=("Tektur", 10) )
port_label.pack()

button_frame = tk.Frame(root, bg="#336699")
button_frame.pack(side="bottom", pady=10, anchor="center")

admin_label = tk.Label(button_frame, text="Logged as", fg="white", bg="#336699", font=("Arial", 14))
admin_label.pack()

admin_button = tk.Button(button_frame, text="Admin", command=run_admin_program, bg="#0D5447", width=10, height=1, font=("Arial", 14))
admin_button.pack(pady=(0, 5), padx=50)

or_label = tk.Label(button_frame, text="or", fg="white", bg="#336699", font=("Arial", 14))
or_label.pack()

user_button = tk.Button(button_frame, text="User", command=run_user_program, bg="#0D5447", width=10, height=1, font=("Arial", 14))
user_button.pack(pady=(5, 0), padx=50)


root.mainloop()