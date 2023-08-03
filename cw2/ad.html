# server.py
import socket

HOST = '127.0.0.1'
PORT = 1234

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Waiting for a connection...")
    conn, addr = server.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        username = data.decode()
        conn.sendall("Username processed".encode())  # Send a confirmation to the client
        # Here, you can call a function to update the admin_panel with the received username
        # For simplicity, we'll just print the username for demonstration purposes.
        print(f"Received username: {username}")
    conn.close()

if __name__ == '__main__':
    main()
