import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
list_of_states = df.state.to_list()

print(list_of_states)

karel = turtle.Turtle()
guessed_states = []
not_guessed_states = []

while len(guessed_states) < 50:
    karel.penup()
    karel.hideturtle()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        for state in list_of_states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        not_guessed_df = pandas.DataFrame(not_guessed_states)
        not_guessed_df.to_csv("missing_states.csv")
        break
    if df["state"].eq(answer_state).any():
        chosen_state = df[df.state == answer_state]
        chosen_state_x = int(chosen_state.x)
        chosen_state_y = int(chosen_state.y)

        karel.goto(chosen_state_x, chosen_state_y)
        karel.write(f"{answer_state}", move=False, align='left', font=('Arial', 10, 'normal'))
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)


turtle.exitonclick()