status = input("Введите статус заметки:")  # Спрашиваем у пользователя текущий статус
print(f"Текущий статус : {status}")  # Выводим его
sep = '\n'
while True:  # бесконечный цикл (до его остановки)
    yes_no = input("Вы хотите изменить статус? (да/нет):")  # Спрашиваем пользователя хочет ли он изменить его
    if yes_no.lower() == "да":  # Варианты событий в зависимости от ответа пользователя

        while True:  # бесконечный цикл (до его остановки)
            NewStatus = input(f"\nВыберете новый статус заметки(1/2/3):"  # Даём пользователю выбрать варианты ответа
                              f"{sep}1.Выполнено"
                              f"{sep}2.В процессе"
                              f"{sep}3.Отложено"
                              f"{sep}-")
            if NewStatus == "1":  # Варианты событий в зависимости от ответа пользователя
                status = "Выполнено"
                print(f"Текущий статус : {status}")
                break  # остановка цикла

            elif NewStatus == "2":  # Варианты событий в зависимости от ответа пользователя
                status = "В процессе"
                print(f"Текущий статус : {status}")
                break  # остановка цикла

            elif NewStatus == "3":  # Варианты событий в зависимости от ответа пользователя
                status = "Отложено"
                print(f"Текущий статус : {status}")
                break  # остановка цикла
            else:  # если пользователь не выбирает один из вариантов ответа

                print("Пожалуйста, выберете один из предложенных вариантов (1/2/3)")
                continue  # перезапуск цикла

    elif yes_no.lower() == "нет":
        print("\nХорошо, до свидания")
        break  # остановка кода

    else:  # если пользователь не выбирает один из вариантов ответа
        print("Пожалуйста введите да или нет")
        continue  # перезапуск цикла