# Множество - это НЕУПОРЯДОЧЕННАЯ коллекция, способная хранить УНИКАЛЬНЫЕ элементы 
# АБСОЛЮТНО ЛЮБОГО ТИПА.

# Инициализация
num_set = set() # Получили пустое множество!
print("This is my set:", num_set)

# Добавление элемента во множество
num_set.add(150) # Метод add(val) - добавить val во множество
num_set.add(120)
num_set.add(12.5)
num_set.add(10**6)
num_set.add(150)
num_set.add(150)
num_set.add("Vasya")
num_set.add(None)

print("Set after x4 add:", num_set) # Порядок элементво во множестве неизвестен никому


# Длина множества
print("Len of set:", len(num_set))

# Проверка вхождения элемента во множество?
to_search = 149
if to_search in num_set:
    print(f"{to_search} in set")
else:
    print(f"{to_search} not in set")