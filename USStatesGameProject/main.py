import turtle
import pandas
import index

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guesses = turtle.Turtle()
guesses.hideturtle()

states_table = pandas.read_csv("50_states.csv")
states_list = states_table.state.to_list()

continue_game = True
correct_guesses_list = []

index = index.Index()

while continue_game:
    answer_state = screen.textinput(title=f"{len(correct_guesses_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in correct_guesses_list:
        continue
    if answer_state in states_list:
        guesses.penup()
        guesses.goto(states_table.iloc[index.find_index(answer_state) - 1].x,
                     states_table.iloc[index.find_index(answer_state) - 1].y)
        guesses.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))
        correct_guesses_list.append(answer_state)
    if len(correct_guesses_list) == 50:
        continue_game = False
        guesses.penup()
        guesses.goto(0, 40)
        guesses.write("End Game", align="center", font=("Arial", 20, "normal"))
        guesses.goto(0, 0)
        guesses.write("Congratulations, you have guessed all the states!", align="center", font=("Arial", 20, "normal"))
        guesses.goto(0, -40)
        guesses.write("Click on the screen to exit.", align="center", font=("Arial", 20, "normal"))
        screen.exitonclick()
    if answer_state == "Exit":
        continue_game = False

missing_states = [state for state in states_list if state not in correct_guesses_list]
states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_to_learn.csv")
