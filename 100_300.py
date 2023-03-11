import os
import datetime
import requests

# Define the filename and path where you want to save the file
filename = "data_goal.txt"
path = "data/"
update_period="12"

# result = []

class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept-Language': 'ru',
            'X-Fsign': 'SW9D1eZo'
        }
        # self.result = []

    def init_run(self):
        pass

    def load_page(self, page: int = None):
        url = 'https://d.soccerstand.com/ru/x/feed/f_1_0_3_ru_1'
        # url = 'https://www.wildberries.ru/catalog/muzhchinam/bele'
        res = self.session.get(url=url)
        print(res.encoding) # Проверка кодировки
        res.raise_for_status()
        return res.text
    def parse_page(self):
        texts = text
    def save_result(self, text: str):
        # Check if the file already exists
        if os.path.exists(os.path.join(path, filename)):
            print('File already exists.')
        else:
            # If the file doesn't exist, create it and add the date to the filename
            today = datetime.datetime.today()
            # new_filename = "{}_{}".format(today.strftime("%Y-%m-%d"), filename)
            # filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"  # создает имя файла с текущей датой и временем
            new_filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"  # создает имя файла с текущей датой и временем
            with open(os.path.join(path, new_filename), "w", encoding="utf-8") as f:
                f.write(text)  #Это новый файл.
                print("File created: {}".format(new_filename))

        # path = 'test.csv'
        # with open(path, 'w', encoding='utf-8') as f:
        #     writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        #     writer.writerow(HEADERS)
        #     for item in self.result:
        #         writer.writerow(item)

    def run(self):
        text = self.load_page()
        # self.get_array(text=text)
        # self.parse_page(text=text)
        # logger.info(f'Плучили {len(self.result)} элементов')
        self.save_result(text)
        # return text

if __name__ == '__main__':
    parser = Client()
    parser.run()
    # get_array()

# import os
# import datetime
#
# filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"  # создает имя файла с текущей датой и временем
# if not os.path.exists(filename):  # checks if the file already exists
#     with open(filename, 'w') as f:  # проверяет, существует ли уже файл
#         # write whatever you want to write in the file
#         f.write("This is a sample text to write in the file.")    #Это пример текста для записи в файл
#     print(f"File '{filename}' created and saved successfully.")
# else:
#     print(f"File '{filename}' already exists.")
