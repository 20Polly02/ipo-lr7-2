import json  # импортируем библиоеку json

num_code = input("Введите номер квалификации: ")  #ввод ноера квалификации от пользователя
find = False  # инициализируем переменную find как False

with open("dump.json", 'r', encoding='utf-8') as file:  # открываем файл dump.json для чтения
    info_file = json.load(file)  # загружаем содержимое файла в переменную info_file
    for skill in info_file:  # перебираем каждый элемент в info_file
        if skill.get("model") == "data.skill":  # проверяем, является ли значение "model" = data.skill"
            if skill["fields"].get("code") == num_code:  # проверяем, совпадает ли код квалификации с введенным
                skill_code = skill["fields"].get("code")  # получаем код квалификации
                skill_title = skill["fields"].get("title")  # получаем название квалификации
                skill_specialty=skill["fields"].get("specialty") #получаем код специальности
                find = True  # так как квалификация найдена
                
if not find:  # если переменная не найдена
    print("Не найдено")  #вывод на консоль
    exit()
for specialty in info_file:  # перебираем каждый элемент в info_file
    if specialty.get("model") == "data.specialty":  # проверяем, является ли значение "model" = data.specialty"
        specialty_code = specialty["fields"].get("code")  # получаем код специальности
        specialty_pk = specialty.get("pk") #получаем код pk

        if skill_specialty == specialty_pk:  # проверяем, одинаковое ли значение у pk и кода специальности 
            specialty_title = specialty["fields"].get("title")  # получаем название специальности
            specialty_educational = specialty["fields"].get("c_type")  # получаем тип образования 
            specialty_c = specialty["fields"].get("code")  # получаем код специальности

else:  # если квалификация найдена
    print("Найдено") # вывод на консоль
    print(f"{specialty_c} >> Специальность '{specialty_title}', {specialty_educational}")  #вывод на консоль 
    print(f"{num_kv} >> Квалификация '{skill_title}'")  #вывод на консоль 
