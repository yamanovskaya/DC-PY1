from random import shuffle, randint


# def get_unique_list_numbers() -> list[int]:
#     '''Реализация через срезы и Comprehension'''
#     list_ = [n for n in range(-10, 11)]
#     #list_ = list(range(-10, 11))
#     list_ = list_[:15]
#     shuffle(list_)
#     return list_


def get_unique_list_numbers() -> list[int]:
    '''Реализация через последовательную генерацию элементов'''
    set_ = set()
    while len(set_) != 15:
        set_.add(randint(-10, 10))
    return list(set_)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
