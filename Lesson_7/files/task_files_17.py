text = [ 'One of the pioneers9 in the industry was famous Walt Disney.',
         'He was not afraid to experiment to make a cartoon, and his Snow White film was among the firsts to use a multiplane camera.',
         'With its help the characters were able to move around the objects, creating an illusion of a 3D world.', ]
with open('../fs/some_dir/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')

