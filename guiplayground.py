from tkinter import *

#widgets = GUI elements: buttons textboxes labels images
#windows = 
def reminder():
    
    window = Tk() #instantiate window
    window.geometry("500x500")
    window.title("Yeehaw")
    label = Label(window,
                    text="Hello World",
                    font=("Arial",40,'bold'),
                    fg='black',
                    bg='darkblue',
                    relief='raised',
                    padx=20,
                    pady=20)

    label.pack()





    window.mainloop() #use to place screen on window and listen for events.

