# tasks/task3.py

def solve():
    # Считываем количество банок, которые прострелили Гарри и Ларри
    a, b = map(int, input("Введите количество банок, простреленных Гарри и Ларри: ").split())
    
    # Вычисляем количество банок, которые не успел прострелить каждый
    not_shot_by_harry = b - 1
    not_shot_by_larry = a - 1
    
    # Выводим результат
    print(not_shot_by_harry, not_shot_by_larry)

if __name__ == "__main__":
    main()
