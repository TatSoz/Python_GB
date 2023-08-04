import logging

logger = logging.getLogger(__name__)


def log_all():
    logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
    logging.info('Немного информации о работе кода')
    logging.warning('Внимание! Надвигается буря!')
    logging.error('Поймали ошибку.Дальше только неизвестность')
    logging.critical('На этом всё')


if __name__ == '__main__':
    log_all()

