import codecs
import json
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2

path = "data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with codecs.open(path, "r", "utf-8") as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def f1(arg):
    return Unique(field(sorted(arg, key=lambda x: x['job-name']), 'job-name'))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return list(map(lambda x: f"{x[0]}, зарплата {x[1]} руб.", zip(arg, gen_random(len(arg), 100000, 200000))))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

