import socket
import threading
import time
from threading import Lock

files = {}
chunk_locations = {}
next_chunk_id = 1
files_lock = Lock()
chunk_locations_lock = Lock()

def monitor_chunk_servers():
    while True:
        with chunk_locations_lock:
            for chunk_id, server in list(chunk_locations.items()):
                try:
                    host, port = server.split(':')
                    with socket.create_connection((host, int(port)), timeout=1) as s:
                        s.sendall(b'PING')
                        if s.recv(1024).decode() != 'PONG':
                            raise Exception("Failed to receive pong")
                except:
                    print(f"Chunk server {server} failed, removing...")
                    del chunk_locations[chunk_id]
        time.sleep(10)

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
                chunk_server = next(iter(chunk_locations.values()), 'localhost:5001')
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
    threading.Thread(target=monitor_chunk_servers, daemon=True).start()
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    main()
