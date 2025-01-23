
def load_notes_from_file(filename):
    global notes
    try:
        with open(filename, encoding='utf-8') as file:
            lines = file.readlines()  # Читаем все строки сразу

        if not lines:  # если файл пуст
            print('Файл пуст')
            return []

        notes = []  # создаём список в который будем добавлять заметки в виде словарей
        current_note = {}  # Создаем временный словарь для текущей заметки

        for line in lines:
            line = line.strip()  # Убираем лишние пробелы и переносы строк

            if '---' in line:  # Если встречаем разделитель, сохраняем текущую заметку и начинаем новую
                notes.append(current_note)
                current_note = {}
            elif ':' in line:

                key, value = line.split(':', maxsplit=1)  # Разбиваем строку на ключ и значение
                current_note[key.strip()] = value.strip()

        if current_note != {}:  # Добавляем последнюю заметку после завершения цикла
            notes.append(current_note)

        for note in notes:  # выводим список заметок
            print(note)

        return notes  # возвращаем список заметок
    except FileNotFoundError:  # если файл не найден
        print(f'Файл {filename} не найден')


load_notes_from_file('task_1')  # вызов функции
