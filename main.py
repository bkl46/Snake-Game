from tkinter import *
import random

speed = 100
unit_length = 25
init_length = 3
snake_color ="#00FF00"
apple_color = "#FF0000"
background_color = "#000000"
score = 0
direction = 'down'
dimension = 750

class Snake:
    def __init__(self):
        self.size = init_length
        self.coordinates = []
        self.squares = []

        for i in range(0,init_length):
            self.coordinates.append([0,0])
        for x, y, in self.coordinates:
            square = canvas.create_rectangle(x,y, x + unit_length, y+unit_length, fill=snake_color,tag='snake')
            self.squares.append(square)

class Apple:
    def __init__(self):
        x = random.randint(0, (int(dimension/unit_length)-1))*unit_length
        y = random.randint(0,(int(dimension/unit_length)-1))*unit_length
        self.coordinates = [x,y]

        self.ap = canvas.create_rectangle(x,y,x+unit_length,y+unit_length,fill=apple_color,tag='apple')

class Tester:
    def __init__(self):
        x = dimension-unit_length
        y = dimension - unit_length
        canvas.create_rectangle(x,y,x+unit_length,y+unit_length,fill=snake_color)


def move(snake, apple):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= unit_length
    elif direction == "down":
        y += unit_length
    elif direction == "left":
        x -= unit_length
    elif direction == "right":
        x += unit_length
    
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x,y,x+unit_length,y+unit_length,fill=snake_color,tag='apple')
    snake.squares.insert(0,square)

    if x == apple.coordinates[0] and y == apple.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete(apple.ap)
        apple = Apple()
        
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(speed, move, snake, apple)

def turn(new_direction):
    global direction

    if((new_direction == 'left') and (direction != 'right')):
        direction = new_direction
    elif((new_direction == 'right') and (direction != 'left')):
        direction = new_direction
    elif((new_direction == 'down') and (direction != 'up')):
        direction = new_direction
    elif((new_direction == 'up') and (direction != 'down')):
        direction = new_direction

def check_collision(snake):
    x,y = snake.coordinates[0]
    if (x < 0 or x > dimension - unit_length) or (y < 0 or y > dimension - unit_length):
        print("Game over")
        return True
    for i in snake.coordinates[1:]:
        if x == i[0] and y == i[1]:
            print("Game over")
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(dimension/2, dimension/2,text="GAME OVER",fill="yellow")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

label = Label(window, text="Score: {}".format(score), font=('Helvetica',40))
label.pack()

canvas = Canvas(window, bg = background_color, height=dimension, width=dimension)
canvas.pack()

window.update()

snake=Snake()
apple=Apple()

window.bind('<Left>', lambda event: turn('left'))
window.bind('<Right>', lambda event: turn('right'))
window.bind('<Down>', lambda event: turn('down'))
window.bind('<Up>', lambda event: turn('up'))

move(snake,apple)

window.mainloop()