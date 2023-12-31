# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.


import csv
import json


def from_csv_to_json(file_csv: str, file_json: str) -> None:
    with (
        open(file_csv, 'r', encoding='utf-8', newline='') as f1,
        open(file_json, 'w', encoding='utf-8') as f2
    ):
        text_csv = csv.reader(f1)
        list_ = []
        for i, (id_, name, level) in enumerate(text_csv):
            if i:
                list_.append({
                    'id': id_.zfill(10),
                    'name': name.capitalize(),
                    'level': level,
                    'hash': hash(id_ + name)
                })
        json.dump(list_, f2, indent=4)


if __name__ == '__main__':
    from_csv_to_json('task_3.csv', 'task_6.json')




