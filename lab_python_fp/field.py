goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]


def field(dicts, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in dicts:
            if args[0] in i.keys() and i[args[0]]:
                yield i[args[0]]
    elif len(args) > 1:
        for i in dicts:
            new_elem = {}
            for key in args:
                if key in i.keys() and i[key]:
                    new_elem[key] = i[key]
            yield new_elem


#for i in field(goods, 'title', 'price'):
#    print(i)