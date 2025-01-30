from main import verifier_login

def test_login():
    assert verifier_login("admin", "admin123") == "total"
    assert verifier_login("lecteur", "lecteur123") == "lecture"
    assert verifier_login("fake", "fake") == None

test_login()
