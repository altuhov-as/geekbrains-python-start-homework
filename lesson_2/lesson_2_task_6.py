my_list = []
i = 0
text = None
list_characteristics = ["название", "цена", "количество", "единица измерения"]
while True:
    i += 1
    text = input(f"Введите характеристики товара"
                 f"({', '.join(list_characteristics)}):\n"
                 f"(для выхода 'exit')\n").split()
    if text == ['exit']:
        break
    dict_t = {}
    for it, v in enumerate(text):
        if it == 1 or it == 2:
            dict_t[list_characteristics[it]] = int(v)
        else:
            dict_t[list_characteristics[it]] = v
    tuple_t = (i, dict_t)
    my_list.append(tuple_t)

dict_result = dict()
for it in list_characteristics:
    list_result = []
    if it == list_characteristics[-1]:
        dict_result[it] = [my_list[0][1].get(it)]
    else:
        for i, v in enumerate(my_list):
            list_result.append(v[1].get(it))
        dict_result[it] = list_result

for k, v in dict_result.items():
    print(k, v)
