#def trie_personaliser(e):
    # return e  # tri en audre alphabetique
    # return len(e) # tri en longeur de text




# ici j'affiche ma collection de pizzas
def afficher_pizza(collection, n_premieres_elements= -1):
    c = collection
    if not n_premieres_elements == -1:
        c = collection[0:n_premieres_elements]
    # collection.sort(reverse=True, key=trie_personaliser)
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZAS")
    else:
        print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        # print(f"---- LISTE DES PIZZAS ({len(collection)}) ----")
        for i in c:
            print(i)
        print()
        print("Première pizza: " + c[0])
        print("Dernière pizza: " + c[-1])



# ici c'est ma collection de pizzas
pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]




# vide = ()


# ici c'est la fonction pour ajouter une pizza
def ajouter_pizza_utilisateur(collection):
    p = input(f"Ajouter une Pizza: ")
    if p.lower() in collection:
        print("ERREUR: Cette pizza existe déjà!")
    else:
        collection.append(p)


"""ici je verifie si la pizza existe où pas avent d'ajouter"""


def pizza_existe(e, collection):
    for i in collection:
        if i == 0:
            return True
    return False


# ici j'appel mes fonction
ajouter_pizza_utilisateur(pizzas)
afficher_pizza(pizzas)


"""
# lower() -> signifie passer en minsuscules
# upper() _> --//-- en MAJUSCULES
# reveres = True _> pour renverser
# Exemple
s = "Bonjour"
print(s)
print(s.lower())
print(s.upper()) """