# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_of_dicts = [{'bin': str(bin(num)), 'dec': num, 'hex': str(hex(num)), 'oct': str(oct(num))} for num in range(0, 16)]
pprint(list_of_dicts)
