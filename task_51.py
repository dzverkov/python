# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

from collections import Counter

companies = Counter()

comp_n = int(input("Введите количество предприятий:"))

for i in range(comp_n):
    comp_name = input("Введите наименование предприятия:")
    comp_revenue = input("Введите доход предприятия по кварталам (4 целых числа, разделённые пробелом):").split()
    companies[comp_name] = sum([int(item) for item in comp_revenue])

# средний доход предприятий
avg_revenue = sum([comp_rev for comp_rev in companies.values()])/len(companies)

print("Средний доход предприятий: {:.2f}".format(avg_revenue))

print("Предприятия с прибылью выше среднего:")
t_exists = False
for comp in companies.most_common():
    if comp[1] < avg_revenue and not t_exists:
        print("Предприятия с прибылью ниже среднего:")
        t_exists = True
    print(f"{comp[0]}: R={comp[1]}")
