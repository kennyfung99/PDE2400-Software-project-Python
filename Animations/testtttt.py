from tkinter import*
from PIL import ImageTk,Image

root=Tk()
root.title('kenny')

my_img= ImageTk.PhotoImage(Image.open("C:/Users/kenny/Desktop/work/PDE2400-Software-project-Python/Animations/kenny.jpg"))
my_label=Label(image=my_img)
my_label.pack()


button_quit=Button(root,text="Exit",command=root.quit)
button_quit.back
