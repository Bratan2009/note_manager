from datetime import datetime  # # импортируем библиотеку datetime для проверки формата дат
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},

    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},

    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]
def update_note():  # создаём функцию
    if not notes:
        print('У вас нет сохранённых заметок')
        return
    for i, note in enumerate(notes, start=1):  # цикл for для показа текущих заметок
        print(f'\nЗаметка №{i}:')  # Выводим номер заметки
        print(f'Имя пользователя: {note['username']}')  # Выводим имя пользователя заметки №i
        print(f'Заголовок заметки: {note['title']}')  # Выводим заголовок заметки №i
        print(f'Описание заметки: {note['content']}')  # Выводим описание заметки №i
        print(f'Статус заметки: {note['status']}')  # Выводим статус заметки №i
        print(f'Дата создания заметки: {note['created_date']}')  # Выводим дату создания заметки №i
        print(f'Дата дедлайна: {note['issue_date']}')  # Выводим дату дедлайна заметки №i
        print('---------------------------------------------------------')  # Красиво разделяем заметки

    while True:
        try:
            index = int(input('Введите номер заметки для изменения:'))
            selected_note = notes[index - 1]
            break

        except (ValueError, IndexError):
            print('Пожалуйста, введите номер заметки из предложенных\n')
            continue

    while True:  # бесконечный цикл
        new_value = input(
            'Какие данные вы хотите обновить ?(username, title, content, status, issue_date): ')  # Спрашиваем у пользователя какие данные надо обновить
        new_value = new_value.lower()  # Переводим ключ в нижний регистр

        if new_value in ['username', 'title', 'content',
                         'status']:  # Если пользователь вводит из предложенных, но не дедлайн
            note_change = input(f'Введите новое значение для {new_value}: ')  # Просим пользователя ввести новые данные
            selected_note[new_value] = note_change  # Обновляем данные заметки

            print(f'Заметка обновлена:\n'
                  f'{selected_note}')  # Выводим обновлённую заметку
            break  # Останавливаем цикл

        elif new_value == "issue_date":  # Если пользователь решит изменить дату дедлайна

            while True:  # бесконечный цикл
                note_change = input(f'Введите новое значение для {new_value}:')  # Просим пользователя ввести новую дату

                try:  # проверяем формат даты
                    datetime.strptime(note_change, '%d-%m-%Y')

                except ValueError:  # если формат даты неправильный
                    print(
                        "\nВы ввели некорректный формат даты. Пожалуйста убедитесь, что дата введена в формате день-месяц-год (пример 12-12-2024) ")  # выводим
                    continue
                selected_note[new_value] = note_change  # Обновляем данные заметки
                print(f'Заметка обновлена:\n'
                      f'{notes}')  # Выводим обновлённую заметку
                break  # Останавливаем цикл
            break  # Останавливаем цикл

        else:
            print('\nПожалуйста введите одно из предложенных - username, title, content, status, issue_date')  # выводим
            continue  # Продолжаем цикл

update_note()  # Используем функцию
