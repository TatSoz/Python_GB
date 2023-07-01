def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))
# print(mean(1, 2, 3))  # Ошибка


def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))

