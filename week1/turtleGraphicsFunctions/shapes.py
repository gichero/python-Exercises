from turtle import *

def draw_a_square():
   for i in range(4):
       forward(100)
       left(90)

# draw_a_square()
# mainloop()

def draw_an_equaliteral_triangle():
   for i in range(2):
       forward(100)
       left(120)
   forward(100)

# draw_an_equaliteral_triangle()
# mainloop()

def pentagon():
   for i in range(5):
       forward(100)
       left(72)

# pentagon()
# mainloop()

def hexagon():
   for i in range(6):
       forward(100)
       left(60)

# hexagon()
# mainloop()

def octagon():
   for i in range(8):
       forward(100)
       left(45)

# octagon()
# mainloop()

def star():
   for i in range(5):
       forward(150)
       right(144)

# star()
# mainloop()

def draw_circle():
   circle(100)

# draw_circle()
# mainloop()
if __name__ == '__main__':
    draw_circle()
    draw_a_square()
    draw_an_equaliteral_triangle()
    star()
    hexagon()
    octagon()
    pentagon()
    
