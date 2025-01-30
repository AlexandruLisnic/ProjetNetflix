import tkinter as tk
from tkinter import messagebox
from Lisnic import Client, Film

# Liste des employés (hardcodé)
employes = [
    {"code_utilisateur": "admin", "password": "admin123", "type_acces": "total"},
    {"code_utilisateur": "lecteur", "password": "lecteur123", "type_acces": "lecture"}
]

# Fonction de vérification des identifiants
def verifier_login(code, password):
    for employe in employes:
        if employe["code_utilisateur"] == code and employe["password"] == password:
            return employe["type_acces"]
    return None

# Liste de clients (hardcodé)
clients = [
    Client("Doe", "John", "M", "john.doe@email.com", "password123"),
    Client("Smith", "Jane", "F", "jane.smith@email.com", "password123")
]

# Liste de films (hardcodé)
films = [
    Film("Action Movie", "1h30", "A thrilling action movie."),
    Film("Comedy Movie", "1h00", "A funny comedy film.")
]

# Fenêtre principale
def afficher_principal(acces):
    root = tk.Tk()
    root.title("Application de gestion")

    # Label d'information selon l'accès
    if acces == "total":
        tk.Label(root, text="Bienvenue (Accès total)").pack()
    elif acces == "lecture":
        tk.Label(root, text="Bienvenue (Accès lecture uniquement)").pack()

    # Affichage de la liste des clients
    tk.Label(root, text="Clients").pack()
    for client in clients:
        tk.Label(root, text=f"{client.nom} {client.prenom} - {client.courriel}").pack()

    # Affichage de la liste des films
    tk.Label(root, text="Films").pack()
    for film in films:
        tk.Label(root, text=f"{film.nom} - {film.duree}").pack()

    # Menu pour quitter ou se déconnecter
    def quitter():
        root.quit()

    tk.Button(root, text="Quitter", command=quitter).pack()

    root.mainloop()

# Fenêtre de connexion
def afficher_login():
    def tenter_connexion():
        code = entree_code.get()
        password = entree_password.get()

        acces = verifier_login(code, password)
        if acces:
            messagebox.showinfo("Succès", "Connexion réussie !")
            root.destroy()
            afficher_principal(acces)
        else:
            messagebox.showerror("Erreur", "Code utilisateur ou mot de passe incorrect.")

    root = tk.Tk()
    root.title("Connexion")

    tk.Label(root, text="Code utilisateur :").pack()
    entree_code = tk.Entry(root)
    entree_code.pack()

    tk.Label(root, text="Mot de passe :").pack()
    entree_password = tk.Entry(root, show="*")
    entree_password.pack()

    tk.Button(root, text="Se connecter", command=tenter_connexion).pack()

    root.mainloop()

if __name__ == "__main__":
    afficher_login()
