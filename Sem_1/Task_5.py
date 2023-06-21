E = 3
n = 100
summ = 0
count = 1

while count <=n:
    if count % 2 == 0 and count % E != 0:
         summ += count
    count += 1
print(summ)
