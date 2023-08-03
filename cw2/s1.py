import socket
import threading
import subprocess
import tkinter as tk

HOST = '127.0.0.1'
PORT = 1234

def run_program():
    try:
        subprocess.Popen(['python', r"C:\Users\anish\OneDrive\Documents\sem 3\Algo2\cw2\c1.py"])
    except FileNotFoundError:
        print("Program not found.")


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
root.geometry("300x150")
root.configure(bg="black")
root.title("Server")

# ... (other GUI elements remain unchanged)
host_label = tk.Label(root, text=f"HOST: {HOST}", fg="white", bg="black")
host_label.pack()

port_label = tk.Label(root, text=f"PORT: {PORT}", fg="white", bg="black")
port_label.pack()

button = tk.Button(root, text="Add User", command=run_program, bg="green")
button.pack(side="bottom")

root.mainloop()
