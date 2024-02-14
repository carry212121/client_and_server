import socket
import threading

def handle_client(client_socket, client_address, client_id):
    print(f"Connected: {client_address} as Client {client_id}")

    while True:

        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from Client {client_id}: {data.decode()}")
            

            other_client_socket = client1_socket if client_id == 2 else client2_socket
            other_client_socket.send(data)
        except ConnectionResetError:
            print(f"Client {client_id} Disconnected.")
            break

    print(f"Disconnected: {client_address} as Client {client_id}")
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(2)  # Maximum 2 clients

print("Server is listening for connections...")

client1_socket, client1_address = server_socket.accept()
print(f"Client 1 connected: {client1_address}")
client2_socket, client2_address = server_socket.accept()
print(f"Client 2 connected: {client2_address}")


client1_thread = threading.Thread(target=handle_client, args=(client1_socket, client1_address, 1))
client1_thread.start()

client2_thread = threading.Thread(target=handle_client, args=(client2_socket, client2_address, 2))
client2_thread.start()

while True:
    pass