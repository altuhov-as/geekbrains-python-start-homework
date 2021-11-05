user_text = input("Введите текст: ").split()

for i, v in enumerate(user_text):
    if len(v) < 11:
        print(i + 1, v)
    else:
        print(i + 1, v[:10])
