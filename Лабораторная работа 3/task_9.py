salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

def m(a, b, c, d, e):
    while c > 0:
        r = b - a
        e = e + r
        b = b * (1 + d)
        c = c - 1
    print(round(e))
m(salary, spend, months, increase, need_money)
