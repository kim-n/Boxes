from tkinter import *
from random import choice

gameSize = 300

def startGame():
    headline['text'] = 'Welcome!'
    
def endGame():
    print('Bye Bye!')
    root.destroy()



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