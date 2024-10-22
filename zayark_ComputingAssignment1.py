
########## Computing Assignment 1


import turtle# Constants (you can change these)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Computing Assignment 1"

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Create the turtle object
t = turtle.Turtle()
t.penup()

# ------------------
# Set the background color
t.screen.bgcolor("#00BFFF")


#### Input
## First, we will be asking how many nails does the user want to use

nails = int(screen.numinput("Nails", "How many nails do you want to use?"))
x = screen.numinput("X-coordinate","Enter the x-coordinate: ")
y = screen.numinput("Y-coordinate","Enter the y-coordinate: ")
t.penup()
t.color("red")
t.goto(x,y)
t.pendown()
t.dot(10,"blue")
prev_x, prev_y = x, y
###### Process   
for  i in range(nails-1):
        """after setting the coordinates of the first nail, use a for loop to ask for the coordinates
           one less than the number of nails the user has input"""
        
        x1 = screen.numinput("X co-ordinate", "Enter the x-co-ordinate: ")
        y1 = screen.numinput("Y co-ordinate", "Enter the y-co-ordinate: ")
        
    
        t.goto(x1,y1)
        t.dot(10,"blue")
        t.color("red")
        
        t.stamp()
t.goto(x,y) #connecting the last x,y coordinates with the very first x,y coordinates

import math
#### Calculating the cost
cost_board = 5
cost_nail = 0.12
cost_string_per_meter = 0.17

'''The cost of the string is calculated by importing math.sqrt() function, using the distance formula and dividing
   the calculated distance (pixels) by 32.
   The total cost is later calculated by adding the given cost values above.'''

distance = math.fabs((math.sqrt((prev_x-x1)**2-(prev_y-y1)**2)))
distance_in_meter = math.fabs(distance /32)
total_cost = cost_board + nails*0.12 + distance_in_meter*0.17

######### Output

print(f"Total cost is ${total_cost: .2f}")

       
        


# ------------------
# End of your code

# Make a clean exit
screen.exitonclick() 
turtle.done()
