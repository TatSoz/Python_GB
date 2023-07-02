# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def numbers_gen(numbers_count: int):
    num = 2
    count = 1

    yield num

    while count < numbers_count:
        is_prime = True
        num += 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            yield num 


for number in numbers_gen(20):
    print(number, end=' ')


