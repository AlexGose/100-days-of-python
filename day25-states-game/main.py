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


num_correct = 0
while num_correct < 50:
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if data['state'].isin([answer_state]).any():
        num_correct += 1
        write_state_name(answer_state, data, writer)

screen.exitonclick()
