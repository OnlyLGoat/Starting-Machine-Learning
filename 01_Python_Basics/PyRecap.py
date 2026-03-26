# Create Functions with Math Type ===================================

# f(x) = x2
# f = lambda x: x**2
# print(f(3))

# f(x, y) = x2 + y
# f = lambda x,y: x**2 + y
# print(f(3, 1))

# Create Complex Functions ===================================

# Function Energy Potentielle Example
# def energy_potentielle(masse, hauteur, g=9.81):
#     E = masse * hauteur * g
#     print(E, 'J')
# energy_potentielle(80, 5) # 3924 J

# Small Exercise
# def energy_potentielle_comparaison(masse, hauteur, e_limit, g=9.81 ):
#     E = masse * hauteur * g
#     if E > e_limit:
#         return 'Energie calculer est superieur a l energie limite'
#     elif E < e_limit:
#         return 'Energie calculer est inferieure a l energie limite'
# print(energy_potentielle(80, 5, 4000))

# Boucle For Recap ===================================

# for _ in range(10):
#     print('Bonjour')

# for i in range(10, -10, -3):
#     print(i)

# Boucle While Recap ===================================

# x = 0
# while x < 10:
#     print(x)
#     x += 1
# while x in range(10):
#     print(x)
#     x += 1

# Suite Fibonacci Exercise

# def suite_fibonacci(n):
#     a = 0
#     b = 1
#     list_1 = [a]
#     while b < n:
#         a, b = b, a+b
#         list_1.append(a)
#     return list_1
#
# print(suite_fibonacci(1000))


# List / Tuples Recap ===================================

# Lists / Not Protected(We can modify the values), 
#         Not Too Fast In Execution
# liste_1 = [1, 4, 2, 7, 37, 84]
# ville = ['Paris', 'Berlin', 'Londres', 'Bruxelles']
# liste_2 = [liste_1, ville]
# liste_3 = []

# # Tuples / Protected Values, Fast In Execution
# tuple_1 = (1, 2, 6, 1, 7)

# Slicing
# print(ville[:3])
# print(ville[1:])
# print(ville[1:3:2])
# print(ville[::2])
# print(ville[::-1])

# List Methods
# ville.append('Marrakech')
# ville.insert(2, 'Rabat')
# ville_2 = ['Tanger', 'Agadir']
# ville.extend(ville_2)
# lent = len(ville)
# print(lent)
# print(ville)

# ville.sort() # Trie Avec Ordre Alphabetic
# # print(ville)

# ville.sort(reverse=True) # Trie Avec Ordre Anti-Alphabetic
# print(ville)

# liste_1.sort() # Trie Minimum Vers Le Maximum
# print(liste_1)

# ...

# for index, value in enumerate(liste_1):
#     print(index, value)

# for a, b in zip(ville, liste_1):
#     print(a, b)


# Dictionnaire Recap ===================================

# dict_0 = {
#     "Chien": "dog",
#     "chat": "cat",
#     "souris": "mouse",
#     "oiseau": "bird"
# }

# import numpy as np
# params = {
#     "W1": np.random.randn(10, 100),
#     "b1": npm.random.randn(10, 1)
# }

# inv = {
#     "banane": 500,
# }

# dict_2 = {
#     "dict_1": dict_0,
#     "Inv": inv
# }

# Inventory = {
#     "bananes": 5000,
#     "pommes": 2094,
#     "poires": 412809,
#     "cerises": 2893
# }

# Inventory["abricots"] = 4902

# liste_5 = ('Paris', 'Londres', 'Rabat')
# Inventory.fromkeys(liste_5)
# Inventory.fromkeys(liste_5, 'valeur affecter a tout les cles')

# Fruits = Inventory.pop('abricots')

# print(Inventory.keys())
# print(Inventory.values())
# print(len(Inventory))

# print(Inventory.get("bananes"))
# print(Inventory.get("peches", 0))

# print(Fruits)

# for i in Inventory:
#     print(i) # Return Keys
# for i in Inventory.values():
#     print(i) # Return Values
# for x,y in Inventory.items():
#     print(x, y) # Return Keys And Values
    
# Classeur Trie Exercise

