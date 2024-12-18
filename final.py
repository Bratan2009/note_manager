username = input("Введите имя пользователя (пример - Bratan@2009):")
first_title = input("Введите заголовок (если нету, пишите - 0): ")
second_title = input("Введите второй заголовок (если нету, пишите - 0):")
third_title = input("Введите третий заголовк (если нету, пишите - 0):")
titles = [first_title,second_title,third_title]
content = input("Введите содержание заметки (прмер - My name):")
status = input("Введите статус заметки (действительна или нет):")
created_date = input("Введите дату создания змаетки (пример - 12.12.24):")
issue_date = input("Введите дату истечения заметки (дедлайн) (пример - 12.01.24):")
note = [f"Имя пользователя: {username} " , f"Содержание заметки: {content}" , f"Статус заметки: {status}" , f"Дата создания: {created_date}" , f"Дата дедлайна заметки: {issue_date}"
        , f"Заголовки: {titles}"
]
print(note)