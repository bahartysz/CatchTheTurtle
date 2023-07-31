import turtle
import random

screen = turtle.Screen()
screen.bgcolor("Light blue")
screen.title("Catch The Turtle")
score = 0
game_over = False
FONT = ("Arial", 30, "normal")
grid_size = 8

# turtle list
turtle_list = []

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

# Restart turtle
restart_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.clear()
    score_turtle.reset()
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_hight = screen.window_height() // 2
    y = top_hight * 0.8
    score_turtle.goto(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score, game_over
        if not game_over:
            score += 1
            score_turtle.clear()
            score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("Dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

def setup_turtles():
    for x in [-20,-10,0,10,20]:
        for y in [20,10,0,-10,-20]:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()

    top_hight = screen.window_height() // 2
    y = top_hight * 0.6
    countdown_turtle.goto(0, y )
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Score: Game Over! Click 'Restart' to play again.", move=False, align="center", font=FONT)
        show_restart_message() #restart opsiyonu devreye girer

def show_restart_message():
    restart_turtle.hideturtle()
    restart_turtle.clear()
    restart_turtle.penup()
    restart_turtle.color("red")
    restart_turtle.goto(0,-50) # yeni konuma ayarla
    restart_turtle.write(arg="Restart", move=False, align="center",font=FONT)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)
    restart_turtle.hideturtle()


def reset_game():
    global score, game_over
    score = 0
    game_over = False
    setup_score_turtle()
    start_game_up()  # oyun sıfırlandığında yeniden başlat
    restart_turtle.hideturtle()  # restart opsiyonu gizle

def handle_restart_click(x, y):
    global game_over
    if game_over and -70 <= x <= 70 and -70 <= y <= -30: #restart opsiyonu tıklandığında oyunu sıfırla
        restart_turtle.clear()
        reset_game()

setup_score_turtle()
start_game_up()
screen.onclick(handle_restart_click)
turtle.mainloop()