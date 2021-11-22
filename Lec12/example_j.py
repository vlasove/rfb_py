# Вырезание строк
# ["vasya", "petya"]
word = " \t\tVasya       \n".strip()
print("Word agter strip:", word)
print("Len :", len(word))


input().strip() # Отбрасывание слева и справа от строки пробельных символов
input().lstrip() # Отбрасывание слева
input().rstrip() # Отбрасывание справа