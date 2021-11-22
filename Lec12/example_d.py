# Добавление и удаление элементов
## Добавление в конец
nums = []
nums.append(10) # Добавляет значение в конец списка
nums.append(20) # Добавляет значение в конец списка

print(nums)

## Добавление в "середину"
nums = [10, 20, 30, 40]
nums.insert(0, 99999) # При вставке в несуществующий индекс - элемент будет добавлен в конец списка!
print("Nums:", nums)


## Удалeние из конца (первого с конца)
elem = nums.pop()
print("Elem after pop:", elem)
print("Nums after pop:", nums)


## Удаление по значению (первого попавшегося элемента)
if 30 in nums:
    nums.remove(30)

print("Nums agter remove:", nums)