import tkinter as tk
from PIL import Image, ImageTk
import pygame
import serverbackend

# Fonction qui sera appelée lorsque le bouton est cliqué
def bouton_clique():
    print("Le serveur est sur écoute... Patientez un moment")
    server.receive()  # Vous devez ajouter le code pour la fonction server.receive() ici

# Créer une fenêtre
fenetre = tk.Tk()

# Changer le logo de la fenêtre
fenetre.iconbitmap("pixi.ico")  # Remplacez "votre_logo.ico" par le chemin de votre fichier d'icône

# Changer le titre de la fenêtre (la barre de titre)
fenetre.title("★  Meow Connect  ★")  # Remplacez "Nouveau Titre" par le titre que vous souhaitez

# Personnaliser les couleurs
fenetre.configure(bg="#E6ACE6")  # Couleur de fond

# Changer la taille de la fenêtre
fenetre.geometry("384x480")  # Définir la taille de la fenêtre

# Initialiser Pygame pour la musique
pygame.mixer.init()
pygame.mixer.music.load("clairo.mp3")  # Remplacez "votre_musique.mp3" par le chemin de votre fichier audio
pygame.mixer.music.set_volume(0.9)  # Réglez le volume (facultatif)
pygame.mixer.music.play(-1)  # "-1" signifie que la musique se répétera en boucle

# Charger le GIF animé
image = Image.open("girlcat.gif")
photo = ImageTk.PhotoImage(image)

# Créer une étiquette pour le GIF
gif_label = tk.Label(fenetre, image=photo, bg="#E6ACE6")
gif_label.image = photo
gif_label.place(relx=0.5, rely=0.5, anchor="center")

# Personnaliser le bouton
cadre = tk.Frame(fenetre, bd=0)
cadre.place(relx=0.5, rely=0.6, anchor="s")

# Bouton pour démarrer l'animation
def demarrer_animation():
    gif_label.configure(image=photo)
    fenetre.after(0, update_gif, 0)

demarrer_bouton = tk.Button(cadre, text="Démarrer l'animation", command=demarrer_animation, bg="#F3506E", fg="white", font=("Helvetica", 12), bd=5, relief=tk.RAISED)
demarrer_bouton.pack(padx=0, pady=0)

# Fonction pour mettre à jour le GIF
def update_gif(frame):
    image.seek(frame)
    photo = ImageTk.PhotoImage(image)
    gif_label.configure(image=photo)
    gif_label.image = photo
    frame = (frame + 1) % image.n_frames
    fenetre.after(100, update_gif, frame)

# Personnaliser le bouton "Meow Meow~~"
bouton = tk.Button(fenetre, text="Meow Meow~~", command=bouton_clique, bg="#F3506E", fg="white", font=("Helvetica", 16), bd=5, relief=tk.RAISED)
bouton.place(relx=0.5, rely=0.9, anchor="s")

# Créer une étiquette vide
label = tk.Label(fenetre, text="")
label.place(relx=0.5, rely=0.75, anchor="center")

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
