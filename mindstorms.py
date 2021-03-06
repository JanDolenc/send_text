import turtle

def prepare_window() :
    window = turtle.Screen()
    window.bgcolor("black")
    return window

def prepare_player(shape, color, speed) :
    player = turtle.Turtle()
    player.shape(shape)
    player.color(color)
    player.speed(speed)
    return player

def draw_square() :

     for _ in range(4):
         player.forward(140)
         player.right(90)
    
def draw_circle() :
    
    player.circle(100)

def draw_triangle() :

    for _ in range(3):
        player.right(120)
        player.forward(160)
       
def turn() :
    player.right(1)
    
win = prepare_window()
player = prepare_player("classic", "orange", 2000)

for _ in range (360) :
    draw_square()
    turn()

win.exitonclick()
