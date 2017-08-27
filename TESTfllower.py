import turtle

def prepare_window() :
    window = turtle.Screen()
    window.bgcolor ("black")
    return window

def prepare_player(shape, color, speed) :
    player = turtle.Turtle()
    player.shape(shape)
    player.color(color)
    player.speed(speed)
    return player


def draw_flower(forward, right) :
    for _ in range(37):
       player.forward(forward)
       player.right(right)


def draw_stem() :
    player.forward(100)
    player.right(93)
    player.forward(250)
   


win = prepare_window()
player = prepare_player("arrow","purple", 10)
draw_flower(200, 175)
draw_stem()
win.exitonclick()
