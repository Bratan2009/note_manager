from datetime import datetime  # импортируем библиотеку datetime для проверки формата дат

def create_note():
    notes = []  # список всех заметок
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
                    print("Введите дату в правильном формате (пример: 12-12-2024)")
                    continue  # продолжение цикла
                break  # остановка цикла

            note = {"Имя пользователя:": name, "Заголовок заметки:": title, "Описание заметки:": content,
                    "Статус заметки:": status, "Дата создания заметки:": (f"{date.day}-{date.month}-{date.year}"),
                    "Дата дедлайна:": issue_date}  # создаём заметку

            notes.append(note)  # добавляем заметку в список
            print(f'Заметка успешно добавлена:{note}')

        elif yes_no.lower() == "нет":  # если пользователь ответит нет
            print("До свидания")  # прощаемся и выводим все заметки
            break  # остановка цикла

        else:  # если пользователь не ввёл ни да, ни нет
            print("Пожалуйста введите да или нет без пробелов и посторонних знаков")  # просим ввести да или нет


create_note()