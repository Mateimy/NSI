""""Code réalisé par les petits Lisandre et Matei"""

from tkinter import Tk, Canvas, PhotoImage
from random import randint as rd
from time import sleep, time
from random import choice, randint

class obj1:
    def __init__(self, posX, posY, depX, depY, size, color, image):
        self.x = posX
        self.y = posY
        self.vX = depX
        self.vY = depY
        self.size = size
        self.color = color
        self.image = image
        self.shape = None  # Variable pour stocker la référence à la forme dessinée

colors = ['red', 'green', 'yellow', 'orange', 'purple', 'cyan', 'black', 'brown', 'pink', 'coral', 'gold']

fen = Tk()
can = Canvas(fen, height=600, width=600, bg='white')
can.pack()
cpt = 0

# Chargement des images
juliette = PhotoImage(file="grenouille.gif", format="gif -index "+str(cpt))
gerard_images = [PhotoImage(file="mouche1.gif", format="gif -index 0"),
                 PhotoImage(file="mouche2.gif", format="gif -index 0"),
                 PhotoImage(file="mouche3.gif", format="gif -index 0")]
gerard_index = 0

nbObjet = 10
objet1 = []

# Création des objets
for i in range(nbObjet):
    color = choice(colors)
    objet1.append(obj1(rd(100, 500),
                       rd(100, 500),
                       rd(-15, 15),
                       rd(-15, 15),
                       10, color, gerard_images[randint(0, 2)]))

# Création du gros carré noir
can.create_rectangle(250, 250, 350, 350, fill='cyan', outline='green')

# Variables pour le timer et le compteur d'objets
start_time = time()

# Boucle de rafraîchissement
while True:
    sleep(0.02)
    # Effacer le contenu du canvas
    can.delete('all')
    
    # Mise à jour des positions des objets et gestion des rebonds
    for i in range(nbObjet):
        prochainX = objet1[i].x + objet1[i].vX
        prochainY = objet1[i].y + objet1[i].vY

        # Vérifier s'il y a collision avec le carré noir
        if prochainX >= 250 - objet1[i].size and prochainX <= 350 + objet1[i].size and \
                prochainY >= 250 - objet1[i].size and prochainY <= 350 + objet1[i].size:
            objet1[i].vX *= 1
            objet1[i].vY *= -1
        else:
            # Vérifier les rebonds sur les bords de la fenêtre
            if prochainX > objet1[i].size and prochainX < 600 - objet1[i].size:
                objet1[i].x = prochainX
            else:
                # Faire réapparaître l'objet de l'autre côté
                objet1[i].x = 600 - objet1[i].size if prochainX <= objet1[i].size else objet1[i].size

            if prochainY > objet1[i].size and prochainY < 600 - objet1[i].size:
                objet1[i].y = prochainY
            else:
                # Faire réapparaître l'objet de l'autre côté
                objet1[i].y = 600 - objet1[i].size if prochainY <= objet1[i].size else objet1[i].size
        
        # Dessiner l'objet sur le canvas
        objet1[i].shape = can.create_image(objet1[i].x, objet1[i].y, image=objet1[i].image)

    # Redessiner le carré noir et l'image de la grenouille
    can.create_rectangle(250, 250, 350, 350, fill='cyan', outline='green')
    can.create_image(315, 310, image=juliette)
    can.create_text(300, 265, text="CATCH LES\n MOUCHES", font=("Arial", 10), fill="black")
    can.create_text(312, 343, text="MIAaaaaaM 20/20", font=("Arial", 7), fill="red")

    # Mettre à jour l'index de l'image de la grenouille pour créer une animation
    cpt += 1
    cpt %= 8
    juliette.configure(format="gif -index "+str(cpt//2))

    # Mettre à jour l'image des mouches gif pour créer une animation
    gerard_index += 1
    gerard_index %= 3
    gerard = gerard_images[gerard_index]

    # Calculer le temps écoulé depuis le début
    elapsed_time = time() - start_time
    timer_text = "Timer: {:.2f}".format(elapsed_time)

    # Afficher le timer en haut à gauche de la fenêtre
    can.create_text(10, 10, anchor='nw', text=timer_text, font=("Arial", 12), fill="black")

    # Mise à jour du compteur d'objets
    can.create_text(300, 20, text="nombre de mouches = {}".format(nbObjet), font=("Arial", 12), fill="black")

    # Rafraîchir la fenêtre
    fen.update()

fen.mainloop()
