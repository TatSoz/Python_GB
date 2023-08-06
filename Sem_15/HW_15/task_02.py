import logging
import argparse

MIN = 0
MAX = 100000


logging.basicConfig(filename='log_2.log', filemode='a', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

def pars():
    parser = argparse.ArgumentParser(prog='Задача №2',
                                     epilog='Число -> простое или составное',
                                     description='Данный модуль проверяет является ли число простым или составным')
    parser.add_argument('-n', '--num')
    args = parser.parse_args()
    return check_number(int(args.num))


def check_number(num: int):

    if num == 1:
        logger.info('Число 1 не является ни простым, ни составным')
        return
    elif MIN < num < MAX:
        count = 0
        for i in range(2, num):
            if (num % i == 0):
                count += 1
        if (count <= 0):
            logger.info(f'Число {num} является простым')
            return
        else:
            logger.info(f'Число {num} является составным')
            return
    else:
        logger.error(f'Число {num} не входит в заданный диапазон')
        return



if __name__ == '__main__':
    # print(check_number(4))
    # print(check_number(5))
    # print(check_number(-9))
    # print(check_number(1))
    pars()
