import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

# Draw a circle of radius 10 at (0, -10)
# oriented around origin for convenience
t.penup()
t.goto(0, -10)
t.pendown()

t.circle(10)

# Draw a circle of radius 50 at (0, -50)
t.penup()
t.goto(0, -50)
t.pendown()

t.circle(50)

# Draw a circle of radius 70 at (0, -70)
t.penup()
t.goto(0, -70)
t.pendown()

t.circle(70)

# Draw a circle of radius 90 at (0, -90)
t.penup()
t.goto(0, -90)
t.pendown()

t.circle(90)

# Draw horizontal line from (-150, 0) to (150, 0)
t.penup()
t.goto(-150, 0)
t.pendown()
t.goto(150, 0)

# Draw vertical line from (0, -150) to (0, 150)
t.penup()
t.goto(0, -150)
t.pendown()
t.goto(0, 150)

# Draw diagonal line from (-106, -106) to (106, 106)
t.penup()
t.goto(-106, -106)
t.pendown()
t.goto(106, 106)

# Draw diagonal line from (-106, 106) to (106, -106)
t.penup()
t.goto(-106, 106)
t.pendown()
t.goto(106, -106)
