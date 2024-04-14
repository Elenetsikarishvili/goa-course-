from turtle import * 

#we want to paint a house 

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup
forward(80)
color("blue")
left(90)

forward(100)
left(120)

forward(90)
left(90)

forward(30)
left(90)

forward(75)
left(90)

forward(50)
left(90)

forward(75)
left(90)

forward(25)
left(90)

forward(40)
left(85)

forward(25)
right(175)

forward(50)

exitonclick()







