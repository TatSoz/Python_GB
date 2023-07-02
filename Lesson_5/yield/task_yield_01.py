def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


for j, num in enumerate(factorial(10), start=1):
    print(f'{j} ! = {num}')

