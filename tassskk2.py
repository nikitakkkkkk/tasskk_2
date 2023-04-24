tickets = int(input("Введите количество билетов:\n"))
ages = []
for i in range(tickets):
    i += 1
    age = int(input(f"Введите возраст {i}-го посетителя:\n"))
    if age <= 0 or age >= 120:
        raise ValueError("Пожалуйста, введите корректный возраст")
    ages.append(age)

cost = 0
for age in ages:
    if age < 18:
        cost += 0
    elif 18 <= age < 25:
        cost += 990
    else:
        cost += 1390

if tickets > 3:
    cost = cost - cost * 0.1
    print("Итоговая сумма с учетом скидки равна", int(cost))
else:
    print("Итоговая сумма равна", cost)

