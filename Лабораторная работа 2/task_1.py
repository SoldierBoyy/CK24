salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

month_capital = 0

for month in range(1, months + 1):
    if month > 1:
        spend *= (1 + increase)
        month_capital += spend - salary
    else:
        month_capital = spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(month_capital))
