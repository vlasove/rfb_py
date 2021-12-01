# Рекурсивный факториал
def factorial(n):
    if n <= 1:
        # База - условие завершения
        return 1
    return factorial(n - 1) * n # Рекурсивный вызов

print(f"{999}! = {factorial(999)}")


"""
factorial(3)-|
             factorial(2) * 3
                        |
                        --|
                          factorial(1) * 2
                                    |
                                    --|
                                       1
"""