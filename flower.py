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


def draw_flower(forward, backward, right) :
   for _ in range(37):
       player.forward(forward)
       player.backward(backward) 
       player.right(right)

       
def draw_stem() :
    #player.forward(100)
    player.right(90)
    player.forward(250)
   


win = prepare_window()
player = prepare_player("arrow","purple", 10)
draw_flower(100, 200, 175)
player = prepare_player("arrow","yellow", 10)
draw_flower(50, 100, 170)
player = prepare_player("arrow","green", 10)
draw_stem()

win.exitonclick()
