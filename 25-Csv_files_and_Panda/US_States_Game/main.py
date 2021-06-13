

# https://www.sporcle.com/games/g/states

import turtle
import pandas

'''Display US states gif'''
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name").lower()

# answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name").lower()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
