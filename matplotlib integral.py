import numpy
from math import sin, cos, pi
import matplotlib.pyplot
from scipy import integrate

# найдем интеграл на участке
func = lambda x: ((4*cos(x))**2)-((2*cos(x))**2) # вводим функцию
answer = integrate.quad(func, pi/6, pi/3) # вычисляем интеграл в точках
newans=answer[1]-answer[0] # вычисляем площадь фигуры (большее из меньшего)
newans=newans/2 # в соответствии с заданием, нужно разделить полученное значение пополам
print(round(newans, 4)) #искомый интеграл - площадь фигуры


# graph
fig = matplotlib.pyplot.figure(figsize=(8., 6.)) # определяем область построения
phi = numpy.arange(pi/6, pi/3, 0.01) # значения для фи - от, до, шаг
rho = 4 * (numpy.cos(phi))**2 - 2 * (numpy.cos(phi))**2 # первый график
# rho2 = 2 * numpy.cos(phi) # второй график
ax1 = fig.add_subplot(projection='polar') # определяем область построения как полярная система координат
ax1.plot(rho, phi) # строим графики
# ax1.plot(rho2, phi) # строим графики
ax1.grid(True) # отображаем на рисунке сетку
matplotlib.pyplot.show() # выводим изображение