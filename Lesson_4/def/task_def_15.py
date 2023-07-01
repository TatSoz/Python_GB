def combined_arg(a, /, b, *, c):
    print(a, b, c)


# combined_arg(1, 2, 3)  # Ошибка
combined_arg(1, 2, c=3)
combined_arg(1, b=2, c=3)
# combined_arg(a=1, b=2, c=3)  # Ошибка

