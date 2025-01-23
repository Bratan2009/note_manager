notes = [  # заметки для примера
    {
        "username": "Матвей",
        "title": "Заметка 1",
        "content": "Это первая заметка.",
        "status": "Новая",
        "created_date": "12-12-2024",
        "issue_date": "12-12-2025"
    },
    {
        "username": "Тимур",
        "title": "Заметка 2",
        "content": "Это вторая заметка.",
        "status": "В процессе",
        "created_date": "12-12-2024",
        "issue_date": "12-12-2025"
    }
]

def append_notes_to_file(notes, filename):

    while True:  # цикл

        try:  # проверка на ошибки
            with open(filename, 'a', encoding='utf-8') as file:  # открываем файл filename
                for i, note in enumerate(notes, start=1):  # цикл for
                    file.write(f'\nЗаметка №{i}:\n')  # Выводим номер заметки
                    file.write(f'Имя пользователя: {note['username']}\n')  # Выводим имя пользователя заметки №i
                    file.write(f'Заголовок заметки: {note['title']}\n')  # Выводим заголовок заметки №i
                    file.write(f'Описание заметки: {note['content']}\n')  # Выводим описание заметки №i
                    file.write(f'Статус заметки: {note['status']}\n')  # Выводим статус заметки №i
                    file.write(f'Дата создания заметки: {note['created_date']}\n')  # Выводим дату создания заметки №i
                    file.write(f'Дата дедлайна: {note['issue_date']}\n')  # Выводим дату дедлайна заметки №i
                    file.write('---\n')  # Красиво разделяем заметки
            return None

        except FileNotFoundError:  # если файл не найден
            with open(filename, 'x', encoding='utf-8') as file:  # открываем файл
                print(f'Файл {filename} не найден. Создан новый файл.')  # создаём новый файл
            continue

        except Exception as e:  # обрабатываем другие виды ошибок
            print(f'Ошибка - {e}')
            return None




filename = input('Введите имя файла: ').strip() + '.txt'
append_notes_to_file(notes, filename=filename)
