import csv
from collections import defaultdict

def split_dataset(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) 
        data = list(reader)
    
    # Поиск данных банков
    banks_data = defaultdict(list)
    for row in data:
        terminal = row[5]  
        bank_name = terminal.split('-')[0]  # Поиск названия банка
        banks_data[bank_name].append(row)
    
    # Запись данных в отдельные файлы для каждого банка
    for bank_name, bank_rows in banks_data.items():
        output_file = f'{bank_name}.csv'
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(bank_rows)
        print(f'Данные банка записаны в файл {output_file}, всего {len(bank_rows)} записей')

class Dataset:
    def __init__(self, data=None, header=None):
        self.data = data if data is not None else []
        self.header = header if header is not None else []
        self.duplicates_count = 0
    
    def __neg__(self):
        """Перегрузка унарного оператора - для удаления дубликатов"""
        unique_data = []
        seen = set()
        duplicates_count = 0
        
        for row in self.data:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
            else:
                duplicates_count += 1
        
        result = Dataset(unique_data, self.header)
        result.duplicates_count = duplicates_count
        return result
    
    @classmethod
    def from_csv(cls, filename):
        """Создание Dataset из CSV файла"""
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
        return cls(data, header)
    
    def to_csv(self, filename):
        """Сохранение Dataset в CSV файл"""
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
            writer.writerows(self.data)        

def main():
    pass

if __name__ == "__main__": 
    input_filename = 'var6.csv'  # Имя исходного файла
    output_filename = 'var6_no_dublikates.csv'  # Имя итогового файла
    dataset = Dataset.from_csv(input_filename)
    unique_dataset = -dataset
    unique_dataset.to_csv(output_filename)
    print(f"Количество удалённых дубликатов: {unique_dataset.duplicates_count}")
    input_filename = 'var6_no_dublikates.csv' # имя нового исходного файла
    split_dataset(input_filename)