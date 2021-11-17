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