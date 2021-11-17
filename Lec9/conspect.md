## Лекция 9. Коллекции в Python.

* `Коллекция` - это способ группировки разрозненных данных в одном месте.

В `Python` существует 5 встроенных коллекций:
* `set` - множество
* `str` - строка
* `list` - список
* `tuple` - кортеж
* `dict` - словарь



### 1. Множество. Инициализация и использование
* `Множество` - это **НЕУПОРЯДОЧЕННАЯ** коллекция, способная хранить **УНИКАЛЬНЫЕ** элементы **АБСОЛЮТНО ЛЮБОГО ТИПА**.

```
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

```

### 2. Методы множеств
```
# Пересечение множеств - это множество, содержащее общие элементы для двух других
# A n B = C

a_set = set([1,2,3,4,5])
b_set = set([3,4,5,6,7])

c_set = a_set.intersection(b_set) # Пересечение
print("Intersaction A n B:", c_set, type(c_set))


# Объединение множеств - это множество, содержащее в себе ВСЕ элементы обоих множеств
# A u B = C

d_set = a_set.union(b_set) # Объединение
print("Union A u B:", d_set)


# Вычитание множеств - это множество, содержащее в себе элементы одного множества,
# не входящее в другое
e_set = a_set.difference(b_set) # Вычитание
print("Difference A - B:", e_set)


# Симметрическая разность
sym_diff = a_set.union(b_set).difference(a_set.intersection(b_set))
print("Sym Diff:", sym_diff)
sym_diff_simple = a_set.symmetric_difference(b_set)
print("Sym Diff Simple:", sym_diff_simple)


# Сравнение множеств
if sym_diff == sym_diff_simple:
    print("Equal sets")
```