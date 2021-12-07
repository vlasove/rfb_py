# Пример записи в файл. Ч.1. Перезапись
fh = open("output.txt", "w")
value = 29010
fh.write(f"This is my line {value}")
fh.close()