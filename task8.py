money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


# TODO Оформить решение
def count(money_capital0, salary0, spend0, increase0):
    global month
    while money_capital0 > 0:
        money_capital0 = money_capital0 - spend0
        spend0 = spend0 * (1 + increase0)
        if money_capital0 > 0:
            month += 1
        else:
            break
        money_capital0 += salary0


count(money_capital, salary, spend, increase)
print(month)
