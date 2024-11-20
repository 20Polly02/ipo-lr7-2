import json#подключаем модуль json
num_id = int(input("Введите номер квалификации: "))# ввод с клавиатуры номера квалификации 
find = False #создаем переменную которая будет указывать на то, найдена ли такая квалификация

with open("dump.json", 'r', encoding='utf-8') as file: #открываем файл для чтения
  file_r = json.load(file) #загружаем все содержимое файла в переменную file_r
  for skill in file_r:# используем цикл for чтобы пройтись по всем элементам из файла 
    if skill.get("model") == "data.skill": #проверяется является ли значение "model" = data.skill"
      if skill["fields"].get("specialty") == num_id: #проверяется, совпадает ли введенный код квалификации с кодом из файла
        skill_code = skill["fields"].get("code")#если совпадает, сохраняем код и название квалификации в переменные 
        skill_title = skill["fields"].get("title")
        find = True#т.к. калификация найдена придаем переменной find значение true

        for speciality in file_r:#с помощью цикла for перебираем каждый элемент в файле
          if speciality.get("model") == "data.specialty":# с помощью цикла проверяем, является ли значение "model" == "data.specialty" 
            code_speciality = speciality["fields"].get("code")# если совпадает, сохраняем код специальности
            if code_speciality in skill_code: # с помощью цикла проверяем, содержится ли код специальности в коде квалификации
              title_speciality = speciality["fields"].get("title")#если содержится, сохраняем название специальности
              type_speciality = speciality["fields"].get("c_type")#если содержится, сохраняем тип образования
if not find:#с помощью цикла проверяем, найдена ли квалификация
  print("=============== Не Найдено ===============") #если не навдена ,вывод результата на консоль
else:#если квалификация найдена
  print("=============== Найдено ===============") #вывод на консоль результата
  print(f"{code_speciality} >> Специальность '{title_speciality}' , {type_speciality}")#вывод на консоль
  print(f"{skill_code} >> Квалификация '{skill_title}'")#вывод на консоль
