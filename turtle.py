import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Color Loop")


artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()
artist.pensize(3)


def draw_petal(size, color):
   artist.color(color)
   artist.begin_fill()


for _ in range(2):
   artist.circle(size, 60)
   artist.left(120)


   artist.end_fill()


   colors = ["red", "orange", "yellow", "green"]


   for i in range(36):
       draw_petal(90, colors[i % len(colors)])
       artist.right(10)


       artist.penup()
       artist.goto(0, -25)
       artist.pendown()


       artist.color("white")
       artist.begin_fill()
       artist.circle(25)
       artist.end_fill()


       turtle.done()

