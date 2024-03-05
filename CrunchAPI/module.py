import socket, json

class Test:
    def __init__(self, host='127.0.0.1', port=80): 
        self.host = host
        self.port = port

    def fetch_data(self, url):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(f"GET {url} HTTP/1.1\r\nHost: {self.host}\r\nConnection: close\r\n\r\n".encode())
                response = b"".join(iter(lambda: s.recv(4096), b''))
            return json.loads(response.decode('utf-8').split('\r\n\r\n', 1)[1])
        except json.JSONDecodeError:
            return None

    def getTest(self, id):
        return self.fetch_data(f"/api/test/{id}")

    def getAllId(self):
        data = self.fetch_data("/api/tests")
        if data:
            return [item.get('id') for item in data]
        return None
    