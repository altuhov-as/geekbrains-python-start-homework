def get_data(first_name: str = None, last_name: str = None, year: int = None, city: str = None,
             phone: str = None, email: str = None):
    return f"{first_name} {last_name} ({year}), {city}, {phone}, {email}"


#мой вариант решения
#функция не отвечает параметрам "Функция должна принимать параметры как именованные аргументы"
def get_data_2(**data):
    for key, value in data.items():
        print("{} ".format(value), end=" ")


user_first_name = input("Имя: ")
user_last_name = input("Фамилия: ")
user_year = int(input("Год рождения: "))
user_city = input("Город: ")
user_email = input("Email: ")
user_phone = input("Номер телефона: ")

print(get_data(first_name=user_first_name, last_name=user_last_name, year=user_year, city=user_city,
               email=user_email, phone=user_phone))

get_data_2(first_name=user_first_name, last_name=user_last_name, year=user_year, city=user_city,
               email=user_email, phone=user_phone)
