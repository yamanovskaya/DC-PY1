import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    list_ = []
    with open(file, 'r', encoding='utf-8') as f:  # TODO реализовать конвертер из csv в json
        keys_string = f.readline()
        keys = keys_string.rstrip('\n').split(',')
        for values_string in f.readlines():
            values = values_string.rstrip('\n').split(',')
            list_.append(dict(zip(keys, values)))
        return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
