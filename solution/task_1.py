# ЗАДАНИЕ-4.1
# Доработать класс FlatIterator.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
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
        except StopIteration:
            try:
                self.chunk = next(self.iter_lists)
                self.iter_chunk = iter(self.chunk) if type(self.chunk) == list else iter([])
            except StopIteration:
                print('Список уплощен на один уровень!')    #
                self.chunk = []
                self.iter_chunk = iter([])
            next_try = next(self.iter_chunk) if type(self.chunk) == list else self.chunk
        print(f'\t{next_try}', end=", ")    #
        return next_try


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    check_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(list_of_lists_1)
    flat_list = list(FlatIterator(list_of_lists_1))

    for flat_item, check_item in zip(flat_list, check_list):
        print(flat_item, flat_item == check_item, check_item)
        assert flat_item == check_item

    assert flat_list == check_list
