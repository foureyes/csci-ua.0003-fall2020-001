"""
recursive.py
"""
def count_nested_tuple(t):
    pass


if __name__ == '__main__':
    print(count_nested_tuple((1,)))
    print(count_nested_tuple((1, 2)))
    print(count_nested_tuple((1, (2, 3))))
    print(count_nested_tuple((1, (2, 3), 4)))
    print(count_nested_tuple((1, (2, 3, (4, 5)))))
    print(count_nested_tuple((1, (2, 3, (4, 5), 6))))
    print(count_nested_tuple(nested_t))
