# ЗАДАНИЕ-4.3
# Доработать класс FlatIterator.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов,
# обрабатывающий списки с любым уровнем вложенности.
# Функция test также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_lists):
        self.lists = list_of_lists
        self.chunk = []

    def __iter__(self):
        self.iter_lists = iter(self.lists) if type(self.lists) == list else iter([])
        self.iter_chunk = iter(self.chunk)
        return self

    def __next__(self):
        try:
            next_try = next(self.iter_chunk)
            print(f'\t1) chunk = {self.chunk} - {type(self.chunk)}, \tnext_try = {next_try} - {type(next_try)}')
        except StopIteration:
            try:
                self.chunk = next(self.iter_lists)
                print(f'\t2) chunk = {self.chunk} - {type(self.chunk)}', end=", ")
                self.iter_chunk = iter(self.chunk) if type(self.chunk) == list else iter([])
            except StopIteration:
                print(f'Список {self.lists} уплощен!')
                self.chunk = []
                self.iter_chunk = iter([])
            next_try = next(self.iter_chunk) if type(self.chunk) == list else self.chunk
            print(f'\tnext_try = {next_try} - {type(next_try)}')
        if type(next_try) == list:
            print(f'\t\tбудем уплощать список {next_try}')
            return list(FlatIterator(next_try))
        print(f'Возвращаем next_try: {next_try}')
        return next_try


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    # list_of_lists_2 = [[[[['!']]]]]

    check_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(list_of_lists_2)
    flat_list = list(FlatIterator(list_of_lists_2))
    print(flat_list)

    for flat_item, check_item in zip(flat_list, check_list):
        print(flat_item, flat_item == check_item, check_item)
        assert flat_item == check_item

    assert flat_list == check_list
