import turtle

wn = turtle.Screen()
wn.setup(500, 600)
wn.bgcolor("black")

turtle = turtle.Turtle()
turtle.speed("fastest")
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
step = 100


def draw_square(length, angle):
    for i in range(0, step):
        for b in range(0, 4):
            turtle.color(colors[i % 6])
            turtle.forward(length + i)
            turtle.right(angle + b)


draw_square(100, 90)
