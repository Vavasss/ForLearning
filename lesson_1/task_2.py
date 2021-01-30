num = int(input('Введите количество секунд: '))
hour = num // 3600
min = (num - hour * 3600) // 60
sec = num - (hour * 3600 + min * 60)
print('{:02d}:{:02d}:{:02d}'.format(hour, min, sec))
