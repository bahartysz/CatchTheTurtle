import turtle
import random

screen = turtle.Screen()
screen.bgcolor("Light blue")
screen.title("Catch The Turtle")
score = 0
game_over = False
FONT = ("Arial", 30, "normal")
# büyük harfle yazılmasının şu şekilde bir mantığı var; font olarak pythonda tanımlı da olabilir karışmaması için
# hem de FONT dediğimizde bu bir sabit ve bunu değiştirmeyeceğim gibi bir anlamı da var.
grid_size = 8

# turtle list

turtle_list = []
#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
# bu score turtle'ı
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_hight = screen.window_height() // 2 # ekranın yarısından başladığı için turtle // 2 yaptık.// tam böler
    y = top_hight * 0.8 # %80 almış olduk veya # top_hight  - top_hight / 10
    score_turtle.goto(0, y) # ekranın üst kısmına ortalamak için
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

    top_hight = screen.window_height() // 2  # ekranın yarısından başladığı için turtle // 2 yaptık.// tam böler
    y = top_hight * 0.6  # %80 almış olduk
    countdown_turtle.goto(0, y )  # ekranın üst kısmına ortalamak için
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Score: Game Over!", move=False, align="center", font=FONT)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0) # takip edici 0 ile başlayıp tü işlem bittikten sonra alttaki gibi 1 yapılabilir
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1) # bu şekilde takip etme yani turtlların sırayla gelişini görmeyi bırakıyoruz animasyon olmadan
                 # hepsi aynı anda ekranda görünüyor.
    screen.ontimer(lambda:countdown(10),10)



start_game_up()
turtle.mainloop()