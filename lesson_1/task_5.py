proceed = int(input('Сколько выручки у Вашей фирмы? '))
consumption = int(input('Сколько издержек у Вашей фирмы? '))
balance = proceed - consumption
rent = balance / proceed
if proceed > consumption:
    print('У Вас прибыль!')
    print('Рентабельность составила:', rent)
if proceed < consumption:
    print('У Вас проблемы с финансами!')
people = int(input('Сколько сотрудников в Вашей фирме? '))
balance_per_people = balance / people
print('Прибыль фирмы в расчете на одного сотрудника составила', balance_per_people)
