f = open('../fs/dir/other_dir/data.txt', 'wb')
f.write('Привет,  '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f))
# f.close()

f = open('../fs/dir/other_dir/data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()

