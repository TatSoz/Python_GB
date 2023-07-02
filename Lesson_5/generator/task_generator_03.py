x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 12, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)  # генератор

# mult = list()
# for i in x:
#     if i % 2 != 0:
#         for j in y:
#             if j != 1:
#                 mult.append(i + j)

res = list(mult)
print(f'{len(res)}\n{res}')