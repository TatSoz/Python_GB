last = before = 0
text = [ 'One of the pioneers9 in the industry was famous Walt Disney.',
         'He was not afraid to experiment to make a cartoon, and his Snow White film was among the firsts to use a multiplane camera.',
         'With its help the characters were able to move around the objects, creating an illusion of a 3D world.', ]
with open('../fs/some_dir/new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))


