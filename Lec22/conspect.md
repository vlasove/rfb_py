# Лекция 22. Итоговое занятие

* Отладчик
* Принципы работы с файлами (`.txt`, `.json`, `.xlsx`)
* Исключения (обработка)

## 1. Отладчик
* **Отладка** - это процесс "построчного" (пошагового) выполнения кода с целью нахождения логических ошибок.

* В `python` существует встроенный отладчик (но он очень неудобный), поэтому будем пользоваться отладчиком графической среды, в которой пишем код. Для того, чтобы отладчик среды правильно кооперировался с интерпреттором/компилятор в ОС, необходимо:
    * 1. И интерпретатор и компилятор должны быть установлены таким образом, чтобы их местоположение было известно ОС на уровне переменных окружений (Python - ADD TO PATH, VSCODE - Add to Path)
    * 2. Нужно отконфигурировать среду, чтобы ей было известно хотя бы местоположение интерпретатора/компилятора. (VSCODE configs to debugger)

* Допусти имеется код следующего вида:
```
# Код с логической ошибкой
COUNT = 10
result = 0

for i in range(COUNT):
    result = i % 10 + i // 3 + 2 # +2 - ошибочное действие

print("Result:", result)
```

* Действие 1 - локализовать возможную область ошибки
* Действие 2 - простановка `breakpoints` на каждой строке кода в области ошибки
* Действие 3 - запускаем отладчик 
* Действие 4 - находим панель с значениями переменных
* Действие 5 - начинаем пошаговую проверку
* Действие 6 - исправляем ошибку и поворяем шаги 1-6 до тех пор, пока код не станет работать так, как нужно.


### 2. Принципы работы с файлами
#### 2.1 Текстовые файлы
* Текстовый файлы (`.txt`) - самый бесполезный формат фалйов сточки зрения внутренней структуры (в текстовых файлах она остутствует), но очень удобный, когда нужно просто сохранять набор какой-нибудь информации.

* Из файлов можно читать, их можно перезаписывать, в них можно ДОзаписывать.

##### Чтение из текстового файла
* open(...) - создает файл-дескриптор (Wrapper)
* .close() - закрывает дескриптор

* fh.read() - вычитывание всего файла целиком!
* fh.readline() - считывает одну строку, при последующем обращении будут пытаться считать следующую. Когда файл закончится - будет возвращать "".
* fh.readlines() - возвращает список строк. Каждая стркоа в списке - это отдельная строка текстового файла!


##### Запись (перезапись) в текстовый файл
* `open(file_path, mode="w")`
* `fh.write(str)`
* `fh.writelines(List[str])`


##### Запись (ДОзапись) в текстовый файл
* `open(file_path, mode="a")`
* `fh.write(str)`
* `fh.writelines(List[str])`