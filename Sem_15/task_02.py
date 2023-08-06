# На семинаре (sem_9, task_03) про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.


from typing import Callable
import logging

logging.basicConfig(level=logging.INFO, filename='log_2.log', encoding='utf-8')
log = logging.getLogger(__name__)


def logger(func: Callable):

    def wrapper(*args, **kwargs):
        info = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        info['result'] = result
        log.info(info)

        return result

    return wrapper


@logger
def get_summ(num1: int, num2: int, *args, **kwargs) -> int:
    return num1 + num2



if __name__ == '__main__':
    summ = get_summ(2, 6, x = 10, y = 'Hello', z = True)
    print(summ)