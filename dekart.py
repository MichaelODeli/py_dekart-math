# x^3+y^3=3axy
import numpy
from math import sin, cos, pi
import matplotlib.pyplot
from scipy import integrate

func = lambda p: (((cos(p))**2)*((sin(p))**2))/((((cos(p))**3)+((sin(p))**3))**2)  # вводим функцию, измененную в соответствии с полярными координатами, а также с вынесенным значением 'a'
answer = integrate.quad(func, 0, pi/4) # вычисляем интеграл в точках
newans=answer[1]-answer[0] # вычисляем площадь фигуры (большее из меньшего)
newans=round(-1*(newans*9), 1) # меняем знак ввиду некорректности решения встроенными модулями
newans=str(newans)
print(newans+"*a^2") #искомый интеграл - площадь фигуры

# graph
fig = matplotlib.pyplot.figure(figsize=(8., 6.)) # определяем область построения
phi = numpy.arange(0, 3, 0.001) # значения для фи - от, до, шаг
rho = (3 * numpy.sin(phi) * numpy.cos(phi))/(((numpy.sin(phi))**3)*((numpy.cos(phi))**3)) # первый график
ax1 = fig.add_subplot(projection='polar') # определяем область построения как полярная система координат
ax1.plot(rho, phi) # строим графики
ax1.grid(True) # отображаем на рисунке сетку
matplotlib.pyplot.show() # выводим изображение