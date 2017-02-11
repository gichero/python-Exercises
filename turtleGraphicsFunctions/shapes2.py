from turtle import *

def draw_a_square(size, color):
   fillcolor(color)
   begin_fill()
   for i in range(4):
       forward(size)
       left(90)
   end_fill()


def draw_an_equilateral_triangle(size, color):
   fillcolor(color)
   begin_fill()
   for i in range(2):
       forward(size)
       left(120)
   forward(size)
   end_fill()


def pentagon(size, color):
   fillcolor(color)
   begin_fill()
   for i in range(5):
       forward(size)
       left(72)
   end_fill()


def hexagon():
   for i in range(6):
       forward(100)
       left(60)


def octagon():
   for i in range(8):
       forward(100)
       left(45)


def star(size, color):
   fillcolor(color)
   begin_fill()
   for i in range(5):
       forward(size)
       left(72)
       forward(size)
       right(144)
   end_fill()


def draw_circle():
   circle(100)


if __name__ == '__main__':
   draw_circle()
   draw_a_square(size, color)
   draw_an_equilateral_triangle(size, color)
   star(size, color)
   hexagon()
   octagon()
   pentagon(size, color)

   mainloop()
