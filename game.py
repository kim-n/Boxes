from tkinter import *
from random import choice

ball, ballSize, gameSize = None, 20, 300
futureJob = None
def leftClick(event):
    global ball, futureJob
    if futureJob is not None:
        root.after_cancel(futureJob)
        futureJob = None
    ball = canvas.create_rectangle(event.x-10, event.y-10,
                               event.x+10, event.y+10, fill=choice(['pink', 'light salmon', 'khaki', 'pale turquoise']))
    animate()

def ballPosition():
    x1, y1, x2, y2 = canvas.coords(ball)
    return[(x1 + x2)/2, (y1 + y2)/2]

def randomSpeed():
    return choice(list(range(ballSize*2)))-ballSize
    
def outBounds(coord):
    return 0 > coord or coord > gameSize-ballSize

def startGame():
    headline['text'] = 'Welcome!'

    global canvas, ball, futureJob
    if futureJob is not None:
        root.after_cancel(futureJob)
        futureJob = None
        
    xLeftCoord = choice(list(range(gameSize-ballSize)))
    yLeftCoord = choice(list(range(gameSize-ballSize)))
    if ball:
        canvas.delete(ball)
    ball = canvas.create_rectangle(xLeftCoord, yLeftCoord, xLeftCoord+ballSize, yLeftCoord+ballSize, fill='red' )
    print(ballPosition())
    
    animate()
    
def endGame():
    print('Bye Bye!')
    root.destroy()

def animate():
    global ball, futureJob
    print(ballPosition())
    xSpeed = randomSpeed()
    ySpeed = randomSpeed()
    while outBounds(ballPosition()[0]+xSpeed):
        xSpeed = randomSpeed()
    while outBounds(ballPosition()[1]+ySpeed):
        ySpeed = randomSpeed()
    canvas.move(ball, xSpeed, ySpeed)
    ball = canvas.create_rectangle(canvas.coords(ball), fill=choice(['pink', 'light salmon', 'khaki', 'pale turquoise']))
    futureJob = root.after(100, animate)


root = Tk()

headline = Label(root)
headline.pack()


canvas = Canvas(root, width=gameSize, height=gameSize)
canvas.pack()

buttonsFrame = Frame(root)
buttonsFrame.pack()
startButton = Button(buttonsFrame, command=startGame, text='Start')
endButton = Button(buttonsFrame, command=endGame, text='Exit')
startButton.pack(side=LEFT)
endButton.pack(side=RIGHT)

canvas.bind('<ButtonPress-1>', leftClick)

mainloop()