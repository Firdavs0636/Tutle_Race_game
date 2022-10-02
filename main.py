from turtle import Turtle, Screen
import turtle
import random

is_game_over = True
screen = Screen()
turtle.speed(11)
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-90, -50, -10, 30, 70, 110]
turtle_list = []
i=0


def turtle_cloner():
    for turtle_index in range(colors.__len__()):
        downy = Turtle(shape="turtle")
        downy.color(colors[turtle_index])
        downy.penup()
        downy.goto(x=-230, y=y_positions[turtle_index])
        turtle_list.append(downy)
        downy.clearstamps()


def reseter(i):
    for old_turtle in turtle_list:
        old_turtle.hideturtle()
        old_turtle.goto(x=-230, y=y_positions[i])
        i += 1
        old_turtle.showturtle()


turtle_cloner()
while is_game_over:
    user_guess = screen.textinput(title="Make a guess!",
                                  prompt="Which turtle will win the race? (Red, Yellow, Blue, Purple, Green) Enter a color: ").lower()
    is_race_on = True

    while is_race_on:
        for turtle in turtle_list:
            random_distance = random.randint(15, 20)
            turtle.forward(random_distance)
            if turtle.xcor() > 230:
                is_race_on = False
                fast_turtle_color = turtle.pencolor()
                if user_guess == fast_turtle_color:
                    print(f"You Win. Congratulations!!! The {fast_turtle_color} turtle is the winner!")
                else:
                    print(f"You Lose. The {fast_turtle_color} turtle is the winner!")
                user_guess2 = screen.textinput(title="Do you wanna play again?", prompt="Type Yes or No: ").lower()

                if user_guess2 == "yes":
                    reseter(i)
                    is_game_over = True
                    break
                elif user_guess2 == "no":
                     exit()
                else:
                    print("You entered an invalid prompt. Please try again!")




#below codes creates turtles in different postions in the number of colors number
# x = -230
# y = -120
#
#
# def cloning(color, x, y):
#     downy.clone().color(color)
#     downy.goto(x=x, y=y)
#
#
# for i in colors:
#     cloning(i, x, y)
#     y += 40

screen.exitonclick()