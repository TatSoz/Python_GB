text = 'In 1895 brothers Louis and Auguste Lumière created a cinematograph.'
with open('../fs/some_dir/new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')

