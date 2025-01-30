import hashlib
import tkinter.messagebox as messagebox


class Personne:
    """Classe de base représentant une personne avec des attributs communs."""
    def __init__(self, nom, prenom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe


class Client(Personne):
    """Classe représentant un client avec des informations supplémentaires."""
    def __init__(self, nom, prenom, sexe, courriel, password):
        super().__init__(nom, prenom, sexe)
        self.courriel = courriel
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hash le mot de passe pour plus de sécurité."""
        return hashlib.sha256(password.encode()).hexdigest()


class Employe(Personne):
    """Classe représentant un employé qui peut accéder au système."""
    def __init__(self, nom, prenom, sexe, code_utilisateur, password, acces):
        super().__init__(nom, prenom, sexe)
        self.code_utilisateur = code_utilisateur
        self.password = self.hash_password(password)
        self.acces = acces  # "total" ou "lecture"

    @staticmethod
    def hash_password(password):
        """Hash le mot de passe pour plus de sécurité."""
        return hashlib.sha256(password.encode()).hexdigest()


class Film:
    """Classe représentant un film avec ses informations."""
    def __init__(self, nom, duree, description, categories):
        self.nom = nom
        self.duree = duree
        self.description = description
        self.categories = categories  # Liste des catégories

    def __str__(self):
        return f"{self.nom} ({self.duree}) - {', '.join(self.categories)}"


# Données de test
clients = [
    Client("Dupont", "Jean", "M", "jean.dupont@mail.com", "password123"),
    Client("Martin", "Sophie", "F", "sophie.martin@mail.com", "abc12345")
]

employes = [
    Employe("Admin", "Super", "M", "admin", "adminpass", "total"),
    Employe("Lecteur", "Simple", "F", "lecteur", "lecturepass", "lecture")
]

films = [
    Film("Inception", "2h28", "Un film de science-fiction sur les rêves.", ["Science-fiction", "Thriller"]),
    Film("Titanic", "3h15", "Une romance dramatique sur le naufrage du Titanic.", ["Romance", "Drame"])
]
