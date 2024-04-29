import socket
import threading
from threading import Lock

files = {}
chunk_locations = {}
next_chunk_id = 1
files_lock = Lock()
chunk_locations_lock = Lock()

def handle_client(conn, addr):
    global next_chunk_id
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        command, *args = data.split()
        if command == 'CREATE':
            file_name = args[0]
            with files_lock:
                if file_name in files:
                    response = 'File already exists'
                else:
                    files[file_name] = []
                    response = 'File created'
            conn.sendall(response.encode())
        elif command == 'WRITE':
            file_name = args[0]
            with files_lock, chunk_locations_lock:
                chunk_id = next_chunk_id
                next_chunk_id += 1
                files[file_name].append(chunk_id)
                chunk_server = 'localhost:5001'  # Ensuring the format is correct
                chunk_locations[chunk_id] = chunk_server
                response = f'{chunk_id} {chunk_server}'.encode()
            conn.sendall(response)

        elif command == 'READ':
            file_name = args[0]
            response = ''
            with files_lock:
                for chunk_id in files.get(file_name, []):
                    with chunk_locations_lock:
                        chunk_server = chunk_locations.get(chunk_id)
                        response += f'{chunk_id} {chunk_server} '
            conn.sendall(response.encode())

def main():
    host = 'localhost'
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Master server is running...")
    chunk_locations[1] = 'localhost:5001'  # Example: Simulate a chunk server registration
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    main()
