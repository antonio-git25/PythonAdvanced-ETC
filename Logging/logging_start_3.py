import logging
import csv

# создаем логгер
logger = logging.getLogger('data_processing')
logger.setLevel(logging.INFO)


def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            # читаем данные из файла
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)

            # обрабатываем данные
            result = []
            for i in range(1, len(data)):
                if int(data[i][1]) > 50:
                    result.append(data[i][0])

            # выводим результаты
            logger.info("Обработан файл %s, найдено %s записей", file_path, len(result))

    except FileNotFoundError:
        logger.error("Файл %s не найден", file_path)

    except csv.Error:
        logger.error("Ошибка при чтении данных из файла %s", file_path)


# список файлов для обработки
files = ['data1.csv', 'data2.csv', 'data3.csv']


for file in files:
    process_file(file)