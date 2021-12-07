# Чтение текстового файла . Ч.1
fh = open("data.txt", "r") # path_to_file, mode
print("Fh type:", type(fh))
print("Fh content:", fh)

# Вычитать все содержимое и вернуть 1 большую строку
content = fh.read()
print(content)

# Закрыть файл-дескриптор
fh.close()