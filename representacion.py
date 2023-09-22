import matplotlib.pyplot as plt
import networkx as nx
import pydot

from insertar import *


def plot_avl_tree(root):
    G = nx.DiGraph()
    plot_tree_recursive(G, root)
    
    dot_tree = nx.nx_pydot.to_pydot(G)
    dot_tree.set_rankdir("TB")  # Orientar el árbol de arriba a abajo
    # Reducir la distancia entre los nodos (ajustar el ancho)
    
    # Guardar el árbol como una imagen
    dot_tree.write_png("avl_tree.png")
    

def plot_tree_recursive(G, node):
    if node:
        G.add_node(node, label=node.city, size=300, color="lightblue")
        if node.izquierda:
            G.add_edge(node, node.izquierda)
            plot_tree_recursive(G, node.izquierda)
        if node.derecha:
            G.add_edge(node, node.derecha)
            plot_tree_recursive(G, node.derecha)

