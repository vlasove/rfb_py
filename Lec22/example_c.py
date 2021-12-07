# Чтение из файла. Ч.3. Декомпозиция

from io import TextIOWrapper


FILE_NAME = "data.txt"

def open_file(file_name:str, mode:str="r") -> TextIOWrapper:
    return open(file_name, mode)

def close_file(wrapper:TextIOWrapper) -> None:
    wrapper.close()


def main() -> None:
    wrapper = open_file(FILE_NAME, "r")
    
    id = 0
    line = wrapper.readline().strip()
    
    # Пример построчного считывания текстового файла
    while line:
        id += 1
        print(f"Line num: {id}, Line content: {line}")
        line = wrapper.readline().strip()

    close_file(wrapper)

if __name__ == "__main__":
    main()