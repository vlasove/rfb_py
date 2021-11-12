# Задача В. Валидатор
login = input()
email = input()

if len(login) < 10 or "@" in login:
    print("Некорректный логин")
elif not ("@" in email and  "." in email):
    print("Некорректная почта")
else:
    print("ОК")