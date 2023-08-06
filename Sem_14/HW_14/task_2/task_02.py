# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


MIN = 0
MAX = 100000

def check_number(num: int):

    if num == 1:
        return 'Число 1 не является ни простым, ни составным'
    elif MIN < num < MAX:
        count = 0
        for i in range(2, num):
            if (num % i == 0):
                count += 1
        if (count <= 0):
            return 'Число является простым'
        else:
            return 'Число является составным'
    else:
        return 'Введённое число не входит в заданный диапазон'



if __name__ == '__main__':
    print(check_number(5))
    print(check_number(4))
    print(check_number(-2))
    print(check_number(1))






