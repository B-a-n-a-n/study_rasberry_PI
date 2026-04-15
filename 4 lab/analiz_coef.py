import numpy as np
import matplotlib.pyplot as plt
import time

print("Получаем данные из файлов data.txt и settings.txt")
#обрабатываем данные из разных файлов

data = []
with open("40 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

with open("80 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

with open("120 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

with open("160 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

real_data = [40,80,120,160]
p = 0
for i in range(4):
    p += real_data[i] / data[i]
p = int(100*(p/4))/100
# построение графика
print("Строим график")
fig, ax = plt.subplots(figsize = (16,10), dpi = 300)
ax.plot(real_data, data, alpha=0.9, label= ("P = " + str(p) + " * (N-10)[Па]"), lw=0.6, c='b', mew=0.4, ms=10, marker = ".", markevery = 100, mfc = 'b', mec = 'b')

#настройка осей
plt.axis([35,165,400, 1700])
ax.minorticks_on()
ax.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей
font = 8
plt.title('Калибровачный график зависимости показаний АЦП от давления')
plt.xlabel('Давление [Па]')
plt.ylabel('Отсчеты АЦП')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig.savefig("graph.svg")
#plt.show()
