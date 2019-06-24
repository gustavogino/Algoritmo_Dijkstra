from collections import defaultdict
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

class Grafo():
    def __init__(self):
        self.arestas = defaultdict(list)
        self.pesos = {}
    
    def adiciona_aresta(self, no_inicio, no_final, peso):
        self.arestas[no_inicio].append(no_final)
        self.arestas[no_final].append(no_inicio)
        self.pesos[(no_inicio, no_final)] = peso
        self.pesos[(no_final, no_inicio)] = peso


def Dijsktra(grafo, inicial, final):
    caminho_curto = {inicial: (None, 0)}
    no_atual = inicial
    visitado = set()
    
    while no_atual != final:
        visitado.add(no_atual)
        destinos = grafo.arestas[no_atual]
        peso_nodo_atual = caminho_curto[no_atual][1]

        for proximo_no in destinos:
            peso = grafo.pesos[(no_atual, proximo_no)] + peso_nodo_atual
            if proximo_no not in caminho_curto:
                caminho_curto[proximo_no] = (no_atual, peso)
            else:
                current_shortest_weight = caminho_curto[proximo_no][1]
                if current_shortest_weight > peso:
                    caminho_curto[proximo_no] = (no_atual, peso)
        
        proximos_destinos = {vertice: caminho_curto[vertice] for vertice in caminho_curto if vertice not in visitado}
        if not proximos_destinos:
            return "Rota impossível"
        no_atual = min(proximos_destinos, key=lambda k: proximos_destinos[k][1])
    
    caminho = []
    while no_atual is not None:
        caminho.append(no_atual)
        proximo_no = caminho_curto[no_atual][0]
        no_atual = proximo_no
        
    caminho = caminho[::-1]
    return caminho

def Combinador(vetor):
	combinacoes = []
	gera_comb = product(vetor, repeat=2)
	for combina in gera_comb:
	    combinacoes.append(combina)	    
	return combinacoes    


grafo = Grafo()

arestas = [
('V1', 'V2', 5),
('V1', 'V4', 5), 
('V1', 'V5', 9),
('V2', 'V3', 4),
('V2', 'V6', 2), 
('V2', 'V5', 9),
('V2', 'V4', 4),
('V3', 'V6', 2),
('V4', 'V5', 3), 
('V4', 'V7', 5),
('V4', 'V8', 6),
('V5', 'V7', 9), 
('V5', 'V8', 4),
('V6', 'V8', 7),
('V6', 'V9', 1),
('V7', 'V8', 6), 
('V7', 'V10', 10),
('V8', 'V9', 2),
('V8', 'V10', 3)
]

for aresta in arestas:
    grafo.adiciona_aresta(*aresta)

arestas_existentes=[
['V1', 'V2'],
['V1', 'V4'],
['V1', 'V5'],
['V2', 'V3'],
['V2', 'V6'],
['V2', 'V5'],
['V2', 'V4'],
['V3', 'V6'],
['V4', 'V5'],
['V4', 'V7'],
['V4', 'V8'],
['V5', 'V7'],
['V5', 'V8'],
['V6', 'V8'],
['V6', 'V9'],
['V7', 'V8'],
['V7', 'V10'],
['V8', 'V9'],
['V8', 'V10']
]

combinacoes=[
['V1', 'V2'],['V1', 'V3'],['V1', 'V4'],['V1', 'V5'],['V1', 'V6'],['V1', 'V7'],['V1', 'V8'],['V1', 'V9'],['V1', 'V10'],
['V2', 'V3'],['V2', 'V4'],['V2', 'V5'],['V2', 'V6'],['V2', 'V7'],['V2', 'V8'],['V2', 'V9'],['V2', 'V10'],
['V3', 'V4'],['V3', 'V5'],['V3', 'V6'],['V3', 'V7'],['V3', 'V8'],['V3', 'V9'],['V3', 'V10'],
['V4', 'V5'],['V4', 'V6'],['V4', 'V7'],['V4', 'V8'],['V4', 'V9'],['V4', 'V10'],
['V5', 'V6'],['V5', 'V7'],['V5', 'V8'],['V5', 'V9'],['V5', 'V10'],
['V6', 'V7'],['V6', 'V8'],['V6', 'V9'],['V6', 'V10'],
['V7', 'V8'],['V7', 'V9'],['V7', 'V10'],
['V8', 'V9'],['V8', 'V10'],
['V9', 'V10']
]

todos_caminhos = []

for i in range(len(combinacoes)):
	caminho = Dijsktra(grafo, combinacoes[i][0],combinacoes[i][1])  
	todos_caminhos.append(caminho)
	print("Caminho de "+combinacoes[i][0]+" para "+combinacoes[i][1]+" : ")
	print(caminho)
	print("   ")

#todos_caminhos = set(tuple(x) for x in todos_caminhos)

#plotar grafo
"""
G = nx.Graph(arestas_existentes)
nx.set_node_attributes(G,'capacity',1)

nx.draw(G)
plt.show()
"""