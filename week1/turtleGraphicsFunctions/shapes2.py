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


def hexagon(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(6):
       forward(100)
       left(60)
    end_fill()


def octagon(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(8):
        forward(100)
        left(45)
        end_fill()


def star(size, color):
   fillcolor(color)
   begin_fill()
   for i in range(5):
       forward(size)
       left(72)
       forward(size)
       right(144)
   end_fill()


def draw_circle(color):
    fillcolor(color)
    begin_fill()
    circle(100)

    end_fill()


if __name__ == '__main__':
   draw_circle(size, color)
   draw_a_square(size, color)
   draw_an_equilateral_triangle(size, color)
   star(size, color)
   hexagon(size, color)
   octagon(size, color)
   pentagon(size, color)

   mainloop()
