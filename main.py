# Домашнее задание к лекции 4
# «Iterators. Generators. Yield»

from solution.task_1 import test_1
from solution.task_2 import test_2
from solution.task_3 import test_3
from solution.task_4 import test_4
# from solution.task_333 import test_333


def print_task_header(title, n=25):
    print('\n', '-' * n, 'ЗАДАНИЕ-' + title, '-' * n)


if __name__ == '__main__':
    print_task_header('2')
    test_2()
    print_task_header('4')
    test_4()
    print_task_header('1')
    test_1()
    print_task_header('3')
    test_3()
    # print_task_header('333')
    # test_333()
