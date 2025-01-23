import json # импортируем библиотеку

notes = [ # заметки для примера
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

def save_notes_json(notes, filename):
    'Эта функция сохраняет заметки в формате json'
    while True: # цикл

        try:  # проверка на ошибки

            with open(filename , 'a' , encoding='utf-8') as file: # открываем файл с кодировкой utf-8
                json.dump(notes, file, ensure_ascii=False, indent=4) # добавляем заметки в файл

            return None #  останавливаем функцию

        except FileNotFoundError: # если файл не найден
            with  open(filename, 'x' , encoding='utf-8') as file:  # создаём новый файл
                print(f'Файл {filename} не найден. Создан новый файл')
            continue

        except Exception as e:
            print(f'Ошибка - {e}')


filename = input('Введите имя файла: ').strip() + '.json'
save_notes_json(notes, filename=filename) # вызов функции