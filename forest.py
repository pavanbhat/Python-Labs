__author__ = 'Vinayak Marali'
__author__ = 'Pavan Prabhakar Bhat'

"""
CSCI-603: Lab 2 (week 2)
Section 03
Author: Pavan Prbahakar Bhat (pxb8715@rit.edu)
        Vinayak Marali (vkm7895@rit.edu)

This is a program that draws a forest with trees and a house.
"""

# Imports required by the program
import turtle
import random
import math

# global constants
UNIT = 50
# to store the height of trees
treeHt=[]


def init():
    """
    Inititializes the window for drawing. (1200,800) is the window setup
    :pre: (relative) pos(0,0), heading (east), up
    :post: relative position, heading (east), up
    :param: None
    :return: None
    """
    turtle.setup(1200, 800)
    turtle.penup()
    turtle.left(180)
    turtle.forward(10 * UNIT)
    turtle.left(90)
    turtle.forward(4 * UNIT)
    turtle.left(90)


def drawTrunk(size):
    """
    Draws the trunl of the trees on the screen
    :pre: (relative) position, heading (east), down
    :post: (relative) position, heading (east), up
    :param size: length of the tree trunk to be drawn
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.penup()
    turtle.right(180)
    turtle.forward(size)
    turtle.left(90)


def drawSpace():
    """
    Draws a space between the trees or between a house and a tree.
    :pre: (relative) position, heading (east), up
    :post: (relative) position, heading (east), up
    :param: None
    :return: None
    """
    turtle.penup()
    turtle.forward(2 * UNIT)


def drawTree(treeNo, isHouse, houseNo):
    """
    Draws the tree on the screen
    :pre: (relative) position, heading (east), up
    :post: (relative) position, heading (east), up
    :param treeNo: constant required to build the walls and roof of the house
    :param isHouse: a boolean value which determines whether the house is required or not by the user
    :param houseNo: a value required to determine the position of the house
    :return: wood required to build the tree
    """

# counts the number of trees that are printed
    count = 0
    flag = 0

    while treeNo > 0:
# Required to generate a random type of tree
        randomtree = random.randint(1, 3)

        if randomtree == 1:
            trunkheight = UNIT * random.randint(1, 2)
            treeHt.append(trunkheight)
            drawTrunk(trunkheight)
            turtle.left(90)
            turtle.forward(trunkheight)
            turtle.left(90)
            turtle.penup()
            turtle.forward(0.5 * UNIT)
            turtle.pendown()
            turtle.right(120)
            turtle.forward(UNIT)
            turtle.right(120)
            turtle.forward(UNIT)
            turtle.right(120)
            turtle.penup()
            turtle.forward(0.5 * UNIT)
            turtle.penup()
            turtle.left(90)
            turtle.forward(trunkheight)
            turtle.left(90)
            drawSpace()
            count = count + 1
        elif randomtree == 2:
            trunkheight = UNIT * random.randint(1, 3)
            treeHt.append(trunkheight)
            drawTrunk(trunkheight)
            turtle.left(90)
            turtle.forward(trunkheight)
            turtle.right(90)
            turtle.pendown()
            turtle.circle(0.5 * UNIT)
            turtle.penup()
            turtle.right(90)
            turtle.forward(trunkheight)
            turtle.left(90)
            drawSpace()
            count = count + 1
        elif randomtree == 3:
            trunkheight = UNIT * random.randint(1, 4)
            treeHt.append(trunkheight)
            drawTrunk(trunkheight)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(trunkheight)
            turtle.left(90)
            turtle.forward(0.5 * UNIT)
            turtle.right(120)
            turtle.forward(UNIT)
            turtle.right(120)
            turtle.forward(UNIT)
            turtle.right(120)
            turtle.forward(0.5 * UNIT)
            turtle.penup()
            turtle.left(90)
            turtle.forward(trunkheight)
            turtle.left(90)
            drawSpace()
            count = count + 1

        if isHouse == 'y' and count == houseNo and flag == 0:
            flag = 1
            hlumber = drawHouse(50)
            drawSpace()

        treeNo = treeNo - 1
    return sum(treeHt)


def drawHouse(unit):
    """
    Draws the house on the screen
    :pre: (relative) pos (0,0), heading (east), down
    :post: (relative) pos (0,0), heading (east), up
    :param unit: constant required to build the walls and roof of the house
    :return: wood required to build the house
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(2 * unit)
    turtle.right(45)
    turtle.forward(unit * math.sqrt(2))
    turtle.right(90)
    turtle.forward(unit * math.sqrt(2))
    turtle.right(45)
    turtle.forward(2 * unit)
    turtle.left(90)
    turtle.penup()
    return 2 * unit + unit * math.sqrt(2) + unit * math.sqrt(2) + 2 * unit


def drawstar(hStar):
    """
    Draws the star on the screen
    :pre: (relative) pos (0,0), heading (east), down
    :post: (relative) pos (0,0), heading (east), down
    :param hStar: height of star
    :return: None
    """
    turtle.left(90)
    turtle.forward(hStar)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(45)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(20)


def drawSun():
    """
    Draws the sun on the screen
    :pre: (relative) position, heading (east), down
    :post: (relative) position, heading (east), down
    :param: None
    :return: None
    """
    turtle.pendown()
    turtle.circle(15)


def main():
    """
    The main function.
    :pre: (relative) pos (0,0), heading (east)
    :post: (relative) pos (0,0), heading (east)
    :return: None
    """
# the lumber required by the house
    hlumber = 0
    turtle.bgcolor('black')
    turtle.pencolor('white')
    init()

# Number of trees required by the user
    treeNo = int(input('Enter the number of trees '))
    isHouse = input('Is there a house in the forest (y/n)? ')
# generates the house at random locations
    if isHouse == 'y':
        if treeNo >=2 :
            houseNo = random.randint(1, treeNo-1)
        else:
            print('There have to be atleast 2 trees for the house to be printed')
            houseNo = 0
        tlumber = drawTree(treeNo, isHouse, houseNo)
        hlumber = 2 * 50  + 50 * math.sqrt(2) + 50 * math.sqrt(2) + 2 * 50
    else:
        tlumber = drawTree(treeNo, isHouse, 0)

# draws the star 10 pixels higher than the highest tree
    hStar = max(treeHt) + UNIT + 10
    drawstar(hStar)

# Total lumber from the trees and the house
    lumber = hlumber + tlumber
    wallht = lumber/(2 + math.sqrt(2))
    input('Night is done, press enter for day')
    turtle.reset()
    init()
    turtle.bgcolor('white')
    turtle.pencolor('black')
    input('We have ' + str(lumber) + ' units of lumber for the building.')
    input('We will build a house with walls ' + str(wallht) + ' tall.')
    drawHouse(wallht/2)
    drawSpace()
    turtle.left(90)
    turtle.forward(wallht * 2)
    drawSun()
    input('Day is done, house is built, press enter to quit')


# Calling the main function
if __name__ == '__main__':
    main()
