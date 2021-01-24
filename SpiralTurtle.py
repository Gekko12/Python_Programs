"""
Building a square root spiral using turtle.
"""

import turtle

def fibo() :
    fir = 0
    sec = 1
    third = fir + sec

    print("Enter a number where series goes upto :")
    x = int(input())

    print(fir , end = "  ")
    print(sec , end = "  ")
    for i in range(x-2):
        print(third , end = "  ")  #end = " " is used to avoid newline as newline is feed to end
        fir = sec
        sec = third
        third = fir + sec


bob = turtle.Turtle()

move = 200 # one unit of move
rainbow = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
degree = 45
i = 1

bob.fd(move)
bob.left(90)
bob.fd(move)

while i < 1000:
    bob.color(rainbow[i % 7])
    bob.left(45)
    bob.fd(move)


quit(0)
