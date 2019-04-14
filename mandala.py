import turtle

number_of_divisions = 8 
turtle_width = 5         


turtle.tracer(False)


turtle.color("gray")
for i in range(number_of_divisions):
    turtle.forward(500)
    turtle.backward(500)
    turtle.left(360 / number_of_divisions)
turtle.color("black")



allTurtles = []


turtle.width(turtle_width)
turtle.shape('circle')
turtle.shapesize(2,2)
allTurtles.append(turtle)

for i  in range(1,number_of_divisions):
    newTurtle=turtle.Turtle()
    newTurtle.width(turtle_width)
    newTurtle.hideturtle()
    allTurtles.append(newTurtle)
print(len(allTurtles))



xt = [1, 1, -1, -1, 1, 1, -1, -1] 
yt = [1, -1, 1, -1, 1, -1, 1, -1] 
def draw(x,y):
    turtle.ondrag(None)
    turtle.goto(x,y)
    for i in range(1,number_of_divisions):
        if i<4:
            new_x=x*xt[i]
            
            new_y=y*yt[i]
        else:
            
             new_y=x*xt[i]
            
             new_x=y*yt[i]
             
        allTurtles[i].goto(new_x,new_y)
       


    
    turtle.update()
    turtle.ondrag(draw)
turtle.ondrag(draw)

colours = ["black", "tomato", "spring green", "slate blue", "turquoise", "orchid", "gold"]


def click(x,y):
    if x<=-130:
        for thisTurtle in allTurtles:
            thisTurtle.color(colours[0])
    elif x<=-80:
        
            for thisTurtle in allTurtles:
                thisTurtle.color(colours[1])
    elif x<=-30:
        
            for thisTurtle in allTurtles:
                thisTurtle.color(colours[2])
    elif x<=20:
        
            for thisTurtle in allTurtles:
                thisTurtle.color(colours[3])
    elif x<=70:
        
            for thisTurtle in allTurtles:
                thisTurtle.color(colours[4])
    elif x<=120:
        
            for thisTurtle in allTurtles:
                thisTurtle.color(colours[5])
    elif x<=1700:
        
            for thisTurtle in allTurtles:
                thisTurtle.color(colours[6])
    turtle.update()


for i in range(len(colours)):
    newTurtle=turtle.Turtle()
    newTurtle.shape('square')
    newTurtle.shapesize(2,2)
    newTurtle.color(colours[i])
    newTurtle.up()
    newTurtle.goto(-150+50*i,-250)
 
    newTurtle.onclick(click)



turtle.update()

turtle.done()
