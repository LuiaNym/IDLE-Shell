import turtle
import random
import math

# Set screen and drawing area
canvas_size = 500
screen = turtle.Screen()
screen.setup(width=canvas_size, height=canvas_size)
screen.tracer(0)  # Turn off tracer to speed up drawing

# Start turtle
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

# Circle diameters and color list
radii = [5, 10, 15, 20, 25, 30]
colors = ["black", "indigo", "dimgray", "pink", "hotpink", "deeppink", "silver", "lavenderblush"]

# Store circle positions and radii to check overlapping
circles = []

def is_overlapping(x, y, radius):
    for cx, cy, cr in circles:
        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius + cr + -1 :  ### Overlap Control
            return True
    return False

# Try to draw 800 circles without overlapping in random positions and colors
for _ in range(800):
    radius = random.choice(radii)
    color = random.choice(colors)
    max_attempts = 1 ## Number of attempts to place circles without overlapping
    placed = False
    
    for attempt in range(max_attempts):
        x = random.randint(-canvas_size // 2 + radius, canvas_size // 2 - radius)
        y = random.randint(-canvas_size // 2 + radius, canvas_size // 2 - radius)
        
        # If there is no overlap, draw the circle and save the information
        if not is_overlapping(x, y, radius):
            drawer.goto(x, y - radius)  # Go to the starting point of the circle
            drawer.pendown()
            drawer.pencolor("black")  # Make the outline black
            drawer.fillcolor(color)   # Set the fill color of the circle
            drawer.begin_fill()
            drawer.circle(radius)
            drawer.end_fill()
            drawer.penup()
            
            # Save the center coordinates and radius of the circle
            circles.append((x, y, radius))
            placed = True
            break

# Let's divide the canvas into small cells to place the small circles
small_radius = 5
grid_size = 10 # A grid (10x10) with one small circle in each cell
step_size = 1 * small_radius # We set the step size according to the circle diameter

for x in range(-canvas_size // 2, canvas_size // 2, step_size):
    for y in range(-canvas_size // 2, canvas_size // 2, step_size):
        # We will place small circles in each cell
        if not is_overlapping(x, y, small_radius):
            drawer.goto(x, y - small_radius)  
            drawer.pendown()
            drawer.pencolor("black") 
            drawer.fillcolor(random.choice(colors))  
            drawer.begin_fill()
            drawer.circle(small_radius)
            drawer.end_fill()
            drawer.penup()
            
            circles.append((x, y, small_radius))

# Show the drawing
screen.update()
screen.exitonclick()
