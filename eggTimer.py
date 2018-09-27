from Tkinter import *
import tkMessageBox

def startTime():
    root.after(scale.get()*60000, messageWindow)
    
#def alertTimer():
#    root.bell()
#    tkMessageBox.showinfo("Ready","DING DING DING")
#    quit()
    
def messageWindow() :
    win = Toplevel()

    b = Button(win, text='DING DING DING',
               bg="blue", fg="yellow",
               activebackground="red", activeforeground="white",
               command=quit)
    b.pack(ipadx=root.winfo_screenwidth()/2,
           ipady=root.winfo_screenheight()/2)

    root.mainloop()

root = Tk()

button = Button(root, text="Start",command=startTime)
button.grid(row=1, column=1, pady=5, sticky=E)

minute = Label(root,text="Minutes")
minute.grid(row=0, column=0)
scale = Scale(root, from_=1,to=45, orient=HORIZONTAL,length=300 )
scale.grid(row=0,column=1)


root.mainloop()