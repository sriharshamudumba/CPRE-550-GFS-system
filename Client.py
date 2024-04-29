import socket

def main():
    master_server = ('localhost', 5000)

    # Create a file via Master
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(master_server)
        sock.sendall(b'CREATE testfile.txt')
        print(sock.recv(1024).decode())

        # Write data to a file via Master and then to Chunk Server
        sock.sendall(b'WRITE testfile.txt')
        response = sock.recv(1024).decode().split()
        chunk_id, chunk_addr = response[0], response[1]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as chunk_sock:
            chunk_server_address = ('localhost', int(chunk_addr.split(':')[1]))
            chunk_sock.connect(chunk_server_address)
            chunk_sock.sendall(f'STORE {chunk_id} HelloGFS'.encode())
            print(chunk_sock.recv(1024).decode())

        # Read the file data via Master and then from Chunk Server
        sock.sendall(b'READ testfile.txt')
        response = sock.recv(1024).decode().strip().split()
        for i in range(0, len(response), 2):
            chunk_id, chunk_addr = response[i], response[i+1]
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as chunk_sock:
                chunk_server_address = ('localhost', int(chunk_addr.split(':')[1]))
                chunk_sock.connect(chunk_server_address)
                chunk_sock.sendall(f'RETRIEVE {chunk_id}'.encode())
                print(chunk_sock.recv(1024).decode())

if __name__ == '__main__':
    main()
