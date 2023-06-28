# (Задание 8)
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей
#
#
friends_things = {'Петр': ('Палатка', 'Спальник', 'Кружка', 'Рация', 'Консервы', 'Каремат'),
                  'Вася': ('Спальник', 'Кружка', 'Фонарик', 'Топор', 'Котелок', 'Спички'),
                  'Иван': ('Палатка', 'Спальник', 'Тент', 'Удочка', 'Спички', 'Нож')
                 }

all_things = set()
uniq_things_dict = {}
not_have_things_dict = {}

for friend in friends_things:
    uniq_things = set(friends_things[friend])
    not_have_things = set()
    for other_friend in friends_things:
        if other_friend != friend:
            uniq_things -= set(friends_things[other_friend])
            if not not_have_things:
                not_have_things |= (set(friends_things[other_friend]))
            else:
                not_have_things.intersection_update(set(friends_things[other_friend]))
    all_things |= set(friends_things[friend])
    uniq_things_dict[friend] = uniq_things
    not_have_things_dict[friend] = not_have_things - set(friends_things[friend])

print(f'Все вещи, которые взяли друзья:\n {all_things}\n')

for key in uniq_things_dict:
    print(f'Только {key} взял {uniq_things_dict[key]}')

print()
for key in not_have_things_dict:
    print(f'Только {key} не взял {not_have_things_dict[key]}')

