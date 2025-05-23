import pandas as pd
import os
class Check_file():
    def __init__(self, file_filename, exemplar_filename):
        try:
            self.file = pd.read_csv(file_filename)
        except FileNotFoundError:
            print("Возникла следующая ошибка: Файл не найден")  
            raise SystemExit
        except pd.errors.EmptyDataError:
            print("Возникла следующая ошибка: Датафрейм пуст")
            raise SystemExit
        except pd.errors.ParserError:
            print("Возникла следующая ошибка: Количество столбцов с данными больше количества столбцов в датафрейме")    
            raise SystemExit
        file_columns = []
        exemplar_columns = []
        k = 0
        for column_name in self.file.columns:
            file_columns.append(column_name)
        check = pd.read_csv(exemplar_filename)
        for column_name in check.columns:
            exemplar_columns.append(column_name)
        try:
            for column_name in check.columns:
                if column_name != file_columns[k]:
                    raise ValueError
                k += 1
        except ValueError:
            print("Структура датафрейма НЕ соотвествует ожидаемой:")
            print("Названия столбцов не совпадают")
            print("Ожидаемые", exemplar_columns)
            print("Фактические", file_columns)
            raise SystemExit
        check_column_types = []
        file_column_types = []
        for column_name in check.columns:    
            check_column_types.append(check[column_name].dtype)
        for column_name in self.file.columns:    
            file_column_types.append(self.file[column_name].dtype)
        try:
            for i in range(0, len(check.columns)-1):
                if file_column_types[i] != check_column_types[i]:
                    raise TypeError
        except TypeError:
            print(f"В столбце {exemplar_columns[i]} тип данных не соответствует ожидаемому")
            print(f"Ожидаемый тип данных: {check_column_types[i]}")
            print(f"Полученный тип данных: {file_column_types[i]}")
        print("Чтение датафрейма успешно завершено")

def main():
    exemplar = 'exemplar.csv'  
    file = 'otsos.csv'  
    Check_file(file, exemplar)

if __name__ == "__main__": 
    main()
