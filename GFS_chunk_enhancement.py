import socket
import threading

chunks = {}  # chunk_id to data

def handle_client(conn, addr):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command, *args = data.split()
            if command == 'STORE':
                chunk_id, data = int(args[0]), args[1]
                chunks[chunk_id] = data
                conn.sendall(b'Data stored')
            elif command == 'RETRIEVE':
                chunk_id = int(args[0])
                data = chunks.get(chunk_id, 'No data')
                conn.sendall(data.encode())
            elif command == 'PING':
                conn.sendall(b'PONG')
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

def main():
    host = 'localhost'
    port = 5001
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Chunk server is running...")
    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
