notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},

    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},

    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

def search_notes(notes, keyword=None, status=None):  # создаём функцию
    results = []  # создаём список со всеми результатами
    if len(notes) == 0:  # Если у пользователя нет заметок
        print('У вас нету заметок')

    if choice == '1':  # если пользователь выбрал 1 критерий

        for note in notes:  # цикл
            if ((keyword in note['username'].lower()) or (keyword in note['title'].lower()) or (
                    keyword in note[
                'content'].lower())):  # если ключевое слово есть в имени пользователя, в заголовке заметки или в описании заметки
                results.append(note)  # добавляем заметку в список результатов

        if len(results) == 0:  # если ни одна заметка не попала в список результатов
            print('\nНи одной заметки с данным ключевым словом не найдено')

        else:  # если хоть одна заметка попала в список результатов
            print('\nВсе найденные заметки:')

            for i, note in enumerate(results, start=1):  # цикл for для вывода заметок
                print(f'\nЗаметка №{i}:')  # Выводим номер заметки
                print(f'Имя пользователя: {note['username']}')  # Выводим имя пользователя заметки №i
                print(f'Заголовок заметки: {note['title']}')  # Выводим заголовок заметки №i
                print(f'Описание заметки: {note['content']}')  # Выводим описание заметки №i
                print(f'Статус заметки: {note['status']}')  # Выводим статус заметки №i
                print(f'Дата создания заметки: {note['created_date']}')  # Выводим дату создания заметки №i
                print(f'Дата дедлайна: {note['issue_date']}')  # Выводим дату дедлайна заметки №i
                print('---------------------------------------------------------')  # Красиво разделяем заметки

    elif choice == '2':  # если пользователь выбрал 2 критерий

        for note in notes:  # цикл
            if status == note['status'].lower():  # если введённый статус равен статусу заметки
                results.append(note)  # добавляем заметку в список результатов

        if len(results) == 0:  # если ни одна заметка не попала в список результатов
            print('\nНи одной заметки с таким статусом не было найдено')


        else:  # если хоть одна заметка попала в список результатов
            print('\nВсе найденные заметки:')

            for i, note in enumerate(results, start=1):  # цикл for
                print(f'\nЗаметка №{i}:')  # Выводим номер заметки
                print(f'Имя пользователя: {note['username']}')  # Выводим имя пользователя заметки №i
                print(f'Заголовок заметки: {note['title']}')  # Выводим заголовок заметки №i
                print(f'Описание заметки: {note['content']}')  # Выводим описание заметки №i
                print(f'Статус заметки: {note['status']}')  # Выводим статус заметки №i
                print(f'Дата создания заметки: {note['created_date']}')  # Выводим дату создания заметки №i
                print(f'Дата дедлайна: {note['issue_date']}')  # Выводим дату дедлайна заметки №i
                print('---------------------------------------------------------')  # Красиво разделяем заметки
    elif choice == '3': # если пользователь выбрал 3 критерий
        for note in notes:  # цикл
            if status == note['status'].lower() or (
                    (keyword in note['username'].lower()) or (keyword in note['title'].lower()) or
                    (keyword in note['content'].lower())):  # если введённый статус равен статусу заметки или ключевое слово есть в имени пользователя, в заголовке заметки или в описании заметки
                results.append(note)  # добавляем заметку в список результатов

        if len(results) == 0:  # если ни одна заметка не попала в список результатов
            print('\nНи одной заметки с таким статусом или ключевым словом не было найдено')

        else:  # если хоть одна заметка попала в список результатов
            print('\nВсе найденные заметки:')

            for i, note in enumerate(results, start=1):  # цикл for
                print(f'\nЗаметка №{i}:')  # Выводим номер заметки
                print(f'Имя пользователя: {note['username']}')  # Выводим имя пользователя заметки №i
                print(f'Заголовок заметки: {note['title']}')  # Выводим заголовок заметки №i
                print(f'Описание заметки: {note['content']}')  # Выводим описание заметки №i
                print(f'Статус заметки: {note['status']}')  # Выводим статус заметки №i
                print(f'Дата создания заметки: {note['created_date']}')  # Выводим дату создания заметки №i
                print(f'Дата дедлайна: {note['issue_date']}')  # Выводим дату дедлайна заметки №i
                print('---------------------------------------------------------')  # Красиво разделяем заметки
    return results # возвращаем список найденных заметок



def how_to_search():
    global choice

    print(f'Список всех текущих заметок:\n{notes}')  # выводим все заметки

    while True:
        choice = input(
            '\nВыберите критерий для поиска заметки (введите 1, 2 или 3) \n'  # Даём пользователю выбрать критерий для поиска
            '1.Ключевое слово\n'
            '2.Статус заметки\n'
            '3.Ключевое слово и статус заметки:\n')

        if choice == '1':  # если пользователь выбрал 1 критерий
            keyword = input("Введите ключевое слово: ").lower()  # запрашиваем у пользователя ключевое слово

            if keyword == '': # если не ввели ключевое слово
                print('\nВы не ввели ключевое слово')
                continue
            search_notes(notes, keyword, ) # выводим функцию
            break # остановка цикла

        elif choice == '2':  # если пользователь выбрал 2 критерий
            status = input("Введите статус: ").lower() # запрашиваем у пользователя статус

            if status == '':
                print('\nВы не ввели статус')
                continue
            search_notes(notes,status = status) # выводим функцию
            break # остановка цикла

        elif choice == '3':  # если пользователь выбрал 3 критерий
            keyword = input("Введите ключевое слово: ").lower()  # запрашиваем у пользователя ключевое слово
            status = input("Введите статус: ").lower()  # запрашиваем у пользователя статус

            if keyword == '': # если не ввели ключевое слово
                print('\nВы не ввели ключевое слово')
                continue

            elif status == '':
                print('\nВы не ввели статус')
                continue

            else:
                search_notes(notes, keyword, status)  # выводим функцию
                break # остановка цикла

        else:  # если пользователь не ввёл 1, 2 или 3
            print('\nПожалуйста введите 1, 2 или 3 (без пробелов или посторонних знаков)')
            continue
how_to_search()