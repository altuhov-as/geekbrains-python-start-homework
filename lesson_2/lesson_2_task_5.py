my_list = [7, 5, 3, 3, 2]
used_number = int(input("Введите число: "))
"""если число содержится в списке"""
if used_number in my_list:
    ind = 0
    if my_list.count(used_number) == 1:
        ind = my_list.index(used_number)
    else:
        for i in range (my_list.count(used_number)):
            ind = my_list.index(used_number, ind) + 1
        ind -= 1
    my_list.insert(ind, used_number)
else:
    for i, v in enumerate(my_list):
        """если число меньше последнего значения в списке"""
        if used_number < my_list[-1]:
            my_list.insert(len(my_list), used_number)
            break
        elif used_number > v:
            my_list.insert(i, used_number)
            break
print(my_list)
