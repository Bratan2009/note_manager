username = input("Введите имя пользователя (пример - Bratan@2009):")
title = input("Введите название заметки (пример - Name):")
first_title = input("Введите заголовок (если нету, пишите - 0): ")
second_title = input("Введите второй заголовок (если нету, пишите - 0):")
third_title = input("Введите третий заголовк (если нету, пишите - 0):")
titles = [first_title,second_title,third_title]
content = input("Введите содержание заметки (прмер - My name):")
status = input("Введите статус заметки (действительна или нет):")
created_date = input("Введите дату создания змаетки (пример - 12.12.24):")
issue_date = input("Введите дату истечения заметки (пример - 12.01.24):")
sep='\n'
print(" Имя пользователя:", username,sep,"Название заметки:", title ,sep, "Заголовки:",titles,sep,
      "Описание заметки:", content,sep,"Статус заметки:", status,sep,
      "Дата создания заметки:", created_date,sep,"Дата истечения заметки (дедлайн):", issue_date,)