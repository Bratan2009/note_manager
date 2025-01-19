from datetime import datetime  # импортируем библиотеку datetime для проверки формата дат


all_notes = []  # список всех заметок
note_count = 0  # кол-во заметок
date = datetime.now()

while True:  # бесконечный цикл
    yes_no = input("Вы хотите создать новую заметку? (да или нет):")  # вопрос пользователю о создании заметок
    if yes_no.lower() == "да":  # если пользователь ответит да
        name = input("Введите имя пользователя:")  # спрашиваем у пользователя имя создателя заметки
        if name == "":  # если пользователь не вводит имя
            name = "нету"
        title = input("Введите заголовок заметки:")  # спрашиваем у пользователя заголовок заметки
        if title == "":  # если пользователь не вводит заголовок
            title = "нету"
        content = input("Введите описание заметки:")  # спрашиваем у пользователя описание заметки
        if content == "":  # если пользователь не вводит описание
                content = "нету"
        status = input(
                "Введите статус заметки (в процессе/завершена и т.п.):")  # спрашиваем у пользователя статус заметки
        if status == "":  # если пользователь не вводит статус
            status = "нету"

        while True:  # бесконечный цикл
            issue_date = input(
                    "Введите дату дедлайна в формате день-месяц-год (пример: 12-12-2025): ")  # спрашиваем у пользователя дату дедлайна

            try:  # проверяем формат даты
                datetime.strptime(issue_date, '%d-%m-%Y')
            except ValueError:  # если формат не верный
                print("Пожалуйста введите дату в правильном формате (пример: 12-12-2024)")
                continue  # продолжение цикла
            break  # остановка цикла

        note = {"Имя пользователя": name, "Заголовок заметки": title, "Описание заметки": content,
                "Статус заметки": status, "Дата создания заметки": (f"{date.day}-{date.month}-{date.year}"),
                "Дата дедлайна": issue_date}  # создаём заметку
        all_notes.append(note)  # добавляем заметку в список

    elif yes_no.lower() == "нет":  # если пользователь ответит нет
        break  # остановка цикла
    else:  # если пользователь не ввёл ни да, ни нет
        print("Пожалуйста введите да или нет без пробелов и посторонних знаков")  # просим ввести да или нет
#--------------------------------------------------------------------------------------------------------------------------------- вместо примера заметок

def display_notes(all_notes):  # Создаём функцию
    if not all_notes: # если заметок нет
        print('У вас нет сохранённых заметок')
        return
    print("Досвидания\nВот все ваши заметки:")
    for i , note in enumerate(all_notes, start = 1): # цикл for
        print(f'\nЗаметка №{i}:') # Выводим номер заметки
        print(f'Имя пользователя: {note['Имя пользователя']}') # Выводим имя пользователя заметки №i
        print(f'Заголовок заметки: {note['Заголовок заметки']}') # Выводим заголовок заметки №i
        print(f'Описание заметки: {note['Описание заметки']}') # Выводим описание заметки №i
        print(f'Статус заметки: {note['Статус заметки']}') # Выводим статус заметки №i
        print(f'Дата создания заметки: {note['Дата создания заметки']}') # Выводим дату создания заметки №i
        print(f'Дата дедлайна: {note['Дата дедлайна']}') # Выводим дату дедлайна заметки №i
        print('---------------------------------------------------------') # Красиво разделяем заметки
display_notes(all_notes) # Используем функцию