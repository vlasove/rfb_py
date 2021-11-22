# Инициализация списка из 100 нулей
nums = [0] * 100

# Инициализаци 0..99
# Создать список, который представляет из себя следующий набор
# При переборе чисел от 0 до 99 если число четное - возвести его в квадрат и добавить
# если чеисло нечетное- в куб и добавить в список
nums = []
for i in range(100):
    if i % 2 ==0:
        nums.append(i ** 2)
    else:
        nums.append(i ** 3)

print(nums)


# Списочнoе выражение
# Создадим список от 0..99
nums = [i for i in range(100)] # [0, 1, 2, 3, 4, .... 99]
# [elem for elem in iter]
# iter -> итератор, по которому берутся значения
# elem (правый) -> переменная цикла
# elem (левый) -> что будет добавлено в список

# Создадим список только из четных чисел от 0..99
nums = [i for i in range(100) if i % 2 == 0]
# [elem for elem in iter if expression]
# Добавляется в список elem только тогда, когда expression == True

# Инициализаци 0..99
# Создать список, который представляет из себя следующий набор
# При переборе чисел от 0 до 99 если число четное - возвести его в квадрат и добавить
# если чеисло нечетное- в куб и добавить в список

nums = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(100)]
#[elem_a if expression else elem_b for elem in iter]
# если expression == True -> добавим в список elem_a
# если expression == Flase -> добавим в список elem_b
print(nums)

# Тернарный условный оператор
current_time = 13
action = "Wake Up and go to work" if current_time > 12 else "U can sleep"
# t = value_a if expression else value_b
# Переменной t будет присвоено значение value_a ЕСЛИ expression == True,
# в противном случае, переменной t будет присвоено значение value_b
print(action)