import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv('50_states.csv')


def write_state_name(state_name, states_data, state_writer):
    data_row = states_data[states_data['state'] == state_name]
    state_writer.goto(float(data_row['x']), float(data_row['y']))
    state_writer.write(state_name)


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    if data['state'].isin([answer_state]).any():
        guessed_states.append(answer_state)
        write_state_name(answer_state, data, writer)
    if answer_state == 'Exit':
        break

data[~data['state'].isin(guessed_states)]['state'].to_csv('states_to_learn.csv')
