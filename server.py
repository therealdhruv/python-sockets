import socket


def server_program():
    host = socket.gethostname()
    port = 6000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("\nConnection from: " + str(address))

    # Step 1: Receive the string from the client
    data = conn.recv(1024).decode()
    print("\nReceived string from client: " + str(data))

    # Step 2: Receive 'n' number of integers from the client
    n = int(conn.recv(1024).decode())
    print("The number of integers from client : {}".format(n))

    integers = []
    for i in range(n):
        num = int(conn.recv(1024).decode())
        integers.append(num)
        print("\nReceived integer from client: {}".format(num))

    # Step 3: Compute PN and NN
    pn = sum([x for x in integers if x > 0])
    nn = sum([x for x in integers if x < 0])
    print("\nComputed PN: {}, NN: {}".format(pn, nn))
    print("\n")

    # Step 4: Send PN and NN to the client
    conn.send(str(pn).encode())
    conn.recv(1024)  # Receive acknowledgment from the client
    conn.send(str(nn).encode())

    conn.close()


if __name__ == '__main__':
    server_program()
