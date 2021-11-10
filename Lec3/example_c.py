# Строка - последовательность символов заключенная в пару однотипных кавычек.
# В Python строкой является все что угодно, помещенное в кавычки
# В Python все строки - юникод


# Считывание
message = input()

# Вывод в StdOut
print("Inputted message:", message)


# Взятие длины строки
len_of_message = len(message) # Количество символов в строке
print(f"Message has {len_of_message} symbols")

# Конкатенация
lhs = "asd"
rhs = "555"

print(lhs + rhs, rhs + lhs)
# Мультипликативная конкатенация - иммет смысл
# только для целых положительных чисел
msg = "Hello"
print(-10 * msg, "len of:", len(-10 * msg)) # -1 * "Hello" => ""
print(0 * msg, "len of:", len(0 * msg)) # 0 * "Hello" => ""
print(2 * msg, "len of:", len(2 * msg)) # 2 * "Hello" = > "HelloHello"


result = 500
result_str = f"{result}" # "500"
result_str_2 = str(500) # "500"

print(result_str + result_str_2)

#
value_float = 2345678.876545678491231
result_float = f"{value_float:.3f}"