#ninja blade

import turtle

screen = turtle.Screen()
screen.bgcolor("black")

bob = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
bob.speed(1)

for i in range(20):
        bob.color( colors[i%6] )
        bob.fd(120)
        bob.lt(90)
        bob.fd(130)
        bob.lt(180-45)
        
        
        
