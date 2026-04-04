import numpy as np

# # Array et dimensions

# A = np.array([1, 2, 3])
# # print(A.ndim) # Return number of dimentions
# # print(A.shape) # Return Form

# B = np.zeros((3, 2)) # Tuple avec 3 ligne et 2 column contient des 0
# # print(B)

# B = np.ones((3, 2)) # Tuple avec 3 ligne et 2 column contient des 1

# D = np.full((2, 3), 9) # Tuple avec 2 ligne et 3 column contient des 9

# E = np.random.randn(3, 4) # Tuple avec 3 ligne et 4 column contient des nombres aleatoire 
# # print(E)

# F = np.eye(4) # Return Une Matrice D'Identitè

# G = np.linspace(0, 10, 20) # Permet de creer un tableaux a une dimention ou en precise un point de debut, un point de fin et une quantiter d'elements
# # print(G)

# H = np.arange(0, 10, 2) # entre un point debut et fin avec un pas
# # print(H)

# I = np.array([
#     [1, 2], 
#     [3, 4], 
#     [5, 6]]
# ) # Objects Arrays a deux dimensions

# J = np.array(
#     [[[1, 2], [2, 3]], [[4, 5], [5, 6]]]
# ) # Objects Arrays a trois dimensions
# # print(J)

# .ndim Renvoie le nombre de dimensions de l'array 
# print(I.ndim) # Return 2 Dimensions
# print(J.ndim) # Return 3 Dimensions

# .shape Renvoie les dimensions sous forme d'un tuple
# print(I.shape) # Return (3, 2) 3 -> nb de ligne, 2 -> nb de column
# print(J.shape) # Return (2, 2, 2) 2 -> nb de matrice, 2 -> nb de lignes, 2 -> nb de column

# Redimensionnement d’array

# .reshape() Renvoie un nouveau array avec les dimensions specifiees en arguments:
a = np.arange(0, 6)
# print(a)
# print(a.shape)
# b = a.reshape((2, 3))
# print(b)
# print(b.shape) # Return (2, 3)
# d = a.reshape((3, 4))
# print(d) # Error: Si les nouvelles dimensions ne sont pas compatibles avec les dimensions initiales, la méthode .reshape() génère une erreur.

# .resize() par contre, ne declenche pas d'erreur dans telle situation et ajoute des 0
a.resize((3, 3), refcheck=False)
print(a)
print(a.shape)
