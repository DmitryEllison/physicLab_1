from matplotlib import pyplot as plt
import math

file = open('times.txt', 'r')
arr = []
for i in file:
    arr.append(i.split())
arr = [float(i[0]) for i in arr]
kf = 7
out = [0]*kf

# Дробим диапазон от минимального до максимально на kf частей
delta = (max(arr) - min(arr)) / kf
xout = [min(arr)+i*delta for i in range(kf)]

# Считаем сколько чисел входит в каждый диапазон
for i in arr:
    out[int((i - min(arr) ) // delta)] += 1;
print(out)

# Выводим границы диапазона для таблицы 2
for i in range(kf+1):
    print(round(min(arr) + delta*i, 3), end=", ")
print("MAX_ARR -", max(arr))

# Остальные данные для таблицы 2
for i in out:
    print(round(i/(len(arr)*delta), 3), end=", ")

# Находим tN
tN = 0
for i in arr:
    tN += i
tN /= len(arr)

# Находим qN
qN = 0
for i in arr:
    qN += (i - tN)**2
#print("qN for spreadsheet- ",qN)
qN = (qN/(len(arr)-1))**0.5
Pmax = 1/(qN*(2*math.pi)**0.5)

# Поиск количества чисел которые входят в диапазаоны из таблицы 3
k1, k2, k3 = 0,0,0
print("\n", tN, qN)
for i in arr:
    if i > tN - 3*qN and i < tN + 3*qN:
        k3 += 1
    if i > tN - 2*qN and i < tN + 2*qN:
        k2 += 1
    if i > tN - qN and i < tN + qN:
        k1 += 1
print(k1, k2, k3)

# Нормальное распределение описываемое функцией Гаусса
print("\nНормальное распределение: ")
for i in xout:
    print(round(Pmax*math.exp(-(i+delta/2 - tN)**2 / (2*qN**2)), 3), end=", ")

print("\ntN, qN, Pmax: ",round(tN, 3), round(qN, 3), round(Pmax, 3))

# Запись таблицы 1 для лаборатоной
data = open("DATA.txt", 'w')
for i in arr:
    cell = i - tN
    #print(str(i) + ' ' + str(round(cell, 3)) + " " + str(round(cell**2, 3)) + "\n")
    data.write(str(i) + ' ' + str(round(cell, 3)) + " " + str(round(cell**2, 3)) + "\n")
file.close()
data.close()

# Строим гистограмму
plt.ylabel = "Point"
plt.xlabel = "Time"
plt.bar(xout, out, color="grey",  linestyle='solid', width= 0.1)

arrGauss = [Pmax*math.exp(-(x-tN)**2 / (2*qN**2)) for x in arr]
#plt.scatter(arr, arrGauss)
plt.show()