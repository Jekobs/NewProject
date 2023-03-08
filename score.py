import os
import datetime

filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"  # создает имя файла с текущей датой и временем
if not os.path.exists(filename):  # checks if the file already exists
    with open(filename, 'w') as f:  # проверяет, существует ли уже файл
        # write whatever you want to write in the file
        f.write("This is a sample text to write in the file.")    #Это пример текста для записи в файл
    print(f"File '{filename}' created and saved successfully.")
else:
    print(f"File '{filename}' already exists.")