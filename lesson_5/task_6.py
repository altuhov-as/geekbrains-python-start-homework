subject = {}


def get_hours(user_list: list):
    hours = 0
    for el in user_list:
        if el.count("(") != 0:
            hours += int(el.split("(")[0])
    return hours


with open('text_6.txt', encoding="utf-8") as f:
    for row in f:
        subject_info = row.split()
        name = subject_info[0].rstrip(':')
        subject[name] = get_hours(subject_info[1:])

print(subject)

