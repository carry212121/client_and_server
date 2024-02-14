import socket
import threading

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print("\nReceived from client1:", data.decode())
        except ConnectionResetError:
            print("Server connection closed.")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

try:
    while True:
        try:
            message = input("You: ")
            if message:
                client_socket.send(message.encode())
        except EOFError:
            print("\nClosing client.")
            break
        except KeyboardInterrupt:
            print("\nClosing client.")
            break

except KeyboardInterrupt:
    print("\nClosing client.")
finally:
    client_socket.close()


