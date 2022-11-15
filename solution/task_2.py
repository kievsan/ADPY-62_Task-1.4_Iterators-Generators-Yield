# # ЗАДАНИЕ-4.2
# Доработать функцию flat_generator.
# Должен получиться генератор, который принимает список списков
# и возвращает их плоское представление.
# Функция test в коде ниже также должна отработать без ошибок.


import types
from collections.abc import Iterable


def flat_generator(list_of_lists, ignore_types=(str, bytes)):
    for chunk in list_of_lists:
        if isinstance(chunk, Iterable) and not isinstance(chunk, ignore_types):
            for elem in chunk:
                # print(f'\t{elem}', end=", ")    #
                yield elem
        else:
            # print(f'\t{chunk}', end=", ")   #
            yield chunk


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    check_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(list_of_lists_1)
    flat_list = list(flat_generator(list_of_lists_1))
    print(flat_list)

    for flat_item, check_item in zip(flat_list, check_list):
        print(flat_item, flat_item == check_item, check_item)
        assert flat_item == check_item

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
