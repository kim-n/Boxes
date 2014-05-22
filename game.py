from tkinter import *
from random import choice

ball, gameSize = None, 300

def ballPosition():
    x1, y1, x2, y2 = canvas.coords(ball)
    return[(x1 + x2)/2, (y1 + y2)/2]

def randomSpeed():
    return choice(list(range(20)))-10
    
def outBounds(coord):
    return 0 > coord or coord > gameSize-10

def startGame():
    headline['text'] = 'Welcome!'
    
    global canvas, ball
    xLeftCoord = choice(list(range(gameSize-10)))
    yLeftCoord = choice(list(range(gameSize-10)))
    if ball:
        canvas.delete(ball)
    ball = canvas.create_rectangle(xLeftCoord, yLeftCoord, xLeftCoord+10, yLeftCoord+10, fill='red' )
    print(ballPosition())
    
    animate()
    
def endGame():
    print('Bye Bye!')
    root.destroy()

def animate():
    global ball
    xSpeed = randomSpeed()
    ySpeed = randomSpeed()
    while outBounds(ballPosition()[0]+xSpeed):
        xSpeed = randomSpeed()
    while outBounds(ballPosition()[1]+ySpeed):
        ySpeed = randomSpeed()
    canvas.move(ball, xSpeed, ySpeed)
    ball = canvas.create_rectangle(canvas.coords(ball), fill=choice(['purple', 'blue', 'yellow', 'orange', 'red', 'green']))
    root.after(100, animate)


root = Tk()

headline = Label(root)
headline.pack()


canvas = Canvas(root, width=gameSize, height=gameSize, bg='light yellow')
canvas.pack()

buttonsFrame = Frame(root)
buttonsFrame.pack()
startButton = Button(buttonsFrame, command=startGame, text='Start')
endButton = Button(buttonsFrame, command=endGame, text='Exit')
startButton.pack(side=LEFT)
endButton.pack(side=RIGHT)


mainloop()