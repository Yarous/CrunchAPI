import socket, json

def getTest(id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 80))
            s.sendall(f"GET /api/test/{id} HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n".encode())
            response = b"".join(iter(lambda: s.recv(4096), b''))
        return json.loads(response.decode('utf-8').split('\r\n\r\n', 1)[1])
    except json.JSONDecodeError:  return None