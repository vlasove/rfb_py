# Задача S . Автобусы

to_park = set()
to_home = set()

while True:
    bus_num_str = input()
    if bus_num_str == "":
        break
    bus_num_int = int(bus_num_str)
    to_park.add(bus_num_int)

while True:
    bus_num_str = input()
    if bus_num_str == "":
        break
    bus_num_int = int(bus_num_str)
    to_home.add(bus_num_int)

intersect = to_home.intersection(to_park) # Номера автобусов туда-обратно
print(len(intersect)) # Количество автобусов