# tasks/task1.py

def main():
    S = int(input("Введите общее количество журавликов: "))
    
    # Вычисляем количество журавликов, сделанных Петей и Сережей
    x = S // 6
    
    # Количество журавликов, сделанных каждым ребенком
    petya = x
    katya = 4 * x
    sereja = x
    
    # Выводим результат
    print(petya, katya, sereja)

if __name__ == "__main__":
    main()
