from tkinter import Button, Label, Tk
from traceback import *
import turtle

def Call():
    turtle.shape('turtle')
    msg = Label(window,text="please learn to follow instructions")
    msg.place(x=300,y=500)
    for i in range(0,6):
        turtle.forward(100)
        turtle.right(90)

    turtle.exitonclick()

window=Tk()
window.geometry('800x800')
button=Button(text='im a button dont press me',command=Call)
button.place(x=200,y=400,height=50,width=400)
button['bg']='red'
button['fg']='black'
window.mainloop()
