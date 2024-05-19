numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = [x ** 2 for x in numbers if x % 2]
print(result)


def f_1(x):
    return x ** 2


def f_2(x):
    return x % 2


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(f_1, filter(f_2, numbers))
print(list(result))
