# Пример записи в файл. Ч.2. Перезапись. Несколько строк
from typing import List


def build_lines_to_file(lines:List[str]) -> List[str]:
    """
    Добавляет символ переноса на новую строку всем
    стркоам списка, кроме последней
    """
    for i in range(len(lines)):
        if i != len(lines) - 1:
            lines[i] += "\n"
    return lines

LINES = ["First line", "Second line", "Last line"]
fh = open("output.txt", "w")
fh.writelines(build_lines_to_file(LINES)) # ["First line\n", "Second line\n", "Last line"]
# Или проще
# fh.writelines("\n".join(LINES).strip())
fh.close()