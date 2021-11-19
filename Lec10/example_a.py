# Длина множества
a_set = set([10,15.5, 20, 30, 30])
print("Len :", len(a_set))

# Сумма элементов множества
print("Sum:", sum(a_set))

# Min/Max
print("Min:", min(a_set))
print("Max:", max(a_set))

# Перебор элементов
# for var in iterator:
#     body

# Удаление элементов (по значению)
to_delete = 10
if to_delete in a_set:
    a_set.remove(to_delete)


# Удаление случайного
res = a_set.pop()
print("Deleted elem via pop():", res)

for elem in a_set:
    print("Elem:", elem)


# Добавим множество во множество  - невозможно
b_set = set([1, 2, 3, "hello kitty :3"])
a_set.add(b_set)
print("Total a_set:", a_set)