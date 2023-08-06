# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


from typing import Callable
import logging

logging.basicConfig(level=logging.INFO, filename='log_3.log', encoding='utf-8', style='{',
                    format='Уровень:{levelname}, дата: {asctime}. {msg}')
log = logging.getLogger(__name__)


def logger(func: Callable):
    def wrapper(*args, **kwargs):
        input_params = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        log.info(f'Функция {func.__name__}\nАргументы: {input_params}\nРезультаты: {result}')

        return result

    return wrapper


@logger
def get_summ(num1: int, num2: int, *args, **kwargs) -> int:
    return num1 + num2



if __name__ == '__main__':
    summ = get_summ(2, 6, x = 10)
    print(summ)