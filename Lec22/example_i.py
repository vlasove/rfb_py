# Пример записи в JSON. Ч.1. Сериализация и конвертация в строку
import json

DATA = {
    "name" : "Bob",
    "last_name" : "Petrov",
    "link" : "https://facebook.com/accounts/?user=14213413"
}


json_str = json.dumps(DATA, indent=4)
print(json_str)