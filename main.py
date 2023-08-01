import turtle
from turtle import *
import pandas as pd

data = pd.read_csv("28_states.csv")
states = data.state
states = states.to_list()

guessed_states = []

game = Turtle()
screen = Screen()
screen.title("India States Game")
screen.addshape("india_map.gif")
turtle.shape("india_map.gif")
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color('black')

while len(guessed_states) != 28:
    guess = screen.textinput(f"{len(guessed_states)}/28 States Correct", "Enter State Name")
    guess = guess.title()
    if guess in states:
        guessed_states.append(guess)
        cur_state = data[data.state == guess]
        x = int(cur_state.x.item())
        y = int(cur_state.y.item())
        writer.goto(x, y)
        writer.write(guess)
    elif guess == "Exit":
        # Normal Execution
        # for st in guessed_states:
        #     states.remove(st)
        # not_guessed_states_dict = {"state": states}
        # df = pd.DataFrame(not_guessed_states_dict)
        # df.to_csv("states_to_learn.csv")
        # List comprehension
        states = [st for st in states if st not in guessed_states]
        df = pd.DataFrame(states)
        df.to_csv("states_to_learn.csv")
        exit()

