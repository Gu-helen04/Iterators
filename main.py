nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, in_list):
        self.in_list = in_list

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        _in_list = sum(self.in_list, [])
        self.index += 1
        if self.index == len(_in_list):
            raise StopIteration
        return _in_list[self.index]


def flat_generator(nested_list):
    for index in nested_list:
        for internal_index in index:
            yield internal_index


if __name__ == '__main__':

    print('Задание 1')
    for element in FlatIterator(nested_list):
        print(element)
    print(f'**********************************\nЗадание 2')
    for element in flat_generator(nested_list):
        print(element)