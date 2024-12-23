import random
from turtle import Turtle, Screen

# Set up the screen with new dimensions and background color
screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("lightblue")  # Set the background color to light blue

# Ask user for their bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Set up turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-150, -90, -30, 30, 90, 150]  # Adjusted y positions for larger screen
all_t = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-320, y=y_pos[i])  # Adjusted x position for larger screen
    tim.turtlesize(stretch_wid=2, stretch_len=2)  # Increase the size of the turtles
    all_t.append(tim)

# Draw the finish line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(320, -250)  # Start at bottom of the screen at the finish line x position
finish_line.pendown()
finish_line.left(90)
finish_line.forward(500)  # Draw a vertical line up
finish_line.hideturtle()

# Start the race if there's a bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_t:
        if turtle.xcor() > 300:  # Adjusted x position for the finish line
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")

        # Move the turtle forward by a random distance
        random_dis = random.randint(0, 10)
        turtle.fd(random_dis)

screen.exitonclick()
