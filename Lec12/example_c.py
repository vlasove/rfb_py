# Сравнение строк
first_word = "cat"
second_word = "d"

print(first_word < second_word)

# ord() 
print("Ord of 'a' is:", ord("a"))
print("Ord of 'b' is:", ord("b"))
print("Ord of 'A' is:", ord("A"))
print("Ord of 'B' is:", ord("B"))

# chr()
print("Chr of 123:", chr(99))

# Простой пример сравнения
print("a" > "A") # 97 > 65

# Пример сравнения слов из двух букв
print("abc" > "a")
# Сначала пытаются сравниться первые символы. Если они равны (равны их коды),
# то сравниваются вторые символы между собой и так далее, до тех пор, пока
# между двумя символами нельзя будет поставить знак > или <