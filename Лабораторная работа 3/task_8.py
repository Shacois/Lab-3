money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
a = 10000
b = 5000
c = 6000
d = 0.05
e = 0
def live(a, b, c, d, e):
    while a > c:
        r = c - b
        a = a - r
        c = c * (1 + d)
        e += 1
    print(e)
live(money_capital, salary, spend, increase, month)