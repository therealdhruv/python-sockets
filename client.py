import socket


def client_program():
    host = socket.gethostname()
    port = 6000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    # Step 1: Send a string to the server
    message = input("\nEnter a string to send to the server: ")
    client_socket.send(message.encode())

    # Step 2: Read 'n' and 'n' integers from the user
    n = int(input("Enter the number of integers to send: "))
    client_socket.send(str(n).encode())

    integers = []
    for i in range(n):
        num = int(input("\nEnter an integer: "))
        integers.append(num)
        client_socket.send(str(num).encode())

    # Step 3: Receive PN and NN from the server
    pn = client_socket.recv(1024).decode()
    print("\nReceived PN from server:", pn)
    client_socket.send(b"Acknowledged")  # Send acknowledgment to the server

    nn = client_socket.recv(1024).decode()
    print("Received NN from server:", nn, "\n")


    client_socket.close()


if __name__ == '__main__':
    client_program()
