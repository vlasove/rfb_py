# Накопление суммы/произведения
# Вводятся положительные целые числа - подсчитать сумму и произведение введенных
# Стоп-сигнал - любое отрицательное целое число

total_sum = 0
total_mult = 1

while True:
    numeric = int(input())
    if numeric < 0:
        break

    total_sum += numeric  # total_sum = total_sum + numeric
    total_mult *= numeric # total_mult = total_mult * numeric
    # total_pow **= 3         # total_pow = total_pow ** 3

    print("Current sum:", total_sum)
    print("Current mult:", total_mult)