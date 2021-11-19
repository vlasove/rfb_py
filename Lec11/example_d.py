# Задача I. Игра в слова

first_word = input().lower() # Самое первое введенное слово

while True:
    second_word = input().lower() # Новое слово
    if first_word[-1] == second_word[0]: # Проверка между первым и новым словом
        first_word = second_word # Теперь самое первое слово - последнее введенное
        continue # Перехожу к новой итерации и повторяю проверки
    else:
        print(second_word) # Вывод последнего введенного слова
        break # Выход из цикла
