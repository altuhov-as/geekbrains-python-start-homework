def fact(number: int):
    temp_result = 1

    if number == 0:
        yield temp_result

    for i in range(1, number + 1):
        temp_result *= i
        yield temp_result


my_number = 5
for n in fact(my_number):
    print(n)
