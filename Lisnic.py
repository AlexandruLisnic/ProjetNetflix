# La classe de base "Personne" avec des attributs simples
class Personne:
    def __init__(self, nom, prenom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

# La classe "Client" qui hérite de "Personne"
class Client(Personne):
    def __init__(self, nom, prenom, sexe, courriel, password):
        super().__init__(nom, prenom, sexe)
        self.courriel = courriel
        self.password = password

# Une classe simple pour représenter un film
class Film:
    def __init__(self, nom, duree, description):
        self.nom = nom
        self.duree = duree
        self.description = description
