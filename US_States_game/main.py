import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
blank_state_img = "blank_states_img.gif"
turtle.addshape(blank_state_img)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
turtle.shape(blank_state_img)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50States Correct",
                                    prompt="What's the next State name?").title()
    if answer_state == "Exit":
        #Without List Comprehensio
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        #Using List Comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        state_to_learn = pandas.DataFrame(missing_states)
        state_to_learn.to_csv("States_to_Learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        selected_state = data[data.state == answer_state]
        t.goto(int(selected_state.x), int(selected_state.y))
        t.write(answer_state)
