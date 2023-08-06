import argparse
import logging


GREGORIAN_START = 1582
FOUR_YEARS = 4
HUNDRED_YEARS = 100
FOUR_HUNDRED_YEARS =400

logging.basicConfig(filename='log_1.log', filemode='a', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

def pars():
    parser = argparse.ArgumentParser(prog='Задача №1',
                                     epilog='Год -> високосный/обычный',
                                     description='Данный модуль проверяет год на високосность')
    parser.add_argument('-y', '--year')
    args = parser.parse_args()
    return leap_year(int(args.year))

def leap_year(year: int):

    if year <= GREGORIAN_START:
        logger.info(f'{year} - Год обычный')
        return
    else:
        if year % FOUR_YEARS != 0:
            logger.info(f'{year} - Год обычный')
            return
        elif year % HUNDRED_YEARS == 0:
            if year % FOUR_HUNDRED_YEARS == 0:
                logger.info(f'{year} - Год високосный')
                return
        else:
            logger.info(f'{year} - Год високосный')
            return



if __name__ == '__main__':
    pars()


