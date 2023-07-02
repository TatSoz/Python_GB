my_dictcomp = {i: chr(i) for i in range(97, 123)}  # dict comprehension- генерация словаря
print(my_dictcomp)
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')

