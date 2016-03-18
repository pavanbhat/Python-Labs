"""
CSCI-603: Lab 3(week 3)
Section 03
Author: Pavan Prabahakar Bhat (pxb8715@rit.edu)
        Vinayak Marali (vkm7895@rit.edu)

This is a program is to draw a tree using recursion.
"""

#IMPORTS CALLED HERE
import turtle
import random

#validation for recursion depth
#flag = True
#while(flag):
recursionDepth = input("Please enter a value for the depth of recursion ")
if(recursionDepth.isnumeric()):
    # A COPY OF THE RECURSION DEPTH
    recursionDepth = int(recursionDepth)
    layers = recursionDepth
#   flag = False
else:
    print("Please enter a valid integer number above zero!")
    # will exit from here as all the validations have failed
    exit()


BRANCH_ANGLE = random.randint(20, 40)# causes right angle between two branches

#validation for overallSize value

# flag1 = True
# while(flag1):
overallSize = input("Please enter the value of the overall expected height of the tree ")
if(overallSize.isnumeric() and int(overallSize) > 0):
    overallSize = int(overallSize)
# flag1 = False
else:
    print("Please enter a valid positive integer!")
    exit()

# as the overallSize has to be approximately equal to the exact height
size = overallSize/2 # used as the size of trunk for the tree
# a copy of the size of trunk
trunkLength = size

#validation for bushiness value

bushiness = input("Please enter a floating point number between 0 and 1 to determine the bushiness of the tree: ")
dotCount = 0 #Count of the number of decimal point
numCount = 0 #Count of the numbers in the input string
notNum = 0 #Count of the  non numeric characters in the input string
numPos = 0 #Index of last number in the input string
decimalPos = 0 #Index of decimal point in the input string
for inputCharacter in bushiness:
    if bushiness[:2] == "0." or bushiness[:2] == "1.":
        if inputCharacter >= "0" and inputCharacter <= "9":
            numCount = numCount +1
            numPos = bushiness.index(inputCharacter)
        elif inputCharacter == ".":
            dotCount = dotCount + 1
            decimalPos = bushiness.index(inputCharacter)
    else:
        notNum = notNum + 1

if notNum > 0:
    print("Enter a valid float number between 0 to 1 eg: 0.5")
    exit()
elif dotCount == 1 and numPos >= decimalPos :
    if numCount == len(bushiness) -1:
        bushiness = float(bushiness)
elif dotCount == 0 and numPos >= decimalPos:
    if numCount == len(bushiness):
        bushiness = float(bushiness)
else:
    print("Enter a valid float number between 0 to 1 eg: 0.5")
    exit()


if(bushiness):
    # randomly generates the number of sub-branches depending on the bushiness value
    noOfSegments = random.randint(1, int(10*bushiness))
else:
    noOfSegments = 0

#validation for leafiness value

leafiness = input("Please enter a floating point number between 0 and 1 to determine the leafiness of the tree: ")
dotCount = 0 #Count of the number of decimal point
numCount = 0 #Count of the numbers in the input string
notNum = 0 #Count of the  non numeric characters in the input string
numPos = 0 #Index of last number in the input string
decimalPos = 0 #Index of decimal point in the input string
for inputCharacter in leafiness:
    if leafiness[:2] == "0." or leafiness[:2]=="1.":
        if inputCharacter >="0" and inputCharacter <="9":
            numCount = numCount +1
            numPos = leafiness.index(inputCharacter)
        elif inputCharacter==".":
            dotCount = dotCount + 1
            decimalPos = leafiness.index(inputCharacter)
    else:
        notNum = notNum + 1

if notNum > 0:
    print("Enter a valid float number between 0 to 1 eg: 0.5")
    exit()
elif dotCount == 1 and numPos>=decimalPos :
    if numCount == len(leafiness) -1:
        leafiness = float(leafiness)
elif dotCount == 0 and numPos>=decimalPos:
    if numCount == len(leafiness):
        leafiness = float(leafiness)
else:
    print("Enter a valid float number between 0 to 1 eg: 0.5")
    exit()


if(leafiness):
     # randomly generates the number of leaves depending on the leafiness value
    noOfLeafs = random.randint(1, int(50*leafiness))
else:
    noOfLeafs = 0



