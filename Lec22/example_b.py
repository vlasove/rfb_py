# Чтение из файла. Ч.2. Контекстный менеджер
file_name = "data.txt"

with open(file_name, "r") as fh:
    content = fh.read()
    print(content)
    print("Is readable?:", fh.readable())
    print("Is writeble:", fh.writable())
    
# Закрыт ли действительно?
print("Can read?:", fh.readable())