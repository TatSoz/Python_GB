# (Задание 7)
# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.



txt = input('Введите текст: ').replace(' ', '').replace(',', '').replace('-', '').lower()
res = {}
res_by_count = {}

for char in txt:
    res[char] = res.get(char, 0) + 1
print(f'Результат без использования метода count: {res}')

for item in txt:
    res_by_count[item] = txt.count(item)
print(f'Результат с использованием метода count: {res_by_count}')