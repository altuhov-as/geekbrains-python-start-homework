from random import randint


def write_to_file():
    my_list = [randint(-10, 50) for _ in range(20)]
    with open("text_5.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, my_list)))


def get_sum_from_file():
    with open("text_5.txt", encoding="utf-8") as f:
        my_list = f.readline().split()
        print(f"Сумма чисел = {sum(map(int, my_list))}")


write_to_file()
get_sum_from_file()