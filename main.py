import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# work of pandas
data = pandas.read_csv("50_states.csv")
name_states = data["state"].to_list()


# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

guessed_states = []
need_to_learn = []
x = 0
while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                   prompt="What's another state's name?").title()
    if answer_text == "Exit":
        need_to_learn = [state for state in name_states if state not in guessed_states]
        new_data = pandas.DataFrame(need_to_learn)
        new_data.to_csv("need_to_learn.csv")
        break
    if answer_text in name_states:
        guessed_states.append(answer_text)
        ans = data[data.state == answer_text]
        new_x = int(ans.x)
        new_y = int(ans.y)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(new_x, new_y)
        new_turtle.write(answer_text)


