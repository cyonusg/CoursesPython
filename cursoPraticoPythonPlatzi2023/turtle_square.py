import turtle
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

window = turtle.Screen()
turtleInstants = turtle.Turtle()

for x in range(0,4):
    turtleInstants.forward(100)
    turtleInstants.right(90)
window.mainloop()
