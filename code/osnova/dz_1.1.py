# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.
duration = int(input('Seconds: '))

days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

print('Days: ', days, ',', 'Hours: ', hours, ',', 'Minutes: ', minutes, ',', 'Seconds: ', seconds, '.', sep='')