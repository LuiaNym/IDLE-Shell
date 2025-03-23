import turtle 
import random 
turtle.title("Program Random Dots") 
turtle.setup(500, 500)

for _ in range(100): # make it 10000 
    # choose a random spot 
    xpos = random.randint(-200,200) 
    ypos = random.randint(-200,200) 
    # goto this spot 
    turtle.penup() 
    turtle.goto(xpos, ypos) 
    turtle.pendown() 
    turtle.dot(5, "red")
