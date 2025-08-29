import getpass
import os
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd  
from functools import wraps

def plot_stock_prices(file_path):
    stock_prices = pd.read_csv(file_path)
    
    # Сбрасываем индекс чтобы иметь последовательные числовые индексы
    stock_prices = stock_prices.reset_index(drop=True)
    
    plt.figure(figsize=(12, 6), dpi=100)
    up = stock_prices[stock_prices.Close >= stock_prices.Open]
    down = stock_prices[stock_prices.Close < stock_prices.Open]

    col_up = 'green'
    col_down = 'red'
    width = 0.6
    wick_width = 0.1
        
    plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col_up)
    plt.bar(up.index, up.High-up.Close, wick_width, bottom=up.Close, color=col_up)
    plt.bar(up.index, up.Low-up.Open, wick_width, bottom=up.Open, color=col_up)
        
    plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col_down)
    plt.bar(down.index, down.High-down.Open, wick_width, bottom=down.Open, color=col_down)
    plt.bar(down.index, down.Low-down.Close, wick_width, bottom=down.Close, color=col_down)
        
    plt.title(f'График акций Apple')
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.grid(True, linestyle='--', alpha=0.6)
        
    step = max(1, len(stock_prices) // 10)
    plt.xticks(
        ticks=range(0, len(stock_prices), step),
        labels=stock_prices['Date'].iloc[::step],
        rotation=45
    )
        
    plt.tight_layout()
    plt.show()

def log_function(func):
    """Декоратор для логирования вызовов функций"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_login = getpass.getuser()
        script_name = os.path.basename(__file__)
        current_date = datetime.datetime.now().strftime('%d %m %Y')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        log_data = {
            "User_login": user_login,
            "Function_name": func.__name__,
            "Date": current_date,
            "Time": current_time
        }
        
        file_exists = os.path.isfile('logs.csv')
        with open('logs.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, 
                                fieldnames=["User_login", "Function_name", "Date", "Time"])
            if not file_exists:
                writer.writeheader()
            writer.writerow(log_data)
        
        return func(*args, **kwargs)
    return wrapper

@log_function
def main():
    file_path = "AAPL.csv"
    plot_stock_prices(file_path)

if __name__ == "__main__":
    main()