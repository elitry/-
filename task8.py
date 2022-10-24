money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
while money_capital > spend:
    month += 1
    spend = spend + spend * increase
    money_capital = (money_capital - spend) + salary
print(month)