# Пример записи в файл. Ч.4. Дозапись нескольких строк
LINES = ["New line 1", "New line 2"]

fh = open("output.txt", "a")

fh.write("\n")
fh.writelines("\n".join(LINES).strip())

fh.close()