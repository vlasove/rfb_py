# Задача F. Сериалы

n_serials = int(input())
m_serials_to_see = int(input())

serials = set()
# Наполняем множество сериалов на сервисе
for _ in range(n_serials):
    serials.add(input())
    
# Запрашиваем на просмотр m каких-то сериалов
for _ in range(m_serials_to_see):
    if input() in serials:
        print("ЕСТЬ")
    else:
        print("НЕТ В НАЛИЧИИ")