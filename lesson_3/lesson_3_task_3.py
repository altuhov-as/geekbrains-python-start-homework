def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))

    return sum(my_list)


x, y, z = float(input("Число a: ")), float(input("Число b: ")), float(input("Число c: "))
print(my_func(x, y, z))
