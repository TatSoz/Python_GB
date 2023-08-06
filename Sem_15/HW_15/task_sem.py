
import os
import os.path
from pathlib import Path
import argparse
import logging
from collections import namedtuple



logging.basicConfig(filename='log_sem.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='files', field_names='name, type_obj, parent')


def pars():
    parser = argparse.ArgumentParser(prog='Задача №6 семинара 15',
                                     epilog='Информация о содержимом директории',
                                     description='name - имя файла без расширения или название каталога; '
                                                 'type_obj - расширение, если это файл или тип объекта; '
                                                 'parent - название родительского каталога')

    parser.add_argument('-p', '--path', default=os.curdir, help='путь к директории')
    args = parser.parse_args()
    return directory_info(args.path)



def directory_info(file_p: str):

    for dir_path, list_dir, list_files in os.walk(file_p):
        dir_name = os.path.basename(dir_path)
        type_obj = 'folder'
        parent = os.path.basename(os.path.dirname(dir_path))
        date_dir_log = file(dir_name, type_obj, parent)
        logger.info(f'{date_dir_log = }')
        if len(list_files) != 0:
            for file_name_str in list_files:
                file_path = os.path.join(dir_path, file_name_str)
                temp_obj = Path(file_path)
                if temp_obj.is_symlink():
                    file_name = temp_obj.stem
                    type_obj = 'symlink'
                    parent = dir_name
                    date_file_log = file(file_name, type_obj, parent)
                    logger.info(f'{date_file_log = }')
                elif temp_obj.is_file():
                    file_name = temp_obj.stem
                    type_obj = temp_obj.suffix[1:]
                    if type_obj == '':
                        type_obj = 'file without extension'
                    parent = dir_name
                    date_file_log = file(file_name, type_obj, parent)
                    logger.info(f'{date_file_log = }')



if __name__ == '__main__':
    print(pars())

#print(directory_info(r'D:\GeekBrains\Python_GB\Sem_15\HW_15'))