def drawTree( aTurtle, recursionDepth, size ):
    """ Recursively draw a tree.

        :param aTurtle: the turtle to be used to do the drawing

        :param size: positive integer
                    length of tree trunk

        :pre: turtle is at base of tree,
              turtle is facing along trunk of tree,
              turtle is pen-down.

        :post: turtle is at base of tree,
               turtle is facing along trunk of tree,
               turtle is pen-down.
    """
    aTurtle.pendown()
    if recursionDepth == 0:
        # base case: draws the leaves on the tree
        leafLength = trunkLength / 10
        for _ in range(noOfLeafs):
            aTurtle.color("Green")
            aTurtle.fd(leafLength)
            aTurtle.backward(leafLength)
            aTurtle.rt(3)
            aTurtle.color("Black")
        aTurtle.lt(3*noOfLeafs) # required to shift an angle at a relative initial position on the final twig
    elif(recursionDepth < layers):
        # recursive case: draws the trunk and the sub-branches
        aTurtle.forward( size )
        aTurtle.left( BRANCH_ANGLE )
        for _ in range(noOfSegments):
            segmentPosition = random.randint(0,round(size/2)) # chooses a random position to place the sub-branch
            aTurtle.fd(segmentPosition)
            direction = random.randint(0,1) # randomizes the direction in which the sub-branch is drawn
            if(direction == 0):
                aTurtle.lt(BRANCH_ANGLE)
            else:
                aTurtle.rt(BRANCH_ANGLE)
            aTurtle.fd(size/4) # allocates the size to the sub-branch drawn which is varying
            aTurtle.backward( size/4 )
            # required to come back to a relative position from where the branch began
            if(direction == 0):
                aTurtle.rt(BRANCH_ANGLE)
            else:
                aTurtle.lt(BRANCH_ANGLE)
            aTurtle.backward(segmentPosition)
        # required for recursing on the right side
        drawTree( aTurtle, recursionDepth - 1, size / 2 )
        aTurtle.right( 2*BRANCH_ANGLE )
        for _ in range(noOfSegments):
            segmentPosition = random.randint(0,round(size/2))
            aTurtle.fd(segmentPosition)
            direction = random.randint(0,1)
            if(direction == 0):
                aTurtle.lt(BRANCH_ANGLE)
            else:
                aTurtle.rt(BRANCH_ANGLE)
            aTurtle.fd(size/4)
            aTurtle.backward( size/4 )
            if(direction == 0):
                aTurtle.rt(BRANCH_ANGLE)
            else:
                aTurtle.lt(BRANCH_ANGLE)
            aTurtle.backward(segmentPosition)
        drawTree( aTurtle, recursionDepth - 1, size / 2 )
        aTurtle.left( BRANCH_ANGLE )
        aTurtle.backward( size )
    elif(recursionDepth == layers):
     # recursive case: Draws the trunk and the sub-branches
        aTurtle.forward( size )
     # generates a random number of branches between 1 and 4
        randomBranch = random.randint(1,4)
     #required to generate random branch angles
        randomFactor = random.randint(1,2)
        aTurtle.rt(2 * BRANCH_ANGLE)
        while randomBranch > 0:
            aTurtle.left( BRANCH_ANGLE )
            drawTree( aTurtle, recursionDepth - 1, size / 2 )
            aTurtle.right(randomFactor * BRANCH_ANGLE )
            drawTree( aTurtle, recursionDepth - 1, size / 2 )
            aTurtle.left( BRANCH_ANGLE )
            randomBranch = randomBranch -1
        aTurtle.setheading(90)
        aTurtle.backward( trunkLength )

MARGIN = 2 # Space at edges of canvas
PEN_SIZE = 2 # Thickness of turtle's pen

def initWorld( size ):
    """ Initialize the drawing area.

        :param size: integer
                     length of tree trunk to draw
                     (not currently used)
        :pre: size > 0
        :post: coordinate system goes from
               (-2*size, -2*size) at lower-left
                 to (2*size, 2*size) at upper-right.
    """

    turtle.setup( 600, 600 )

    # The lines below are removed because they keep one from
    # seeing the difference that the size parameter makes
    # in the perceived size of the tree.
    #
    turtle.setworldcoordinates( -2*size - MARGIN, -2*size - MARGIN, \
                                2*size + MARGIN, 2*size + MARGIN)


def initTurtle( aTurtle ):
    """ Set up the turtle by establishing the drawTree
        function's pre-conditions.

        :post: aTurtle is at origin ( center ),
               aTurtle is facing North,
               aTurtle's pen is down, size PEN_SIZE, aTurtle's speed is set to 0
    """

    aTurtle.home()  # turtle is at origin, facing east, pen-down
    aTurtle.left( 90 )  # turtle is facing North
    aTurtle.down()  # turtle's pen is put down
    aTurtle.pensize( PEN_SIZE )
    aTurtle.speed(0)




def main():
    """ Print a message, initialize the world,
        draw an instance of the recursive tree, and wait for ENTER
        t: turtle
        recursionDepth: depth of recursion
        size: positive integer
                    length of tree trunk
    """
    print("Drawing recursive tree with", (recursionDepth, size))
    initWorld( size )
    t = turtle.Turtle()
    initTurtle( t )
    drawTree( t, recursionDepth, size )
    input("Hit enter to exit...")

# calls the main function
if __name__ == '__main__':
    main()