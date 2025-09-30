# tasks/task2.py

def main():
    # Считываем количество купленных товаров
    X, Y, Z = map(int, input("Введите количество карандашей, ручек и фломастеров: ").split())
    
    # Установим цены
    price_pencil = 3  # цена карандаша
    price_pen = price_pencil + 2  # цена ручки
    price_marker = price_pen + 7  # цена фломастера
    
    # Вычисляем общую стоимость
    total_cost = X * price_pencil + Y * price_pen + Z * price_marker
    
    # Выводим результат
    print(total_cost)

if __name__ == "__main__":
    main()
