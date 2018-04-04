'''
************************
NJIT SPRING 2018
CS104
Rashidbek Sadriddinov
Home Work 2, 02/17/2018
************************

1. Write a program that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon, each with side length 100.
2. Write a program that uses turtle graphics to draw four concentric circles or radius 50, 100, 150 and 200.

'''
import turtle
import time
turtle.setup(1000,800)
tello=turtle.Turtle()
tello.screen.bgcolor('#FF0F00') #fill background color with NJIT's logo red color code. 



#intro visuals
#First:Turtle Appearence 
tello.shape('turtle')
tello.color('white')
tello.speed(3)
print(range(5, 68, 4))
tello.up()                 
for size in range(5, 68, 2):  
    tello.stamp()                
    tello.forward(size)
    tello.right(24)
#pause for one sec
time.sleep(1)
tello.clear()
tello.hideturtle()
time.sleep(1)
tello.speed(100)
tello.shape('classic')
tello.up()
tello.goto(0, 40)
tello.down()
#Second: Show title text
tello.write('NJIT Spring 2018', False, 'center', font=('Arial', 28, 'bold'))
tello.up()
tello.goto(0, 0)
tello.down()
tello.write('CS104', False, 'center', font=('Arial', 24))
time.sleep(3)
tello.clear()
tello.write('Rashidbek Sadriddinov', False, 'center', font=('Arial', 26))
time.sleep(2)
tello.clear()
tello.write('Home Work #2', False, 'center', font=('Arial', 26))
time.sleep(3)
tello.clear()
time.sleep(1)
tello.up()
tello.goto(0, 40)
tello.down()
tello.color('black')
tello.write('Part I', False, 'center', font=('Arial', 26, 'bold'))
time.sleep(1)
tello.up()
tello.goto(0, 0)
tello.down()
tello.color('white')
tello.write('Draw an equilateral triangle, a square and a regular pentagon, each with side length 100. ', False, 'center', font=('Arial', 18))
time.sleep(8)
tello.clear()
tello.screen.bgcolor('white')
tello.speed(5)


tello.reset()
tello.up()
tello.goto(-210,0)
tello.down()
tello.speed(5)

tello.color('black', 'red')
tello.width(2)

tello.up()
tello.goto(-210,0)
tello.down()
tello.speed(2)
#Draw Equilateral Triangle
tello.begin_fill()
for i in range (3):
    tello.left(360/3)
    tello.fd(100)
tello.end_fill()

tello.up()
tello.goto(10,200)
tello.down()

#Draw Square
tello.color('black', 'green')
tello.begin_fill()
for i in range (4):
    tello.left(360/4)
    tello.fd(100)
tello.end_fill()

tello.up()
tello.goto(250,0)
tello.down()


#Draw Regular Pentagon
tello.color('black', 'blue')
tello.begin_fill()
for i in range (5):
    tello.left(360/5)
    tello.fd(100)
tello.end_fill()
tello.hideturtle()
time.sleep(6)
tello.clear()

#Part II
#Background color change and show the title
tello.screen.bgcolor('#FF0F00')
tello.up()
tello.goto(0,40)
tello.down()
tello.color('black')
tello.write('Part II', False, 'center', font=('Arial', 26, 'bold'))
time.sleep(1)
tello.up()
tello.goto(0, 0)
tello.down()
tello.color('white')
tello.write('Draw four concentric circles with radiuses 50, 100, 150 and 200. ', False, 'center', font=('Arial', 18))
time.sleep(8)

tello.clear()
tello.screen.bgcolor('white')
time.sleep(1)

#Draw four concentric circles with radiuses 50, 100, 150 and 200.
#Circle r50
tello.up()
tello.goto(0,0)
tello.down()
tello.width(4)
tello.color('purple')
tello.circle(50,None,None)
tello.screen.bgcolor('black')
tello.screen.bgcolor('white')
time.sleep(1)

#Circle r100
tello.up()
tello.goto(0,-50)
tello.down()
tello.color('yellow')
tello.circle(100,None,None)
time.sleep(1)
#Circle r150
tello.up()
tello.goto(0,-100)
tello.down()
tello.color('green')
tello.circle(150,None,None)
time.sleep(1)
#Circle r200
tello.up()
tello.goto(0,-150)
tello.down()
tello.color('red')
tello.circle(200,None,None)

#After drawing last circle show 'Eurikaaa!' text and make the screen flicker.
tello.up()
tello.goto(0,-250)
tello.down()

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))

tello.screen.bgcolor('black')
tello.color('white')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.screen.bgcolor('white')
tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(0.2)

tello.color('black')
tello.write('Eurika!', False, 'center', font=('Arial', 48, 'bold'))
time.sleep(2)


#outro visuals
tello.clear()
tello.screen.bgcolor('#FF0F00')
tello.up()
tello.goto(0,40)
tello.down()
tello.color('black')
tello.write('rs865@njit.edu', False, 'center', font=('Arial', 32))
time.sleep(3)
tello.clear()

'''
#turtles going inward
tello.shape('turtle')
tello.color('white')
tello.hideturtle()
tello.speed(100)
print(range(5, 68, 2))
tello.up()                 
for size in range(5, 68, 2):  
    tello.forward(size)
    tello.right(24)
tello.showturtle()
tello.left(118)
tello.speed(2)
print(range(68, 5, -2))
tello.up()   
for i in range(68, 5, -2):
    tello.stamp()
    tello.forward(i)
    tello.left(24)
'''
















