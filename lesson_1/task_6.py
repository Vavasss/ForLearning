first_distance = int(input("Введите результаты пробежки первого дня в км: "))
wish_distance = int(input("Желаемый результат спортсмена в км: "))
result_days = 1
result_km = first_distance
while result_km < wish_distance:
    first_distance = first_distance + 0.1 * first_distance
    result_days += 1
    result_km = result_km + first_distance
print(f"Спортсмен достигнет желаемых результатов на %.d день" % result_days)
