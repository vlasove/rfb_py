# Пустой список
a_list = []
b_list = list()

print("A_list:", len(a_list))
print("B_list:", len(b_list))


# Список с значениями
numerics = [1, 2, 3, 5, 6, 7, 1, 2, -2, "Hello", "World", True, None]
print("Len:", len(numerics))
print("Numerics:", numerics)


# Индексация и срезы
words = ["a", "b", "c", "d"]
print("First:", words[0])
print("Last:", words[-1])

print("Slice:", words[0:3:1])

# Длина списка
print("Len:", len(words))


# Проверка вхождения
if "c" in words: # Проверка вхождения ЭЛЕМЕНТА "c" в список ["a", "b", "c", "d"]
    print("c in words")
else:
    print("c not in words")


# Итерирование через индекс
for i in range(len(words)):
    print(f"id: {i}, elem: {words[i]}")


# Итерирование через элементы
for elem in words:
    print("Elem:", elem)