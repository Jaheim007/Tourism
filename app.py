from cProfile import label
from cgitb import text
import fractions
from struct import pack
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from turtle import left
from tkcalendar import *
from cryptography.fernet import Fernet
import sqlite3
import tkinter
import re
from PIL import Image,ImageTk


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

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
    frame5.pack(pady=25,ipadx=100)

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

def return3():
    frame5.pack_forget()
    frame2.pack(pady=350, padx=400)

#To return the first home page   
def return4():        
    frame6.pack_forget()
    frame2.pack(pady=350, padx=400)
    footer.pack(ipadx=2048, pady=60)


def return5():      
    frame6.pack_forget()
    frame5.pack(pady=25,ipadx=100)
        

    
     
   
   
  

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

emaillabel = Label(frame3, text="Votre adresse e-mail", font="Arial 20", bg="#2779b8")
emaillabel.pack(pady=10,padx=15, anchor='nw')

emailentry = Entry(frame3)
emailentry.pack(pady=10,padx=15, anchor='nw')

mdplabel = Label(frame3, text="Mot de passe ", font="Arial 20", bg="#2779b8")
mdplabel.pack(pady=10,padx=15,anchor='nw')

mdpentry = Entry(frame3 ,show="•")
mdpentry.pack(pady=10, padx=15,anchor='nw')

cmdplabel = Label(frame3, text="Confirme mot de passe", font="Arial 20", bg="#2779b8")
cmdplabel.pack(pady=10, padx=15,anchor='nw')

cmdpentry = Entry(frame3, show="•")
cmdpentry.pack(pady=10,padx=15, anchor='nw')

#I used this to hide the password in the database
key = Fernet.generate_key()
fernet = Fernet(key)
encmdp = fernet.encrypt(mdpentry.get().encode())

