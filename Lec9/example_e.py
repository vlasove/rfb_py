# Множество - это ссылочная коллекция
a_set = set([10, 20, 30])
b_set = a_set.copy() # Копирование содержимого по ссылке a_set

b_set.add(100)
b_set.add(99999999)

print("A_set:", a_set)
print('B_set:', b_set)