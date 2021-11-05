line = input("Введите данные. Окончание работы с программой является пустая строка:")
with open("result.txt", "w", encoding="utf-8") as f:
    while line:
        print(line, file=f)
        line = input("Следующая строка:")