# classeur = {
#     'Positif': [],
#     'Negatif': []
# }

# def Trier(classeur, number):
#     while number > 0:
#         return classeur['Positif'].append(number)
#     return classeur['Negatif'].append(number)

# Trier(classeur, 3)
# Trier(classeur, -2)

# print(classeur)


# List / Tuple / Dict Comprehension ===================================

# List Comprehension

# list_1 = []
# for i in range(10):
#     list_1.append(i**2)
# print(list_1)

# list_2 = [i**2 for i in range(10)]
# print(list_2)

# Nested List

# list_3 = [i for i in range(3)]
# print(list_3)

# list_4 = [[i for i in range(5)] for j in range(5)]
# print(list_4)

# Dict Comprehension

# dictionnaire = {
#     '0': 'Pierre',
#     '1': 'Jean',
#     '2': 'Julie',
#     '3': 'Sophie'
# }

# prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']

# dictionnaire_2 = {x:y for x, y in enumerate(prenoms)}
# print(dictionnaire_2)

# ages = [24, 62, 10, 23]

# dictionnaire_3 = {prenom:age for prenom, age in zip(prenoms, ages)}
# print(dictionnaire_3)

# dictionnaire_4 = {prenom:age for prenom, age in zip(prenoms, ages) if age > 30}
# print(dictionnaire_3)

# dict_1 = { value1, value2 / For Boucle / Condition}

# Tuple Comprehension

# tuple_1 = tuple((i**2 for i in range(10)))
# print(tuple_1)

# Dictionary k:v Exercise

# dict_kv = {
#     str(k): k**2 for k in range(20)
# }

# print(dict_kv)

# Built-in Functions ===================================

# x = -3
# abs(x) # Return La Valeur Absolue

# x = 3.14
# round(x) # Return A Decimal

# liste_1 = [0, 2, 33, 19, 20]
# max(liste_1)
# min(liste_1)
# sum(liste_1)
# all(liste_1) # Return True If All Elements Not Equal To 0
# any(liste_1) # Return True If There Is At Least One Elements !== 0

# liste_2 = [True, False, True, True]
# all(liste_2) # Return True If All Elements Are True
# any(liste_2) # Return True If There Is At Least True Element

# list_1 = [0, 61, 40, 80, 92]
# tuple_1 = tuple(liste_1) # Transform list_1 from list type to tuple type
# list_2 = list(tuple_1) # Transform tuple_1 from tuple type to list type

# dic_1 = {
#     "bananes": 5000,
#     "pommes": 2094,
#     "poires": 412809
# }
# list_3 = list(dic_1.keys()) # Create A List Of dic_1 Dictionnary Keys
# liste_3 = list(dic_1.values()) # Create A List Of dic_1 Dictionnary Values

# bin(15) # Transform An Element To Binnary Type
# oct(15) # Transform An Element To Octet Type
# hex(15) # Transform An Element To HexaDecimal Type

# x = int(input('Enter A Number: '))
# print(x)

# x = 25
# ville = 'Marrakech'
# # Format Function Method
# message = "La Temperature est de {} deg C a {}".format(x, ville)

# # Another Method
# message = f"La Temperature est de {x} deg C a {ville}"

# print(message)

# Open() Function

# open(
    # file, mode="r", buffering=-1, encoding=None, errors=None, 
    # newline=None, closefd=True, opener=None
#   )

# Modes :
#   'r': open for reading (default)
#   'w': open for writing, truncating the file first
#   'x': open for exclisive creation, failing if the file already
#        exists
#   'a': open for writing, appending to the end of rhe file if it
#        exists
#   'b': binary mode
#   't': text mode (default)

# f = open('fichier.txt', 'w')
# f.write('Bonjour !')
# f.close()

# f = open('fichier.txt', 'r')
# f.read()

# with open('fichier.txt', 'r') as f:
#     print(f.read())

# Exercise

# with open('fichier.txt', 'w') as f:
#     for i in range(10):
#         f.write("{}^2 = {} \n".format(i, i**2))

# with open('fichier.txt', 'r') as f:
#     l = f.read()
# list_1 = l.split('\n')
# print(list_1)
