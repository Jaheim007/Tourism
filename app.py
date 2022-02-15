from cProfile import label
from cgitb import text
from curses import window
from tkinter import *
import tkinter
from xxlimited import foo 
from PIL import Image,ImageTk

window = Tk()
window.title("Beach Resort")

#This is use to place the image as a background colour
image1= Image.open('/Users/imac-13/Desktop/Tourism/LUX_NMA_WaterVilla_Hero-2048x1363.jpeg')
window.geometry('2048x1363')
background_image = ImageTk.PhotoImage(image1)
lbl = Label(window, image=background_image)
lbl.place(x=0, y=0, width=2048, height=1363)

#This is the Navigation Bar and the The title of the Project.
frame1= Frame(window)
frame1.pack()
heading = Label(frame1, text="Horizon De Mer", font="Arial 25", bg="#2779b8")
heading.pack(ipadx=2048, ipady=15)

frame2 = Frame(window, highlightbackground="black", highlightthickness=3)
frame2.configure(bg="#2779b8")
frame2.pack(pady=350, padx=400)

def connecte():
    lbl.pack_forget()      
    frame2.pack_forget()

btn1 = Button(frame2, text="Connexion", command=connecte, font="Arial 17")
btn1.pack(pady=10, ipady=10, padx=30)

btn2 = Button(frame2, text="Inscription", font="Arial 17")
btn2.pack(pady=5, ipady=10, padx=30)

btn3 = Button(frame2, text="Deconnexion", font="Arial 17" ,command=window.quit)
btn3.pack(pady=10, ipady=10, padx=30)


image2= Image.open('/Users/imac-13/Desktop/Tourism/images (1).jpeg')
window.geometry('2048x1363')
background_image = ImageTk.PhotoImage(image2)
lbl2 = Label(window, image=background_image)
lbl2.place(x=0, y=0, width=2048, height=1363)

frame3 = Frame(window)
frame3.configure(bg="#2779b8")

nomlabel = Label(frame3, text="Nom")
nomlabel.pack()
nomentry = Entry(frame3)
nomentry.pack()

prenomlabel = Label(frame3, text="Prenom")
prenomlabel.pack()
prenomentry = Entry(frame3)
prenomentry.pack()

emaillabel = Label(frame3, text="Email")
emaillabel.pack()
emailentry = Entry(frame3)
emailentry.pack()

mdplabel = Label(frame3, text="Mot De Passe ")
mdplabel.pack()
mdpentry = Entry(frame3)
mdpentry.pack()

cmdplabel = Label(frame3, text="Confirme mot de passe")
cmdplabel.pack()
cmdpentry = Entry(frame3)
cmdpentry.pack()

btn = Button(frame3, text="Sumbit")

 






















footer = Frame(window)
footer.configure(bg="#2779b8")
footer.pack(ipadx=2048, pady=50)

contact_nous =Label(footer, text="Appelez-nous au:", bg="#2779b8")
contact_nous.pack(side=LEFT, pady=10)
numbre1 = Label(footer, text="+225 01 54 68 90 44", bg="#2779b8")
numbre1.pack(side=LEFT, pady=10)
numbre2 = Label(footer, text="+225 07 88 54 23 00",bg="#2779b8")
numbre2.pack(side=LEFT, pady=10)

email_us = Label(footer, text="Envoyez-nous un email:", bg="#2779b8")
email_us.pack(side=LEFT, pady=10)

email1 = Label(footer, text="horizondemer@gmail.com,", bg="#2779b8")
email1.pack(side=LEFT, pady=10)

email2 = Label(footer, text="horizondemer@yahoo.com", bg="#2779b8")
email2.pack(side=LEFT, pady=10)














window.mainloop()
