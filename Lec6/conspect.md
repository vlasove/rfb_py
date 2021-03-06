## Лекция 6. Циклы

Цикл - это повторяющийся (чаще всего) заранее известное количество раз БЛОК КОДА, или как минимум существует известная ситуация, когда повторение будет завершено.

Циклов в Python 2 штуки:
* `while` (`while-do`)
* `for` (`range-based-for`)

### 1. Цикл while
Чаще всего используется для реализации бесконечного цикла.

#### 1.1 Синтаксис:
```
while expression:
    body
```
* `expression` - логическое выражение 
* `body` - тело цикла, которое выполняет до тех пор, ПОКА верно `expression`

#### 1.2 Пример:
```
# Цикл while
i = 0 # Переменная цикла (внешеняяя переменная цикла, штука, вот та)

while i < 10: # Условное выражение
    print("Hello world!") # Тело
    print(f"Times : {i}") # Цикла
    i = i + 1  # Инкермент - увеличение переменной цикла

print("DONE")
```

#### 1.3 Терминальные фразы
* `break` - прерывание текущей итерации цикла и передача управления следующему блоку кода за циклом.

* `continue` - прерывание текущей итерации цикла и передача управления СЛЕДУЮЩЕЙ ИТЕРАЦИИ цикла.