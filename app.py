from cProfile import label
from cgitb import text
import fractions
from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import *
import tkinter
from PIL import Image,ImageTk

#Creating the tkinker windows  
window = Tk()
window.title("Beach Hotels")


#This is use to place the image as a background colour
image1= Image.open('/Users/imac-13/Desktop/Tourism/images/maldives_tropical_beach_sand_summer_palm_trees_88001_2048x1152.jpeg')
window.geometry('2048x1152')
background_image = ImageTk.PhotoImage(image1)
lbl = Label(window, image=background_image)
lbl.place(x=0, y=0, width=2048, height=1152)


#This is the Navigation Bar or the The title of the Project.
frame1= Frame(window)
frame1.pack()
heading = Label(frame1, text="Horizon De Mer", font="Arial 25", bg="#2779b8", )
heading.pack(ipadx=2048, ipady=15)


#Moving from the main to the inscription page 
def insrcire():      
    frame2.pack_forget()
    footer.pack_forget()
    frame3.pack(pady=200)
    
def connecte():
    frame2.pack_forget()
    footer.pack_forget()
    frame4.pack(pady=300, ipadx=25)
    
def main():            
    frame4.pack_forget()
    frame5.pack(pady=150,ipadx=100 )

#To Return to the home page from the inscription page 
def return1():      
    frame3.pack_forget()
    frame2.pack(pady=350, padx=400)
    footer.pack(ipadx=2048, pady=60)

#To Return to the home page from the Connection page   
def return2():     
    frame4.pack_forget()
    frame2.pack(pady=350, padx=400)
    footer.pack(ipadx=2048, pady=60)
    
    

#The Frame of the main page of the application   
frame2 = Frame(window, highlightbackground="#191970", highlightthickness=4)
frame2.configure(bg="#2779b8")
frame2.pack(pady=350, padx=400)

btn1 = Button(frame2, text="Inscription", command=insrcire, font="Arial 17")
btn1.pack(pady=10, ipady=10, padx=30)

btn2 = Button(frame2, text="Connexion", command=connecte, font="Arial 17")
btn2.pack(pady=5, ipady=10, padx=30)

btn3 = Button(frame2, text="Quitter", font="Arial 17" ,command=window.quit)
btn3.pack(pady=10, ipady=10, padx=30)



# The Inscription Page of the Application
frame3 = Frame(window, highlightbackground="#191970", highlightthickness=5)
frame3.configure(bg="#2779b8")

heading = Label(frame3, text="Page de connexion", font="Arial 20 underline", bg="#2779b8")
heading.pack(pady=10,padx=15)

nomlabel = Label(frame3, text="Nom", font="Arial 20", bg="#2779b8")
nomlabel.pack(pady=10,padx=15,anchor='nw')

nomentry = Entry(frame3)
nomentry.pack(pady=10,padx=15, anchor='nw')

prenomlabel = Label(frame3, text="Prenom", font="Arial 20",bg="#2779b8" )
prenomlabel.pack(pady=10,padx=15, anchor='nw')

prenomentry = Entry(frame3)
prenomentry.pack(pady=10,padx=15, anchor='nw')

emaillabel = Label(frame3, text="Email", font="Arial 20", bg="#2779b8")
emaillabel.pack(pady=10,padx=15, anchor='nw')

emailentry = Entry(frame3)
emailentry.pack(pady=10,padx=15, anchor='nw')

mdplabel = Label(frame3, text="Mot de passe ", font="Arial 20", bg="#2779b8")
mdplabel.pack(pady=10,padx=15,anchor='nw')

mdpentry = Entry(frame3)
mdpentry.pack(pady=10, padx=15,anchor='nw')

cmdplabel = Label(frame3, text="Confirme mot de passe", font="Arial 20", bg="#2779b8")
cmdplabel.pack(pady=10, padx=15,anchor='nw')

cmdpentry = Entry(frame3)
cmdpentry.pack(pady=10,padx=15, anchor='nw')

