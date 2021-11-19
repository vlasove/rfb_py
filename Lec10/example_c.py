# Методы множеств *_update
a_set = set([1,2,3])
b_set = set([2,3,4,5])

c_set = a_set.intersection(b_set)
a_set.intersection_update(b_set)
print("A set:", a_set)
print("B_set:", b_set)
print("C set:", c_set)


# del c_set # Передать сборщику мусора объект