import tkinter as tk
from tkinter import ttk
from Lisnic import clients, films, employes


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")

        self.logged_in_user = None

        self.create_login_window()

    def create_login_window(self):
        """Affiche la fenêtre de connexion."""
        self.clear_window()

        tk.Label(self.root, text="Code utilisateur:").pack()
        self.entry_user = tk.Entry(self.root)
        self.entry_user.pack()

        tk.Label(self.root, text="Mot de passe:").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(self.root, text="Se connecter", command=self.verify_login)
        self.btn_login.pack()

    def verify_login(self):
        """Vérifie les identifiants de connexion."""
        username = self.entry_user.get()
        password = self.entry_password.get()

        for emp in employes:
            if emp.code_utilisateur == username and emp.password == emp.hash_password(password):
                self.logged_in_user = emp
                self.create_main_window()
                return

        tk.messagebox.showerror("Erreur", "Identifiants incorrects")

    def create_main_window(self):
        """Affiche la fenêtre principale après connexion."""
        self.clear_window()

        tk.Label(self.root, text=f"Bienvenue, {self.logged_in_user.prenom}").pack()

        frame_clients = ttk.LabelFrame(self.root, text="Clients")
        frame_clients.pack(fill="both", expand=True, padx=10, pady=10)

        tree_clients = ttk.Treeview(frame_clients, columns=("Nom", "Prénom", "Courriel"), show="headings")
        tree_clients.heading("Nom", text="Nom")
        tree_clients.heading("Prénom", text="Prénom")
        tree_clients.heading("Courriel", text="Courriel")

        for client in clients:
            tree_clients.insert("", "end", values=(client.nom, client.prenom, client.courriel))

        tree_clients.pack(fill="both", expand=True)

        frame_films = ttk.LabelFrame(self.root, text="Films")
        frame_films.pack(fill="both", expand=True, padx=10, pady=10)

        tree_films = ttk.Treeview(frame_films, columns=("Nom", "Durée", "Catégories"), show="headings")
        tree_films.heading("Nom", text="Nom")
        tree_films.heading("Durée", text="Durée")
        tree_films.heading("Catégories", text="Catégories")

        for film in films:
            tree_films.insert("", "end", values=(film.nom, film.duree, ", ".join(film.categories)))

        tree_films.pack(fill="both", expand=True)

        self.btn_logout = tk.Button(self.root, text="Se déconnecter", command=self.create_login_window)
        self.btn_logout.pack()

    def clear_window(self):
        """Efface le contenu de la fenêtre."""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
