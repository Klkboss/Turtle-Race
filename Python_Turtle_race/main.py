"""Turtle race game has been made with the help of Turtle graphics """
import random
from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)

# Ask user for their bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: \n Red, Orange, Yellow, Green, Blue and Purple")

# Set up turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_t = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_pos[i])
    all_t.append(tim)

# Start the race if there's a bet
if user_bet:
    Start_race = True

while Start_race:
    for turtle in all_t:
        if turtle.xcor() > 230:
            Start_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")

        # Move the turtle forward by a random distance
        random_dis = random.randint(0, 10)
        turtle.fd(random_dis)

screen.exitonclick()
