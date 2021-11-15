# Задача К. Космическая программа

count = 0 # Счетчик отобранных кандидатов
lhs = 100
rhs = 140 
pulse_max = -1
pulse_min = 1000

while True:
    pulse = float(input())
    if pulse < 0:
        break

    if lhs <= pulse and pulse <= rhs:
        count += 1

        if pulse > pulse_max:
            pulse_max = pulse

        if pulse < pulse_min:
            pulse_min = pulse

print(count)
print(pulse_min, pulse_max)
