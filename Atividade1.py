import matplotlib.pyplot as pp
import numpy as np
import math

# 1 - funcao seno
a = np.arange(0, 4 * np.pi, 0.1)
b = np.sin(a)

pp.subplot(231)
pp.title("Seno")
pp.plot(a, b, 'r--')

# 2 - grafico cardióide
t = np.arange(0, 2 * np.pi, 0.1)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

pp.subplot(232)
pp.title("Cardióide")
pp.plot(x, y, 'r+')

# 3 - funcao quadratica (parabola)
eixo_x = []
eixo_y = []

for x1 in range(-8, 9, 1):
    y1 = x1 ** 2
    eixo_x.append(x1)
    eixo_y.append(y1)

pp.subplot(233)
pp.title("Função Quadrática")
pp.plot(eixo_x, eixo_y, "b--")

# 4 - bicorn
eixo_x = []
eixo_y = []

a = 1

for t in np.arange(0, 2 ** np.pi, 0.1):
    x = a * math.sin(t)
    p1 = a * ((math.cos(t)) ** 2) * (2 + math.cos(t))
    p2 = 3 + ((math.sin(t)) ** 2)
    y = p1 / p2
    eixo_x.append(x)
    eixo_y.append(y)

pp.subplot(234)
pp.title("Bicorn")
pp.plot(eixo_x, eixo_y, 'ro')

# 5 - dente de serra
a = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
b = 2 * (np.sin(a))

for n in range(2, 1002, 1):
    b = b - 2 * ((-1) ** n / n) * np.sin(n * a)

pp.subplot(235)
pp.title("Dente de Serra")
pp.plot(a, b)
pp.show()