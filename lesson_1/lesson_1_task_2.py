seconds = int(input("Введите количество секунд: "))

if seconds < 60:
    print(f"00:00:{seconds:02d}")
elif seconds < 3600:
    print(f"00:{seconds//60:02d}:{seconds%60:02d}")
else:
    print(f"{seconds//3600:02d}:{(seconds//60)%60:02d}:{seconds%60:02d}")
