import socket, json
def fetch_and_parse_json(host, path="/", port=80):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode())
        response = b"".join(iter(lambda: s.recv(4096), b''))
    try: return json.loads(response.decode('utf-8').split('\r\n\r\n', 1)[1])
    except json.JSONDecodeError: return None

print(fetch_and_parse_json('127.0.0.1', '/api/tests'))