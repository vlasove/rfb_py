# Целые числа
a_int = int(input()) # int("10")
b_int = int(input()) # int("20")

# Вывод в StdOut
print(a_int, b_int)
# Сам тип - команда type()
print("Type of a_int:", type(a_int))

# Сложение
sum_int = a_int + b_int
print("Sum:", sum_int)

# Вычитание
sub_int = a_int - b_int
print("Sub:", sub_int)


# Умножение
mult_int = a_int * b_int
print("Mult:", mult_int)

# Деление - всегда вещественное число возвращает
div_int = a_int / b_int
print("Div result 10/20:", div_int)
print("Div result 20/10:", b_int/a_int)


# Деление нацело (целочиесленное деление)
div_round_int = -4 // 3 
print("Div round -4 // 3:", div_round_int)


# Взятие остатка от деления
mod_int = 7 % 5
print("Mod of 35 by 12:", mod_int)


# Вовзведение в степень
pow_int = 2 ** 5 # 2 ^ 5
print("Val of 3^11:", pow_int)