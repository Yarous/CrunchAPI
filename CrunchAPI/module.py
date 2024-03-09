import socket, json

class Test:
    def __init__(self, host='127.0.0.1', port=80): self.host, self.port = host, port

    def fetch_data(self, url):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.host, self.port))
                request = f"GET {url} HTTP/1.1\r\nHost: {self.host}\r\nConnection: close\r\n\r\n".encode()
                s.sendall(request)
                response = b"".join(iter(lambda: s.recv(4096), b''))
                return json.loads(response.decode().split('\r\n\r\n', 1)[1])
            except: return None

    def getTest(self, id): return self.fetch_data(f"/api/test/{id}")

    def getAllId(self): return [item.get('id') for item in self.fetch_data("/api/tests") or []]

    def addTest(self, testInfo):
        if not isinstance(testInfo, dict): return ValueError("The argument passed is not a dict")        
        if "description" in testInfo and "questions" in testInfo:
            if isinstance(testInfo["questions"], list) and all(
                "question_text" in q and "answers" in q and isinstance(q["answers"], list) 
                and all("answer_text" in a and "is_correct" in a for a in q["answers"]) for q in testInfo["questions"]
            ):
                try:
                    data_string = json.dumps(testInfo) 
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((self.host, self.port))
                        s.sendall(f"POST /api/addtest HTTP/1.1\r\nHost: {self.host}\r\nContent-Type: application/json\r\nContent-Length: {len(data_string)}\r\n\r\n{data_string}".encode())
                        return b"".join(iter(lambda: s.recv(4096), b'')).decode().split('\r\n\r\n', 1)[1]
                except Exception as e: return str(e)
            else: return ValueError("JSON structure does not match the expected format")
        else: return ValueError("JSON structure does not match the expected format")



# Пример использования
li = {
    "description": "asd",
    "questions": [
        {
            "answers": [
                {
                    "answer_text": "df",
                    "is_correct": "true"
                },
                {
                    "answer_text": "das",
                    "is_correct": "false"
                },
                {
                    "answer_text": "s",
                    "is_correct": "false"
                },
                {
                    "answer_text": "d",
                    "is_correct": "false"
                },
                {
                    "answer_text": "d",
                    "is_correct": "false"
                }
            ],
            "question_text": "asd"
        }
    ],
    "testname": "liquor"
}

test = Test()
print(test.addTest(li))