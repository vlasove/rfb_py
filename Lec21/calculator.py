def add(a, b):
    return a + b

def sub(a,b):
    return a-b

def main():
    """
    Основная точка входа в программу
    """
    a_arg = int(input())
    b_arg = int(input())

    result = add(a_arg, b_arg) ** 2 - sub(a_arg, b_arg) ** 3
    print(result)

if __name__ == '__main__':
    main()