# Логический тип - определение
a_true = True
a_true = False # Под капотом - создается новая ячейка памяти, она ассоциируется с старым именем
# старая ячейка -уничтожается
b_false = False

print("Type:", type(a_true))

# Операции
print("True and False:", a_true and b_false)
print("True or False:", a_true or b_false)
print("not True:", not a_true)

operations = not(a_true and (b_false or a_true))
print("Operations:", operations)

# Никогда так не делайте
# При выполнении арифметических операций над логическим типом
# логический тип НЕЯВНО приводится к целочиесленным значениям
# True => 1, False => 0
res = False - True ** (True + False)
print(res) # Что будет?