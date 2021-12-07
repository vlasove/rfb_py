# Пример записив XLSX файл
import xlsxwriter

DATA = (
    ["Water", 25],
    ["Cola", 37],
    ["Butter", 85],
    ["Bread", 15],
)

workbook = xlsxwriter.Workbook("sample.xlsx")
worksheet = workbook.add_worksheet()

row = 0
col = 0

for item, cost in DATA:
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Можно использовать формулы (только общепринятые, не локаль)
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()