#this is a function used to crete a database and store it in the database also with it various exceptions   
def lite():
    conn  = sqlite3.connect("database.db")
    
    d = {
    "nom": nomentry.get(),
    "prenom": prenomentry.get(),
    "email": emailentry.get(),
    "mdp" : encmdp 
    }


    if nomentry.get() == "" or prenomentry.get()== "" or emailentry.get() =="" or mdpentry.get()=="":    
        messagebox.showerror("Error", " Veuillez saisir les champs ") 

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)



    elif nomentry.get().isspace() == "" or  prenomentry.get().isspace() == "": 
        messagebox.showerror("Error", " Veuillez saisir les champs ") 

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)
        


    elif cmdpentry.get() != mdpentry.get():   
        messagebox.showerror(" Error ", " Les mots de passe ne correspondent pas ")

        nomentry.delete(0,END)
        prenomentry.delete(0, END)
        emailentry.delete(0, END)
        mdpentry.delete(0, END)
        cmdpentry.delete(0, END)



    elif cmdpentry.get() == mdpentry.get():
        if(re.fullmatch(regex, emailentry.get())):
            
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS informations (   
                    nom text,
                    prenom text,
                    email text, 
                    mdp text
                )""")


            c.execute("INSERT INTO informations VALUES(:nom, :prenom, :email, :mdp)", d)
            
            nomentry.delete(0,END)
            prenomentry.delete(0, END)
            emailentry.delete(0, END)
            mdpentry.delete(0, END)
            cmdpentry.delete(0, END)


            conn.commit()
            conn.close()
            messagebox.showinfo("Info", "Vous êtes inscrit ") 
      
            frame3.pack_forget()
            frame4.pack(pady=300, ipadx=25)  


        else: 
            messagebox.showerror("Error", "Merci de saisir votre adresse email au format : votreexemple@exemple.com") 

            nomentry.delete(0,END)
            prenomentry.delete(0, END)
            emailentry.delete(0, END)
            mdpentry.delete(0, END)
            cmdpentry.delete(0, END)
    
        
            
    
btn4 = Button(frame3, text="S'inscrire", command=lite,  font="Arial 20")
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

#this is a function i creted to decryt the password and verify if it is the same password stored in the database
def connected():        
    connecte = sqlite3.connect('database.db')
    
    dictornary={
    "username": Username_entry.get(), 
    "mdp": encmdp
    }
  
    c = connecte.cursor()      
    c.execute("SELECT * FROM informations WHERE email=:username AND mdp=:mdp", dictornary)
    donnes = c.fetchall()
    
    encmd = fernet.decrypt(encmdp).decode()
    
    for i in donnes:
        if  Username_entry.get() in i   and encmdp in i  :
            messagebox.showinfo("Info", "Vous êtes connecte")
            break
        else:      
            messagebox.showerror("Error", "Vous n'avez pas de compte")
       
    connecte.commit()
    connecte.close()
    frame4.pack_forget()
    frame5.pack(pady=25,ipadx=100)


btn6 = Button(frame4, text="Se Connecté", command=connected, font="Arial 20")
btn6.pack(ipady=5, pady=15)

btn7 = Button(frame4, text="Retour", font="Arial 20", command=return2)
btn7.pack(ipady=5, pady=15)

#The Accueil menu to do a reservation.
frame5 = Frame(window, highlightbackground="#191970", highlightthickness=5)
frame5.configure(bg="#2779b8")


#This is the header of the Page of Reservation
heading = Label(frame5, text="Accueil", font="Arial 30 underline", bg="#2779b8", )
heading.pack()
heading1 = Label(frame5, text="Faire une réservation",font="Arial 25 underline", bg="#2779b8")
heading1.pack()


#This is the Destination label
destinationLabel = Label(frame5, text="Où allez-vous", font="Arial 20 ", bg="#2779b8")
destinationLabel.pack(ipady=5, pady=5, anchor='nw')



#This is the destination comboBox menu chose
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


#I created this function to show the date selected by the user.
def selectedc1():      
    date1.config(text="Vous avez sélectionné cette date:" + cal1.get_date())


#I created this function to show the date selected by the user.
def selectedc2():      
    date2.config(text="Vous avez sélectionné cette date:" + cal2.get_date())



#This is the arrival label  
arrival = Label(frame5, text="Jour d'arrivée", font="Arial 20", bg="#2779b8")
arrival.pack(ipady=3, pady=3, anchor='nw')


#This is the first calendar I created for the user to select his date from.
cal1 = Calendar(frame5, selectmode = 'day',year = 2022, month = 1,day = 22)
cal1.pack(pady =3,padx=3,anchor='nw')

btn8 = Button(frame5, text="Vailde" ,command=selectedc1, highlightbackground="#2779b8" )
btn8.pack(pady=3, anchor='nw')


#this is an empty label to show the date 
date1 = Label(frame5, text="", bg="#2779b8")
date1.pack(pady=3, anchor='nw')


#this is the destination label
departureLabel = Label(frame5, text="Jour de départ",font="Arial 20", bg="#2779b8")
departureLabel.pack(ipady=3, pady=3, anchor='nw')


#This is the second calendar I created for the user to select his date from.
cal2 = Calendar(frame5, selectmode = 'day',year = 2022, month = 3,day = 22)
cal2.pack(pady = 3,padx=3,anchor='nw')

btn9 = Button(frame5, text="Vailde", command=selectedc2, highlightbackground="#2779b8" )
btn9.pack(pady=3, anchor='nw')


#this is an empty label to show to the date 
date2 = Label(frame5, text="", bg="#2779b8")
date2.pack(pady=3, anchor='nw')


#this is the adults label 
adultsLabel = Label(frame5, text="Nombre D'Adultes", font="Arial 20", bg="#2779b8")
adultsLabel.pack(ipady=5, pady=5, anchor='nw')


#this is the adults comboBox which the user selects the number of dates 
adults = Combobox(frame5, width = 45, state='readonly')
adults['values'] = ("0","1","2","3","4","5","6","7","8","9","10","11")
adults.pack(pady=5,padx=5,anchor='nw')


#this is the children label 
childrenLabel = Label(frame5, text="Nombre D'Enfants", font="Arial 20", bg="#2779b8")
childrenLabel.pack(ipady=5, pady=5, anchor='nw')


#this is the children comboBox 
children = Combobox(frame5, width = 45, state='readonly')
children['values'] = ("0","1","2","3","4","5","6","7","8","9","10", "11")
children.pack(pady=5,padx=5,anchor='nw')


#this is the rooms label 
roomslabel = Label(frame5, text="Nombre de chambres que vous souhaitez réserver", font="Arial 20", bg="#2779b8")
roomslabel.pack(ipady=5, pady=5, anchor='nw')


#this is the rooms comboBox
rooms = Combobox(frame5, width = 45, state='readonly')
rooms['values'] = ("0","1","2","3","4","5","6","7","8","9","10","11")
po = rooms.get()
rooms.pack(pady=5,padx=5,anchor='nw')

#this is a function i created to store all the infomations from the menu into a database.
def menudata():

    menu = sqlite3.connect('menubase.db')
    dictmenu = {
        "destination": destination.get(),
        "arrival": cal1.get_date(),
        "deputure": cal2.get_date(),
        "adults": adults.get(), 
        "children": children.get(),
        "rooms": rooms.get()
    }

    if destination.get() == '' or adults.get() == '' or children.get() == '' or rooms.get() == '':
        messagebox.showerror("Error", "Veuillez saisir le champs")
    elif destination.get().isspace() == "" or adults.get().isspace() == '' or children.get().isspace() == '' or rooms.get().isspace() == '':
        messagebox.showerror("Error", "Veuillez saisir le champs")
    else: 
        
        m = menu.cursor()
        m.execute("""CREATE TABLE IF NOT EXISTS menudata(
                destination text, 
                arrival text, 
                deputure text, 
                adults integer, 
                children integer,
                rooms integer
            )""")

        m.execute("INSERT INTO menudata VALUES(:destination, :arrival, :deputure, :adults, :children, :rooms)", dictmenu)

        menu.commit()
        menu.close()
        destination.set('')
        adults.set('')
        children.set('')
        rooms.set('')
        frame5.pack_forget()
        frame6.pack(pady=100, ipadx=20)


reserve = Button(frame5,text="Reservée" , command=menudata, font="Arial 14")
reserve.pack(ipady=5, pady=10)

quite= Button(frame5, text="Quitter", command=return3, font="Arial 14")
quite.pack(pady=3, ipadx=5)

def destiny(): 
    desti.config(text="Vous allez à " + destination.get())
    btn12.pack_forget()
    
def ert():           
    arri.configure(text="Le jour de votre arrivée est " + cal1.get_date())
    btn13.pack_forget()

def ter():
    dept.configure(text="Le jour de votre départ est " + cal2.get_date())
    btn14.pack_forget()
    
def yot():      
    adus.configure(text="Il y a " + adults.get() + " adultes ")
    btn15.pack_forget()

def reel():    
    chi.configure(text="Il y a " + children.get() + " enfants ")
    btn16.pack_forget()
    
def real():    
    rombo.configure(text="Vous avez demandé " + rooms.get() + "chambres")
    btn17.pack_forget()
    
    

frame6 = Frame(window, highlightbackground="#191970", highlightthickness=5)
frame6.configure(bg="#2779b8")

Dest = Label(frame6, text="Votre Destination" , font="Arial 20", bg="#2779b8")
Dest.pack(pady=5, anchor='nw')

desti= Label(frame6, text=" ", font="Arial 16", bg="#2779b8")
desti.pack(pady=5, anchor='nw')

btn12 = Button(frame6,text="Voir",font="Arial 16", command=destiny)
btn12.pack(pady=5,anchor='nw')

arr = Label(frame6, text='Le jour de votre arrivée ', font="Arial 20", bg="#2779b8")
arr.pack(pady=5, anchor='nw')

arri = Label(frame6, text=" ", bg="#2779b8", font="Arial 16")
arri.pack(pady=5, anchor='nw')

btn13 = Button(frame6,text="Voir",font="Arial 16",command=ert)
btn13.pack(pady=5, anchor='nw')


dep = Label(frame6, text="Votre Jour De Départ", font="Arial 20", bg="#2779b8")
dep.pack(pady=5, anchor='nw')

dept = Label(frame6, text=" ", bg="#2779b8", font="Arial 16" )
dept.pack(pady=5, anchor='nw')

btn14 = Button(frame6,text="Voir",font="Arial 16", command=ter)
btn14.pack(pady=5, anchor='nw')

adul = Label(frame6, text="Nombre D'Adults",font="Arial 20", bg="#2779b8" )
adul.pack(pady=5, anchor='nw')

adus = Label(frame6, text=" ", font="Arial 16", bg="#2779b8")
adus.pack(pady=5, anchor='nw')

btn15 = Button(frame6,text="Voir",font="Arial 16",command=yot )
btn15.pack(pady=5, anchor='nw')

child = Label(frame6, text="Nombre D'Enfants", font="Arial 20", bg="#2779b8")
child.pack(pady=5, anchor='nw')

chi = Label(frame6, text=" ", font="Arial 16", bg="#2779b8")
chi.pack(pady=5, anchor='nw')

btn16 = Button(frame6,text="Voir",font="Arial 16", command=reel)
btn16.pack(pady=5, anchor='nw')

rom = Label(frame6, text="Chambres", font="Arial 20", bg="#2779b8")
rom.pack(pady=5, anchor='nw')

rombo = Label(frame6, text=" ", font="Arial 16", bg="#2779b8",)
rombo.pack(pady=5, anchor='nw')

btn17 = Button(frame6,text="Voir",font="Arial 16", command=real)
btn17.pack(pady=5, anchor='nw')

btn10 = Button(frame6, text="Faire une autre réservation", command=return5, font="Arial 15")
btn10.pack(pady=10, ipady=3)

btn11 = Button(frame6, text="Se Déconnecte", command=return4, font="Arial 15")
btn11.pack(pady=10, ipady=3)















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








window.mainloop()
