MIN_NUMBER = 2
MIDDLE_NUMBER = 5
MAX_NUMBER = 10


def multiplication_table(num_1, num_2):
    if num_2 > MIDDLE_NUMBER:
        num_1 += 1
        num_2 -= 1

    for row in range(2, 11):
        for col in range(num_1, num_2 + 1):
            print(f"{col} X {row:2d} = {col * row:2d}\t ", end='')
        print()


print("{:^50}".format("ТАБЛИЦА УМНОЖЕНИЯ"))
multiplication_table(MIN_NUMBER, MIDDLE_NUMBER)
print()
multiplication_table(MIDDLE_NUMBER, MAX_NUMBER)