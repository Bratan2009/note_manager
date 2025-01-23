import yaml

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

def save_notes_to_file(notes, filename): # создаём функцию

    try:
        with open(filename, mode='w', encoding='utf-8') as file: # открываем файл - filename, читаемым и в кодировке utf-8
            for note in notes: # цикл
                yaml.dump(note, file, allow_unicode=True, sort_keys=False) # преобразуем словари в формат yaml, выводим utf-8 в yaml, и отключаем сортировку ключей по алфавиту
                file.write('---')
                file.write('\n\n')
        return None

    except Exception as e:
        print(f'Ой, ошибка - {e}')
        return None
filename = input('Введите имя файла: ') # спрашиваем имя файла
save_notes_to_file(notes, filename) # вызываем функцию
