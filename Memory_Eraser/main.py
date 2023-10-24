from tkinter import *
from tkinter.ttk import Progressbar,Style
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
from time import sleep

root = Tk()
root.geometry("400x300")
root.title("Memory Eraser")
root.resizable(0,0)

def update_progress_label(pb):
    return f"Deleting Feelings >>>> {pb['value']}%"

def delete_mem():
    del_button.config(state="disable")
    s = Style()
    s.theme_use('alt')
    s.configure("white.Horizontal.TProgressbar",background="white")
    pb = Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=200,
        style="white.Horizontal.TProgressbar"
    )
    pb.place(x=120,y=220)
    def start():
        if pb['value'] < 90:
            pb['value'] += 2
            value_label['text'] = update_progress_label(pb)
        else:
            sleep(1)
            showinfo(title="Warning",message='Unable to delete Memories\n Size is too Large')
            root.destroy()
        root.after(100, start)

    value_label = Label(root, text=update_progress_label(pb),font=('Noto Serif',10,"bold"),bg="black",fg="white")
    value_label.place(x=120,y=250)
    root.after(100, start)


img = ImageTk.PhotoImage(Image.open("C:/Users/INFRATECH/Desktop/tkinter/delete_feelings/bg.jpg")) 
win_background = Label(root,image=img).pack()

win = Frame(root,height=300,width=400,bg="black").pack()

label_1 = Label(win,text="Delete all Memories of her",fg="white",bg="black",font=('Noto Serif',18,"bold"))
label_1.place(x=60,y=100)
del_button = Button(win,text="Delete",font=('Noto Serif',10,"bold"),bg="black",fg="white",command=delete_mem,activebackground="red")
del_button.place(x=180,y=180)


root.mainloop()
