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
phi = numpy.arange(pi/6, pi/3, 0.001) # значения для фи - от, до, шаг
rho = 2 * numpy.cos(phi)
rho2 = 4 * numpy.cos(phi)
matplotlib.pyplot.figure()
matplotlib.pyplot.polar(phi, rho)
matplotlib.pyplot.polar(phi, rho2)
matplotlib.pyplot.show() # выводим изображение

