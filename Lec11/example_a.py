# Индексы в строках
message = 'Hello#World'
print("First letter:", message[0]) # Обращение к первому элементу строки!
print("Second letter:", message[1]) # Обращение ко второму элементу строки

# message[1000000000000] # Ошибка обращения по индексу
last_id = len(message) - 1
print("Last letter:", message[-1]) # message[len(message) - 1]
print("PreLast letter:", message[-2]) # message[len(message) - 2]


# Выделение подстроки
sub_message = message[0] + message[1] + message[2] + message[3] + message[4]
print("Sub Message:", sub_message)

# Синтаксис среза
# str[start:stop:step]
sub_message = message[0:5:1]
print("Sub Message (Slice):", sub_message)

# Шаг можно не указывать
sub_message = message[0:5]
print("Sub Message (slice) with default step=1:", sub_message)

# Срез от САМОГО начала до stop
sub_message = message[:5]
print("Sub Message (slice) from 0 id:", sub_message)


# Срез от какого-то элемента до САМОГО конца строки
print("Sub Message (slice) to end:", message[6:])


# Срез до конца с шагом в 2
print("Sub Message (slice) to end with step=2:", message[3::2])

# Разворот строки
print("Reversed:", message[::-1])


# Итерирование по индексу
for i in range(0, len(message), 2):
    print(f"id {i}, letter {message[i]}")

# Итерирование по самой строке
for letter in message[::2]:
    print("Letter:", letter)
