# Задача P. Кулинар
n_dishes = int(input().strip())
dishes = []

for _ in range(n_dishes):
    dishes.append(input().strip())

n_days = int(input().strip())

for _ in range(n_days):
    m_dishes_per_day = int(input().strip())
    for _ in range(m_dishes_per_day):
        current_dish = input().strip()
        if current_dish in dishes:
            dishes.remove(current_dish)

for dish in sorted(dishes):
    print(dish)