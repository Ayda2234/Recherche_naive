import random 
import time
import matplotlib as plt


def recherche_naive(element_cible, sequence):
    """
    Recherche naïve de l'élément cible dans la séquence.

    Parameters:
    - element_cible: L'élément que nous recherchons.
    - sequence: La séquence dans laquelle nous effectuons la recherche.
    - occurrence : l'occurrences of the cible element in the sequence

    Returns:
    - True si l'élément cible est trouvé, False sinon.
    """
    occurrences = 0 
    for element in sequence:
        if element == element_cible:
             occurrences += 1  # L'élément cible a été trouvé, donc retourne True
    return occurrences # le nombre d'occurence de l'element cible 

# Exemple d'utilisation
ma_sequence = [1, 2, 3, 4, 5, 3, 5, 3]
element_recherche = 5

resultat = recherche_naive(element_recherche, ma_sequence)

if resultat > 0:
    print(f"L'élément {element_recherche} a été trouvé dans la séquence. et son occurence est {resultat}")
else:
    print(f"L'élément {element_recherche} n'a pas été trouvé dans la séquence.")
