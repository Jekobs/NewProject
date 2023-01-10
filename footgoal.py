import logging
import collections
import csv
#import bs4
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wb')

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url',
    ),
)

HEADERS = (
    'Бренд',
    'Товар',
    'Ссылка',
)


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept-Language': 'ru',
            'X-Fsign': 'SW9D1eZo'
        }
        self.result = []

    def load_page(self, page: int = None):
        url = 'https://d.soccerstand.com/ru/x/feed/f_1_0_3_ru_1'
        # url = 'https://www.wildberries.ru/catalog/muzhchinam/bele'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def get_array(self, text: str):
        # print(res.text)
        # print(len(res.text))
        fs_rows = text
        # fs_rows_length = len(fs_rows)
        # fs_row = fs_rows_length.split("¬")
        # s = []
        for block in fs_rows:

        # for block in range(len(fs_rows[0:-4])):
            # fs_rows = range(len(fs_rows[0:-4]))
            # s = []
            # fs_rows = res.text.split("¬")
            # fs_rows = res.text.split("÷")
            # fs_row = list()
            # fs_row = split(i[0], "÷")
            # fs_index = split(fs_row(0), "?")
            # it = i
            # fs_row = it[]
            # print(A)
            # print(block, fs_rows)
            # print(ord("¬"))
            # print(i)
            # print(fs_rows_length)
            # chr(&HF7)
            self.parse_block(block=block)

    def parse_page(self, text: str):
        # print(text)
        fs_rows = text.split('~')
        fs_row_length = len(fs_rows[0:-4])
        # fs_rows2 = len(fs_rows[0:-4])
        # fs_rows2 = range(len(fs_rows[0:-4]))
        # print(fs_row_length)
        # i = 0
        for i in range(fs_row_length):
            for fs_rows2 in fs_rows:
                fs_row = fs_rows2.split('¬')
                fs_index = fs_row[0].split('÷')
                # fs_row_length2 = len(fs_index)
                for s in range(len(fs_index)):
                    # if len(fs_row_length2) != 0:
                    # print(s)
                    # print(fs_index[s])
                    print(fs_row)

                    # for fs in i:
                    #     # print(fs_row(i))
                    #     # print(fs_index)
                    #     print(fs))
        # fs_row = list(fs_rows)
        # print(fs_row)
        # print(chr(63))
        # soup = text
        # soup = bs4.BeautifulSoup(text, 'lxml')
        # container = soup.split("~")
        # container = soup.select('div.product-card.j-card-item')
        # container = len(self.result[0:-4])
        # for block in container:
        #     self.parse_block(block=block)

    def parse_block(self, block):
        logger.info(block)
        # logger.info('=' * 100)

        # url_block = block.select_one('a.product-card__main')
        # if not url_block:
        #     logger.error('no url_block')
        #     return
        #
        # url = url_block.get('href')
        # if not url:
        #     logger.error('no url')
        #     return
        #
        # name_block = block.select_one('div.product-card__brand-name')
        # if not name_block:
        #     logger.error(f'no name_block on {url}')
        #     return
        #
        # brand_name = name_block.select_one('strong.brand-name')
        # if not brand_name:
        #     logger.error(f'no brand_name on {url}')
        #     return
        #
        # # Wrongler /
        # brand_name = brand_name.text
        # brand_name = brand_name.replace('/', '').strip()
        #
        # goods_name = name_block.select_one('span.goods-name')
        # if not goods_name:
        #     logger.error(f'no goods_name on {url}')
        #     return
        #
        # # Wrongler /
        # goods_name = goods_name.text
        # goods_name = goods_name.replace('/', '').strip()

        # self.result.append(ParseResult(
        #     url=url,
        #     brand_name=brand_name,
        #     goods_name=goods_name,
        # ))

        # logger.info('%s, %s, %s', url, brand_name, goods_name)
        # logger.info('-' * 100)

    def save_result(self):
        path = 'test.csv'
        with open(path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        text = self.load_page()
        # self.get_array(text=text)
        self.parse_page(text=text)
        logger.info(f'Плучили {len(self.result)} элементов')
        self.save_result()

if __name__ == '__main__':
    parser = Client()
    parser.run()
    # get_array()