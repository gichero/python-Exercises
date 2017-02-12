import matplotlib.pyplot as plot


def fahrenheit(c):
    
    return (c * 1.8) + 32

xs = range(0, 100)
ys = []

for c in xs:
    ys.append(fahrenheit(c))
plot.plot(xs, ys)
plot.show()
