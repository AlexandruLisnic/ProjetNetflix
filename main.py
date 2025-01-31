import tkinter as tk
from tkinter import messagebox
from Lisnic import Employe, Client

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Application Gestion Films")

        # Liste d'employés avec mot de passe haché et niveaux d'accès
        self.employes = [Employe("admin", "admin123", "total"), Employe("user", "user123", "lecture")]

        # Liste de clients
        self.clients = []

        # Fenêtre de login
        self.login_window()

    def login_window(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        self.username_label = tk.Label(self.login_frame, text="Nom d'utilisateur:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Mot de passe:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Se connecter", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Vérification des identifiants
        employe = next((e for e in self.employes if e.username == username), None)
        if employe and employe.check_password(password):
            self.login_frame.destroy()
            self.main_window(employe)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def main_window(self, employe):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Accès aux films et aux clients en fonction du niveau d'accès
        self.clients_listbox = tk.Listbox(self.main_frame)
        self.clients_listbox.pack()

        self.film_listbox = tk.Listbox(self.main_frame)
        self.film_listbox.pack()

        # Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Quitter", command=self.quit)
        self.menu.add_command(label="Déconnexion", command=self.logout)

        if employe.access_level == "total":
            self.create_client_button = tk.Button(self.main_frame, text="Créer un client", command=self.create_client_window)
            self.create_client_button.pack()

            self.modify_client_button = tk.Button(self.main_frame, text="Modifier un client", command=self.modify_client_window)
            self.modify_client_button.pack()

            self.delete_client_button = tk.Button(self.main_frame, text="Supprimer un client", command=self.delete_client)
            self.delete_client_button.pack()

    def create_client_window(self):
        self.create_client_frame = tk.Frame(self.root)
        self.create_client_frame.pack()

        self.nom_label = tk.Label(self.create_client_frame, text="Nom:")
        self.nom_label.pack()

        self.nom_entry = tk.Entry(self.create_client_frame)
        self.nom_entry.pack()

        self.prenom_label = tk.Label(self.create_client_frame, text="Prénom:")
        self.prenom_label.pack()

        self.prenom_entry = tk.Entry(self.create_client_frame)
        self.prenom_entry.pack()

        self.email_label = tk.Label(self.create_client_frame, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.create_client_frame)
        self.email_entry.pack()

        self.mdp_label = tk.Label(self.create_client_frame, text="Mot de passe:")
        self.mdp_label.pack()

        self.mdp_entry = tk.Entry(self.create_client_frame, show="*")
        self.mdp_entry.pack()

        self.save_button = tk.Button(self.create_client_frame, text="Sauvegarder", command=self.save_client)
        self.save_button.pack()

    def save_client(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        email = self.email_entry.get()
        mdp = self.mdp_entry.get()

        client = Client(nom, prenom, email, mdp)

        # Validation
        if not client.validate_email(self.clients):
            messagebox.showerror("Erreur", "L'email est déjà utilisé.")
            return
        if not client.validate_password():
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
            return

        self.clients.append(client)
        self.create_client_frame.destroy()
        messagebox.showinfo("Succès", "Client ajouté avec succès.")

    def modify_client_window(self):
        # Implémenter la modification d'un client ici
        pass

    def delete_client(self):
        # Implémenter la suppression d'un client ici
        pass

    def logout(self):
        self.main_frame.destroy()
        self.login_window()

    def quit(self):
        self.root.quit()

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()