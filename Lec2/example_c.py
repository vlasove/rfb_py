# Вывод нескольких значений за один print()
print("Bob", "likes", "Baseball")


# Вывод значений переменных
name = "Bob"
print("My name is:", name) # print("My names is:", "Bob")


# Вывод нескольких значений переменных
first_name = "Bob"
last_name = "Johnson"
age = "19"

print("Full info:", first_name, last_name, "and age:", age)

# Задача D
word1 = "имя"
word2 = "твое"
word3 = "мне"
word4 = "знакомо"

print(word1, word2, word3, word4)
print(word2, word3, word1, word4)
print(word3, word2, word4, word1)


# Использование форматированного вывода
job = "Engineer"
location = "Saratov"

print(job, " ", " ", location) # Engineer     Saratov
print(f"{job}     {location}")

child_name = "Vova Morriss"
age = "7"
hobby = "LEGO"

print(f"{child_name} is {age} y.o. and he likes         {hobby}")

# Смешение кавычек
author = "Л.Н.Толстой"
title = "Война и Мир"
print(f'Автор {author}, "{title}"')
print(f"Автор {author}, '{title}'")