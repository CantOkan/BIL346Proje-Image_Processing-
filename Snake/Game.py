import tkinter

status=False
def startGame():
    status=True
    window.destroy()

    if(status==True):
        import Snake
        Snake.start



window=tkinter.Tk()

window.title("Game")
window.geometry('300x300')
label=tkinter.Label(master=window, text="Welcome to the Game")
label2=tkinter.Label(master=window, text="You can control the Snake with W,A,S,D \n NOTE:color of object must be blue")

label.grid(column=0,row=0)
label2.grid(column=0,row=3)



btn1=tkinter.Button(master=window, text="Start the Game",command=startGame)

btn1.grid(column=0,row=5)

window.mainloop()
