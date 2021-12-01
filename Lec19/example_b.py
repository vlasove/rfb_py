from typing import List


def mutate(nums: List[int], pred: int) -> List[int]:
    """
    Функция, которая увеличивает все элементы
    списка на значение pred
    nums : список целых чисел
    pred : целое число , на которое будут увеличиваться элементы списка
    результат : список такой же длины, но с измененными значениями
    """
    return [elem + pred for elem in nums]


print(mutate([20, 22, 33], 99))
