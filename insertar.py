from data import database
from arbol import *

# Insertar un elemento en el árbol

arbol = ArbolAVL()

for i in range(len(database)):
    arbol.insertar(database[i])