size = 64
with open('../fs/some_dir/new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))