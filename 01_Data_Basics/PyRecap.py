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
#     list = []
#     while a < n:
#         list.append(a)
#         a, b = b, a+b
#     return list
        
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