btn4 = Button(frame3, text="S'inscrire", font="Arial 20")
btn4.pack(ipady=5, pady=15)

btn5 = Button(frame3, text="Retour", command=return1, font="Arial 20")
btn5.pack(ipady=5, pady=15)



#This is The connection page of the website.
frame4 = Frame(window, highlightbackground="#191970", highlightthickness=5)
frame4.configure(bg="#2779b8")

Username_Label = Label(frame4, text="Username", font="Arial 20", bg="#2779b8")
Username_Label.pack(pady=10, padx=15,anchor='nw')

Username_entry = Entry(frame4)
Username_entry.pack(ipady=5, pady=15)

MdpLabel = Label(frame4, text="Mot de passe", font="Arial 20", bg="#2779b8")
MdpLabel.pack(pady=10, padx=15,anchor='nw')

Mdpentry = Entry(frame4)
Mdpentry.pack(ipady=5, pady=15)

btn6 = Button(frame4, text="Se Connecté", command=main, font="Arial 20")
btn6.pack(ipady=5, pady=15)

btn7 = Button(frame4, text="Retour", font="Arial 20", command=return2)
btn7.pack(ipady=5, pady=15)

#The Accueil menu to do a reservation.
frame5 = Frame(window, highlightbackground="#191970", highlightthickness=5)

frame5.configure(bg="#2779b8")

heading = Label(frame5, text="Accueil", font="Arial 20 underline", bg="#2779b8", )
heading.pack()
heading1 = Label(frame5, text="Faire une réservation",font="Arial 20 underline", bg="#2779b8")
heading1.pack()


destinationLabel = Label(frame5, text="Destination", font="Arial 20", bg="#2779b8")
destinationLabel.pack(ipady=5, pady=5, anchor='nw')

destination= Combobox(frame5, width = 45, state='readonly')
destination ['values']= ("Akwa Beach/Assinie, Côte d'Ivoire",
"Hotel Coucone/Assinie, Côte d'Ivoire",
"Assinie Beach/Assinie, Côte d'Ivoire", 
"Enotel Beach/San-Pedro, Côte d'Ivoire",  
"Hotel Palm Rock Beach/San-Pédro, Côte d'Ivoire",
"Afrik Casa Hotel /San-Pédro, Côte d'Ivoire",
"Boblin la Mer hotel restaurant plage/Grand-Bassam, Côte d'Ivoire",
"Le Koral Beach Hotel/Grand-Bassam, Côte d'Ivoire", 
"Assoyam Beach Hôtel/Grand-Bassam, Côte d'Ivoire")
destination.pack(pady=5,padx=5,anchor='nw')












#This The Footer of Page 
footer = Frame(window)
footer.configure(bg="#2779b8")
footer.pack(ipadx=2048, pady=60)

contact_nous =Label(footer, text="Appelez-nous au:", bg="#2779b8")
contact_nous.pack(side=LEFT, pady=10, ipadx=20)

numbre1 = Label(footer, text="+225 01 54 68 90 44", bg="#2779b8")
numbre1.pack(side=LEFT, pady=10, padx=10)

numbre2 = Label(footer, text="+225 07 88 54 23 00",bg="#2779b8")
numbre2.pack(side=LEFT, pady=10, padx=10)

email_us = Label(footer, text="Envoyez-nous un email:", bg="#2779b8")
email_us.pack(side=LEFT, pady=10, ipadx=20)

email1 = Label(footer, text="horizondemer@gmail.com", bg="#2779b8")
email1.pack(side=LEFT, pady=10, ipadx=20)

email2 = Label(footer, text="horizondemer@yahoo.com", bg="#2779b8")
email2.pack(side=LEFT, pady=10, ipadx=2)

btn5 = Button(footer, text="Voir Plus", highlightbackground="#2779b8")
btn5.pack(pady=9)








window.mainloop()
