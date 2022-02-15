from cProfile import label
from cgitb import text
from curses import window
from tkinter import *
import tkinter 
from PIL import Image,ImageTk

window = Tk()
window.title("Beach Resort")

image1= Image.open('/Users/imac-13/Desktop/Tourism/LUX_NMA_WaterVilla_Hero-2048x1363.jpeg')
window.geometry('2048x1363')
background_image = ImageTk.PhotoImage(image1)

lbl = Label(window, image=background_image)
lbl.place(x=0, y=0, width=2048,height=1363)

frame1 = Frame(window, highlightbackground="black", highlightthickness=3)
frame1.place(x=1024, y=681)
heading = Label(frame1, text="Hello")
heading.pack()









window.mainloop()
