from app.modelos import Cifrador



def test_cifrador():

    cifrador = Cifrador(3)
    assert  cifrador.cifrar("DIEGO") == "GLHJR"