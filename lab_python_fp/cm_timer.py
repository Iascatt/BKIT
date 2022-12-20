from contextlib import contextmanager
from time import perf_counter, sleep


class cm_timer_1:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        print(perf_counter() - self.start)


@contextmanager
def cm_timer_2():
    start = perf_counter()
    yield
    print(perf_counter() - start)


#with cm_timer_1():
#    sleep(5.5)

#with cm_timer_2():
#    sleep(5.5)
