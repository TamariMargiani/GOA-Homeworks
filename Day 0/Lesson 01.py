from turtle import *


#we want to paint a house

#step 1: draw a square


width(7)
color("gray")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()

left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)

end_fill()

#drawing a roof

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
goto(0, 0)
pendown()

right(150)
color("gray")
forward(90)
color("yellow")

right(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)

penup()
goto(200, 0)
pendown()

right(180)
color("gray")
forward(90)
color ("yellow")
left(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)

right(90)
forward(25)
right(90)
forward(60)
right(90)
forward(25)
right(90)
forward(30)
right(90)
forward(50)

penup()
goto(0, 120)
pendown()

right(180)
forward(50)

penup()
goto(25, 90)
pendown()

left(90)
forward(60)

penup()
goto(0, 0)
pendown()

color("green")
begin_fill()
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(400)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

penup()
goto(75, 0)
pendown()

color("gray")
begin_fill()
left(90)
forward(20)
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)

left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
end_fill()

left(90)
forward(20)
left(90)
forward(50)

begin_fill()
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
end_fill()


exitonclick()
