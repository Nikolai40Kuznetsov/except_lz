import pandas as pd
import os
try:
    pd.read_csv("var6.csv")
except FileNotFoundError:
    print("Возникла следующая ошибка: Файл не найден")  
except pd.errors.EmptyDataError:
    print("Возникла следующая ошибка: Датафрейм пуст")
except pd.errors.ParserError:
    print("Возникла следующая ошибка: Количество столбцов с данными больше количества столбцов в датафрейме")    
file_columns = []
exemplar_columns = []
i = 0
j = 0
k = 0
file = pd.read_csv("var6.csv")
for column_name in file.columns:
    file_columns.append(column_name)
    i += 1
check = pd.read_csv("exemplar.csv")
for column_name in check.columns:
    exemplar_columns.append(column_name)
    j += 1
try:
    for column_name in check.columns:
        if column_name != file_columns[k]:
            raise ValueError
        k += 1
except ValueError:
    print("Структура датафрейма НЕ соотвествует ожидаемой:")
    print("- Названия столбцов не совпадают")
    print("Ожидаемые", exemplar_columns)
    print("Фактические", file_columns)
for column_name in file.columns:
    print(str(check[column_name].dtype))
for column_name in check.columns:
    print(str(check[column_name].dtype))
