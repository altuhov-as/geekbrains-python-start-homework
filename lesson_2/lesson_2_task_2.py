user_list = input("Введите последовательность чисел: ").split()
my_list = []

for i in range(len(user_list)):
    my_list.append(None)

if len(user_list) % 2 == 0:
    for i, v in enumerate(user_list):
        if i % 2 == 1:
            my_list[i - 1] = v
            my_list[i] = user_list[i - 1]
else:
    for i, v in enumerate(user_list):
        if i % 2 == 1:
            my_list[i - 1] = v
            my_list[i] = user_list[i - 1]
        elif i == len(user_list) - 1:
            my_list[i] = v

print(my_list)
