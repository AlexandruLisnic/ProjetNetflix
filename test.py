from Lisnic import Client, Employe


def test_client_creation():
    client = Client("Durand", "Paul", "M", "paul.durand@mail.com", "monpassword")
    assert client.nom == "Durand"
    assert client.prenom == "Paul"
    assert client.sexe == "M"
    assert client.courriel == "paul.durand@mail.com"
    assert client.password == client.hash_password("monpassword")


def test_employe_creation():
    employe = Employe("Boss", "Big", "M", "boss123", "adminpass", "total")
    assert employe.code_utilisateur == "boss123"
    assert employe.password == employe.hash_password("adminpass")
    assert employe.acces == "total"


def test_password_hashing():
    client = Client("Test", "User", "F", "test@mail.com", "securepass")
    assert client.password == client.hash_password("securepass")


if __name__ == "__main__":
    test_client_creation()
    test_employe_creation()
    test_password_hashing()
    print("Tous les tests sont passés avec succès ! ✅")
