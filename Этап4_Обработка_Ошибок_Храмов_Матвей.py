
def load_notes_from_file(filename):

    if filename == '':  # если в функции не дали название файлу
        print('Дайте название файлу')
        return None

    while True:  # цикл

        try:  # обработка ошибок
            with open(filename, encoding='utf-8') as file:
                lines = file.read()  # Читаем все строки сразу
                return lines

        except FileNotFoundError:  # ошибка нахождения файла
            with open(filename, 'x') as file:  # создаём новый файл
                print(f'Файл {filename} не найден. Создан новый файл')
                continue

        except OSError:  # Ошибка при чтении
            print(f'Ошибка при чтении файла {filename}. Проверьте его содержимое.')
            break

        except Exception as e:  # все остальные ошибки
            print(f'Ой, ошибка - {e}')
            break


text = load_notes_from_file('')  # вызов функции

if not text:
    pass

else: 
    print(f'{text} - все что есть в файле')
