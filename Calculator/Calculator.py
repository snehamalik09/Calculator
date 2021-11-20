from tkinter import *

root=Tk()
root.title("Calculator by sneha")
root.geometry("500x600")
root.maxsize(500,600)
root.wm_iconbitmap("calculator.ico")      #Adding icon to gui title


screenvalue=StringVar()
screenvalue.set("")
screen=Entry(root, textvariable=screenvalue, font="lucida 35 bold")
screen.pack(padx=8, pady=15, ipadx=10, fill="x")


#Function to operate functioning of calculator
def click(event):
    global screenvalue
    text=event.widget.cget("text")
    if text=="C":
        screenvalue.set("")
        screen.update()
    elif text=="=":
        if screenvalue.get().isdigit():
            value=int(screenvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        screenvalue.set(value)
        screen.get()
    else:
        screenvalue.set(screenvalue.get()+text)
        screen.update()


#function to create buttons of calculator
def createbuttons(*args):
    l=[]
    for i in args:
        l.append(i)
    frame = Frame(root, bg="grey")          #Creating Frames to pack buttons
    for i in l:
        button = Button(frame, text=f"{i}", pady=25, padx=33, font="lucida 10 bold")
        button.pack(side="left", padx=11, pady=5)
        buttonevent = button.bind("<Button-1>", click)
    frame.pack(pady=5)


#calling createbutton function to create buttons
createbuttons("C","=","%","/")
createbuttons("9","8","7","+")
createbuttons("6","5","4","-")
createbuttons("3","2","1","*")
createbuttons(".","0","00")

root.mainloop()

