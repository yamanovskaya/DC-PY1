def get_count_char(str_):
    alpha_str_ = [elem for elem in str_.lower() if elem.isalpha()]
    dict_ = {}
    for symbol in alpha_str_:
        if symbol not in dict_.keys():
            dict_[symbol] = 1
        else:
            dict_[symbol] += 1
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def normal(d):
    sum_value = sum(d.values())
    for key, value in d.items():
        d[key] = value/sum_value*100
    return d
