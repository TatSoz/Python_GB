"""map(function, iterable)"""
texts = ['Привет', 'ЗДОРОВА', 'ПривеТствую']
res = map(lambda x: x.lower(), texts)
print(*res)