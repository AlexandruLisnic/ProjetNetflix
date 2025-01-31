import hashlib


class Employe:
    def __init__(self, username, password, access_level):
        self.username = username
        self.password = self.hash_password(password)
        self.access_level = access_level

    def hash_password(self, password):
        """Hashage du mot de passe pour la sécurité"""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Vérifier le mot de passe"""
        return self.password == self.hash_password(password)


class Client:
    def __init__(self, nom, prenom, email, mot_de_passe):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe

    def validate_email(self, clients_list):
        """Vérifier si l'email est unique"""
        for client in clients_list:
            if client.email == self.email:
                return False
        return True

    def validate_password(self):
        """Vérifier si le mot de passe est valide (min 8 caractères)"""
        return len(self.mot_de_passe) >= 8


class Film:
    def __init__(self, nom, duree, categories, acteurs):
        self.nom = nom
        self.duree = duree
        self.categories = categories
        self.acteurs = acteurs