import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("US States Game")

# Load the image of the blank US map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data of US states
data = pandas.read_csv('50_states.csv')

# Create a turtle to write state names on the map
pen = turtle.Turtle()
pen.hideturtle()

# Convert the state names to a list
state_name_list = data.state.to_list()
known_state = []

# Main game loop
while len(known_state) < 50:
    # Prompt the user to enter a state name
    answer_state = screen.textinput(title=f"{len(known_state)}/50 States Correct", prompt="What's another state name?")
    str_answer = (str(answer_state)).title()

    # Check if the entered state name is correct and not already guessed
    if str_answer in state_name_list and str_answer not in known_state:
        # Get the coordinates of the state
        state = data[data.state == str_answer]
        pen.penup()
        pen.goto(state.x.item(), state.y.item())
        pen.pendown()
        # Write the state name on the map
        pen.write(f"{str_answer}")
        known_state.append(str_answer)
        
    # If the user types 'Exit', save the missing states to a CSV file and exit
    elif str_answer == 'Exit':
        missing_states = [state for state in state_name_list if state not in known_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break