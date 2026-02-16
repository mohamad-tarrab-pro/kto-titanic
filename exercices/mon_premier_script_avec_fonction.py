"""
Count names with more than seven letters
"""
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))

import unittest

def count_long_first_names(first_names: list[str], threshold: int = 7) -> int:
    """
    Compte le nombre de prénoms dont la longueur est strictement supérieure au seuil défini.
    """
    # On utilise une compréhension de liste pour la clarté et l'efficacité
    long_names = [name for name in first_names if len(name) > threshold]
    
    return len(long_names)

class TestNamesMethod(unittest.TestCase):
    def test_count_long_first_names(self):
        # Données de test
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        
        # Exécution
        resultat = count_long_first_names(first_names=prenoms)
        
        # Vérification (Guillaume, Juliette, François, Cassandre = 4)
        self.assertEqual(resultat, 4)

if __name__ == '__main__':
    unittest.main()