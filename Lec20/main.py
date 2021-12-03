# Главный модуль, попробуем из него обратиться к 
# объектам в sample.py
# import sample_with_timezones_at_rfb_database_greenplum_connector as conn
import sample

def add(a : int, b : int) -> int:
    """
    a^2 + b^2
    """
    return a ** 2 + b ** 2

numerics = [i * 100 for i in range(1, 10)]
MAX_VALUE = 3 ** 8

res = sample.add(10, 20)
print("res of add 10 and 20:", res)
print(sample.numerics)
print(sample.MAX_VALUE)

print("Current:", add(10, 20))
print(numerics)
print(MAX_VALUE)

# print("Connector:", conn.CONN)