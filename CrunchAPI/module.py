import socket

def simple_http_get(host, path="/"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, 80))  # Подключение к порту 80 сервера
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.send(request.encode())  # Отправка HTTP-запроса

        # Получение и объединение всех частей ответа
        response = b''
        while True:
            part = s.recv(1024)
            if not part:
                break
            response += part

    # Преобразование байт в строку и возврат содержимого (после заголовков)
    return response.decode().split('\r\n\r\n', 1)[1]

def naive_json_parse(json_str):
    """
    Очень примитивный парсер JSON. Предполагает, что json_str - это простой объект вида {"ключ": "значение"}.
    Только для демонстрации и не должен использоваться для реального парсинга JSON!
    """
    try:
        # Простейший парсинг: удаляем скобки, делим по запятым, затем по двоеточиям
        json_str = json_str.strip()[1:-1]  # Удаление открывающей и закрывающей скобки
        json_items = json_str.split(',')
        json_dict = {}
        for item in json_items:
            key, value = item.split(':')
            key = key.strip('" ')
            value = value.strip('" ')
            json_dict[key] = value
        return json_dict
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return {}

host = 'example.com'
path = '/api/tests'
response_body = simple_http_get(host, path)
parsed_json = naive_json_parse(response_body)
print(parsed_json)