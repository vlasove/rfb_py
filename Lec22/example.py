# Код с логической ошибкой
COUNT = 10
result = 0

# Предполагаемая область с ошибкой - начало
for i in range(COUNT):
    result += i % 10 + i // 3 # +2 - ошибочное действие
# Конец области

print("Result:", result)