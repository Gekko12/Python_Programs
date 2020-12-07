# Python program to draw 
# Spiral Helix Pattern 
# using Turtle Programming 

import turtle 

loadWindow = turtle.Screen() 
loadWindow.bgcolor("blue")

turtle.speed(5) 

bob = turtle.Turtle()
bob.color("pink")

for i in range(20): 
	bob.circle(5*i) 
	bob.circle(-5*i) 
	bob.left(i) 

turtle.exitonclick() 

