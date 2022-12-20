# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.used_elements = set()
        self.index = 0
        self.ignore_case = kwargs['ignore_case'] if 'ignore_case' in kwargs.keys() else False

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if next(self.items) is None:
                raise StopIteration
            else:
                current = next(self.items)
                self.index = self.index + 1
                if current.lower() not in self.used_elements:
                    self.used_elements.add(current.lower())
                    return current
