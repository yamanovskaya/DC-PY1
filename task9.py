salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


# TODO Оформить решение
def count(mon):
    for i in range(mon):
        global need_money
        need_money = need_money + salary - spend * ((1 + increase) ** i)
    need_money = -need_money


count(months)
print(round(need_money))
