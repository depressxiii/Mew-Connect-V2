import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

# Fonction pour envoyer un message au serveur
def send_message():
    message = entry.get()
    if message:
        full_message = f"{username}: {message}"  # Inclure le nom d'utilisateur
        client.send(full_message.encode('utf-8'))
        entry.delete(0, tk.END)

# Fonction pour afficher un message reçu dans la zone de texte
def display_message(message):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, message + '\n')
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

# Fonction pour gérer la réception de messages du serveur
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            display_message(message)
        except:
            print("Erreur")
            client.close()
            break

# Fonction pour définir le nom d'utilisateur
def set_username():
    global username
    username = username_entry.get()
    username_label.config(text=f"Nom d'utilisateur : {username}")
    username_entry.destroy()
    set_username_button.destroy()

# Fonction pour définir la taille de la fenêtre
def set_window_size():
    new_width = int(width_entry.get())
    new_height = int(height_entry.get())
    root.geometry(f"{new_width}x{new_height}")

# Configuration du socket pour le client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

# Création de l'interface en utilisant Tkinter
root = tk.Tk()
root.title("★  Meow Connect  ★")

# Définir l'icône de la fenêtre
root.iconbitmap("pixi.ico")  # Remplacez "chemin_vers_votre_icone.ico" par le chemin de votre fichier d'icône

# Configuration de l'arrière-plan
root.configure(bg='#F4BEF4')  # Arrière-plan bleu clair

# Créer un widget Canvas pour l'image
canvas = tk.Canvas(root, bg='#F4BEF4', width=400, height=300)  # Ajustez les dimensions au besoin
canvas.pack(padx=10, pady=10)

# Charger et afficher l'image
image = Image.open("pix.jpg")  # Remplacez par le chemin de votre image
image = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=image)

chat_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, font=('Helvetica', 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, bg='#F0F0F0', font=('Helvetica', 12), bd=2, relief=tk.SOLID)
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

send_button = tk.Button(root, text="Envoyer", command=send_message, bg='#4CAF50', fg='white', font=('Helvetica', 12), bd=2, relief=tk.RAISED, padx=10)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Ajouter la fonctionnalité pour définir le nom d'utilisateur
username_label = tk.Label(root, text="Entrez votre nom d'utilisateur :", font=('Helvetica', 12))
username_label.pack(padx=10, pady=5)

username_entry = tk.Entry(root, bg='#F0F0F0', font=('Helvetica', 12), bd=2, relief=tk.SOLID)
username_entry.pack(padx=10, pady=5)

set_username_button = tk.Button(root, text="Définir le nom d'utilisateur", command=set_username, bg='#4CAF50', fg='white', font=('Helvetica', 12), bd=2, relief=tk.RAISED, padx=10)
set_username_button.pack(padx=10, pady=5)


# Définir la taille initiale de la fenêtre à 1300x630
root.geometry("630x1000")

# Démarrer le thread pour recevoir des messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

root.mainloop()
