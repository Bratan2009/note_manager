import datetime  # импортируем библиотеку datetime

while True:  # бесконечный цикл (до его остановки)
    date = datetime.datetime.now()  # спрашиваем, какая сейчас дата
    print(f"\nТекущая дата {date.day}-{date.month}-{date.year}")  # выводим дату в виде строки

    issue_date = input(
        "Введите дату дедлайна (в формате день-месяц-год): ")  # спрашиваем дату дедлайна у пользователя в виде строки

    try:  # проверяем формат даты
        date.strptime(issue_date, '%d-%m-%Y') == date.strptime(issue_date, '%d-%m-%Y')
    except:  # проверяем формат даты
        print(
            "\nВы ввели некорректный формат даты. Пожалуйста убедитесь, что дата введена в формате день-месяц-год (пример 12-12-2024) ")  # выводим
        continue

    if int(issue_date[6:10]) > 0:  # проверяем формат даты
        issue_datetime = date.strptime(issue_date, '%d-%m-%Y')  # переводим полученную дату в datetime

        if issue_datetime < date:  # вариант развития событий
            dif = date - issue_datetime  # вычисляем сколько дней прошло с дедлайна
            print(f'\nВнимание!!!Дедлайн истёк {dif.days} дня/дней/день назад')  # выводим
            break  # остановка цикла
        elif issue_datetime > date:  # вариант развития событий
            dif = issue_datetime - date  # вычисляем сколько дней отсталось до дедлайна
            print(f'\nДо дедлайна осталось {dif.days} дня/дней/день')  # выводим
            break  # остановка цикла12
