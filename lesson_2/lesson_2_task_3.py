number = int(input("Введите числовое значение месяца: "))

list_month = [
    [1, "зима"], [2, "зима"], [3, "весна"], [4, "весна"], [5, "весна"], [6, "лето"],
    [7, "лето"], [8, "лето"], [9, "осень"], [10, "осень"], [11, "осень"], [12, "зима"]
]
dict_month = dict()
for i, v in enumerate(list_month):
    if v[0] == number:
        print(v[1])
    dict_month[v[0]] = str(v[1])

if number in dict_month.keys():
    print("Это определенно ", dict_month.get(number))


