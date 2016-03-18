__author__ = 'Pavan'

"""
CSCI-603: Intro Lecture (week 1)
Section
Author: Pavan Prbahakar Bhat

This is a demo program that draws several Python heads. It demonstrates
the importance of using a hierarchy of functions that can be re-used.
"""

# modules required by the program imported here
import turtle
import math

# global variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200
unit = 50
slant_angle = math.degrees(math.asin((unit / 2) / math.hypot(unit, (unit / 2))))


def init():
    """
    Inititialize for drawing. (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos(-250,30), heading (east), up
    :post: pos(-250,30), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.title('Project to print U. Pavan Bhat')
    turtle.setpos(-250, 30)
    turtle.pensize(3)
    turtle.bgcolor("lightgreen")
    turtle.shape("turtle")
    turtle.speed(5);

def drawU():
    """
    This method prints the character U.
    :pre: (relative) pos(0,0), heading (east), up
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.setheading(90)
    turtle.fd(unit)
    turtle.up()
    turtle.setheading(-90)
    turtle.fd(unit)
    turtle.down()
    turtle.setheading(0)
    turtle.fd(unit)
    turtle.lt(90)
    turtle.fd(unit)
    turtle.up()
    for _ in range(2):
        turtle.lt(90)
        turtle.fd(unit)
    turtle.setheading(90)

def drawCircle():
    """
    This method prints a dot for the initials.
    :pre: (relative) pos(0,0), heading (east), up
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.fd(3)
    turtle.down()
    turtle.pensize(5)
    turtle.circle(0)
    turtle.pensize(3)
    turtle.up()
    turtle.fd(25)
    turtle.setheading(90)

def drawP():
    """
    This method prints the character P.
    :pre: (relative) pos(0,0), heading (east), down
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.setheading(90)
    turtle.forward(unit)
    turtle.right(90)
    turtle.forward(unit)
    turtle.right(90)
    turtle.forward(unit / 2)
    turtle.right(90)
    turtle.forward(unit)
    turtle.lt(90)
    turtle.up()
    turtle.fd(unit / 2)
    turtle.setheading(90)


def drawA():
    """
    This method prints the character A.
    :pre: (relative) pos(0,0), heading (east), down
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.fd(unit)
    turtle.rt(90)
    turtle.fd(unit)
    turtle.setheading(-90)
    turtle.fd(unit)
    turtle.setheading(90)
    turtle.up()
    turtle.fd(unit / 2)
    turtle.lt(90)
    turtle.down()
    turtle.fd(unit)
    turtle.lt(90)
    turtle.up()
    turtle.fd(unit / 2)
    turtle.setheading(90)


def drawV():
    """
    This method prints the character V.
    :pre: (relative) pos(0,0), heading (east), up
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.up()
    turtle.fd(unit)
    turtle.setheading(-90 + slant_angle)
    turtle.down()
    turtle.fd(math.hypot(unit, (unit / 2)))
    turtle.setheading(0)
    turtle.setheading(90 - slant_angle)
    turtle.fd(math.hypot(unit, (unit / 2)))
    turtle.up()
    turtle.setheading(-90)
    turtle.fd(unit)
    turtle.rt(90)
    turtle.fd(unit)
    turtle.setheading(90)



def drawN():
    """
    This method prints the character N.
    :pre: (relative) pos(0,0), heading (east), down
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.fd(unit)
    turtle.down()
    turtle.setheading(-45)
    turtle.fd(math.sqrt(2) * unit)
    turtle.setheading(90)
    turtle.fd(unit)
    turtle.up()
    turtle.setheading(-90)
    turtle.fd(unit)
    turtle.rt(90)
    turtle.fd(unit)
    turtle.setheading(90)

def drawB():
    """
    This method prints the character B.
    :pre: (relative) pos(0,0), heading (east), down
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.fd(unit)
    turtle.rt(90)
    turtle.fd(unit)
    turtle.rt(90)
    turtle.fd(unit / 2)
    turtle.rt(90)
    turtle.fd(unit)
    turtle.up()
    turtle.setheading(0)
    turtle.fd(unit)
    turtle.rt(90)
    turtle.down()
    turtle.fd(unit / 2)
    turtle.rt(90)
    turtle.fd(unit)
    turtle.setheading(90)
    turtle.up()



def drawH():
    """
    This method prints the character H.
    :pre: (relative) pos(0,0), heading (east), down
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.fd(unit)
    turtle.up()
    turtle.setheading(-90)
    turtle.fd(unit / 2)
    turtle.lt(90)
    turtle.down()
    turtle.fd(unit)
    turtle.up()
    turtle.lt(90)
    turtle.fd(unit / 2)
    turtle.down()
    turtle.setheading(-90)
    turtle.fd(unit)
    turtle.up()
    turtle.rt(90)
    turtle.fd(unit)
    turtle.setheading(90)

def drawT():
    """
    This method prints the character T.
    :pre: (relative) pos(0,0), heading (east), up
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.up()
    turtle.fd(unit)
    turtle.rt(90)
    turtle.down()
    turtle.fd(unit)
    turtle.setheading(180)
    turtle.up()
    turtle.fd(unit / 2)
    turtle.lt(90)
    turtle.down()
    turtle.fd(unit)
    turtle.rt(90)
    turtle.up()
    turtle.fd(unit / 2)
    turtle.setheading(90)

def drawSpace():
    """
    This method prints a space between two characters.
    :pre: (relative) pos(0,0), heading (east), up
    :post:(relative) pos(0,0), heading (east), up
    :return: None
    """
    turtle.up()
    turtle.rt(90)
    turtle.fd(25+unit)
    turtle.lt(90)


def drawName():
    """
    This method prints the entire name
    :return: None
    """
    # prints the initials
    drawU()

# Required to position the dot slightly away from the first character
    turtle.rt(90)
    turtle.fd(unit+3)
    drawCircle()

# prints the characters in the first name
    drawP()
    drawSpace()
    drawA()
    drawSpace()
    drawV()
    drawSpace()
    drawA()
    drawSpace()
    drawN()
    drawSpace()

# the following code is required to print the Last name on the next line
    turtle.setheading(180)
    turtle.fd(7.5 * unit)
    turtle.lt(90)
    turtle.fd(1.5 * unit)
    turtle.setheading(90)

# prints the characters in the last name
    drawB()
    drawSpace()
    drawH()
    drawSpace()
    drawA()
    drawSpace()
    drawT()
    drawSpace()


def main():
    """
    The main function
    :pre: (relative) pos(0,0), heading (east), up
    :post: (relative) pos(0,0), heading (east), up
    :return: None
    """

# Sets the initial parameters required to initialize turtle
    init()

# prints the characters in your name
    drawName()

# hides the turtle on the screen
    turtle.ht()
# Waits for a click on the screen to exit
    turtle.exitonclick()

    #input("Press enter to exit the screen!!")

if __name__ == '__main__':
    main()
