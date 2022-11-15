# ЗАДАНИЕ-4.3
# Доработать класс FlatIterator.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов,
# обрабатывающий списки с любым уровнем вложенности.
# Функция test также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_lists, stop=False, iterations=0):
        self.lists = list_of_lists
        self.stop_iterations = stop
        self.iterations = iterations
        self.chunk = []
        self.simpler_list = []
        print('def __init__(self, list_of_lists, counter_of_lists=0):')  #
        print(f'\tlists = {list_of_lists}')  #
        print(f'\titerations = {iterations}')  #

    def __iter__(self):
        print('def __iter__(self):')  #
        self.iter_list = iter(self.lists)
        self.iter_chunk = iter(self.chunk)
        self.print_chunk_and_lists()  #
        return self

    def get_iter_chunk(self):
        print('def get_iter_chunk(self):')  #
        self.iterations += 1
        iterable = True
        try:
            self.chunk = next(self.iter_list)
            print(f'try-{self.iterations}:')  #
            self.iter_chunk = iter(self.chunk)
        except StopIteration:
            print(f'except-{self.iterations}:')  #
            print(f'\t(simpler_list = {self.simpler_list}, iterations = {self.iterations}):')  #
            if self.lists == self.simpler_list:
                self.stop_iterations = True
            self.chunk = list(FlatIterator(self.simpler_list, self.stop_iterations, self.iterations))
        except TypeError:
            iterable = False
            self.iter_chunk = iter([])
        self.print_chunk_and_lists()  #
        return iterable

    def __next__(self):
        try:
            if self.stop_iterations:
                print('Список стал плоским!')
                raise StopIteration
            else:
                print('def __next__(self):')  #
                assert self.iterations < 100, 'СЛИШКОМ МНОГО ИТЕРАЦИЙ!'
                next_try = self.get_next_element()
                print(f'\tnext_try = {next_try}')  #
                self.simpler_list.append(next_try)
                print(f'\tsimpler_list-{self.iterations}: {self.simpler_list}')  #
                next_try = next(self.iter_chunk)
        except StopIteration:
            print('Список стал плоским!!!')
            next_try = next(self.iter_chunk)
        return next_try

    def get_next_element(self):
        try:
            next_el = next(self.iter_chunk)
            print(f'TRY-{self.iterations}:')  #
        except StopIteration:
            print(f'EXCEPT-{self.iterations}:')  #
            next_el = self.get_next_element() if self.get_iter_chunk() else self.chunk
            print(f'EXCEPT-{self.iterations}:')  #
        return next_el

    def print_chunk_and_lists(self):
        print(f'\tchunk-{self.iterations}: {self.chunk}')
        print(f'\tlists-{self.iterations}: {self.lists}')


def test_333():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print(list_of_lists_2)
    check_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    flat_iterator = FlatIterator(list_of_lists_2)
    flat_list = list(flat_iterator)
    print(flat_list)

    for flat_item, check_item in zip(flat_list, check_list):
        print(flat_item, flat_item == check_item, check_item)
        assert flat_item == check_item

    assert flat_list == check_list
