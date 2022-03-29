from tkinter import * 
import sys
import os
import tkinter
import pygame

pygame.init()

fenetre = Tk(className='Arthus Client')
fenetre.geometry("1920x1080")
#fenetre.iconbitmap("artus/client.png")
label = Label(fenetre, text="Combien de cléments ?")
label.pack()
s = Spinbox(fenetre, from_=0, to=69)
s.pack()

trucdeouf = pygame.mixer.Sound("songs/trucdeouf.wav")

trucdeouf.play()
bouton = Checkbutton(fenetre, text="FPS Booster")
bouton.pack()

bouton = Checkbutton(fenetre, text="Kill Aura")
bouton.pack()

bouton = Checkbutton(fenetre, text="/admin")
bouton.pack()

bouton = Checkbutton(fenetre, text="Rich")
bouton.pack()

bouton = Checkbutton(fenetre, text="/kill LowHighYT")
bouton.pack()

#L1 = Label(fenetre, text="Chemin du Client Lunaire")
#L1.pack( side = TOP)
#E1 = Entry(fenetre, bd =5)
#E1.pack(side = TOP)

image = PhotoImage(file="artuslebest.png")

def launch():
    os.popen("clientlunaire.lnk")


bouton=Button(fenetre, image = image , command=launch)
bouton.pack()

photo = PhotoImage(file="client.png")

canvas = Canvas(fenetre,width=1920, height=1080)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()



fenetre.mainloop()
