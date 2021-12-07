# Чтение из файла. Ч.4. Декомпозиция

from io import TextIOWrapper
import os
from typing import Union


FILE_NAME = "data.txt"

def open_file(file_name:str, mode:str="r") -> Union[TextIOWrapper, None]:
    """
    Проверяет что файл существует и возвращает Wrapper,
    в противном случае - возвращает None
    """

    if os.path.isfile(file_name):
        return open(file_name, mode)
    return None

def close_file(wrapper:TextIOWrapper) -> None:
    wrapper.close()


def main() -> None:
    wrapper = open_file(FILE_NAME, "r")
    lines = wrapper.readlines()
    
    for line in lines:
        print(f"Line : {line.strip()}")

    close_file(wrapper)

if __name__ == "__main__":
    main()