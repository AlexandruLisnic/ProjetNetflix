import unittest
from Lisnic import Employe, Client

class TestEmploye(unittest.TestCase):

    def test_hash_password(self):
        employe = Employe("testuser", "testpassword", "total")
        self.assertEqual(len(employe.password), 64)  # Le hash doit avoir une longueur de 64 caractères

    def test_check_password(self):
        employe = Employe("testuser", "testpassword", "total")
        self.assertTrue(employe.check_password("testpassword"))
        self.assertFalse(employe.check_password("wrongpassword"))

class TestClient(unittest.TestCase):

    def test_validate_email(self):
        client1 = Client("John", "Doe", "john.doe@example.com", "password123")
        client2 = Client("Jane", "Doe", "john.doe@example.com", "password123")
        clients = [client1]
        self.assertTrue(client2.validate_email(clients))  # L'email n'est pas encore utilisé
        client1.email = "jane.doe@example.com"  # Modifier l'email du client 1
        self.assertFalse(client2.validate_email(clients))  # L'email est déjà utilisé

    def test_validate_password(self):
        client = Client("John", "Doe", "john.doe@example.com", "password123")
        self.assertTrue(client.validate_password())
        client.mot_de_passe = "short"
        self.assertFalse(client.validate_password())  # Le mot de passe est trop court

if __name__ == "__main__":
    unittest.main()