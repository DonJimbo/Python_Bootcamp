import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To click on the map, and find the location 'x' and 'y'

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()