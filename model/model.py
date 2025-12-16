import copy

import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        # TODO
        self.G = nx.Graph()
        self._nodes = None
        self._edges = None
        self._rifugi = None
        self._idMap = {}
        self._soluzioneMigliore = []
        self._pesoMigliore = 0

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        # TODO
        self.G.clear()
        self._edges = DAO.get_cammini()
        fattori = {'facile': 1, 'media' : 1.5, 'difficile' : 2}
        for edge in self._edges:
            if edge.anno <= year and edge.difficolta in fattori:
                fattore_difficolta = float(fattori[edge.difficolta])
                peso = float(edge.distanza) * fattore_difficolta
                self.G.add_edge(edge.id_rifugio1, edge.id_rifugio2, weight=peso)

    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        # TODO
        weights = list(nx.get_edge_attributes(self.G, 'weight').values())
        weights = [float(w) for w in weights]
        return min(weights), max(weights)


    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        # TODO
        minori = 0
        maggiori = 0
        weights = list(nx.get_edge_attributes(self.G, 'weight').values())
        weights = [float(w) for w in weights]
        for w in weights:
            if soglia > w :
                minori += 1
            if soglia < w :
                maggiori += 1
        return minori, maggiori

    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
    def cammino_minimo(self, S):
        self._soluzioneMigliore = []
        self._pesoMigliore = float("inf")

        for v in self.G.nodes():
            self._dfs([v], 0, S)

        if self._pesoMigliore == float("inf"):
            return [], 0

        return self._soluzioneMigliore, self._pesoMigliore

    def _dfs(self, parziale, peso_attuale, S):
        if len(parziale) >= 3:
            if peso_attuale < self._pesoMigliore:
                self._pesoMigliore = peso_attuale
                self._soluzioneMigliore = parziale.copy()
                return
        for v in self.G.neighbors(parziale[-1]):
            if v not in parziale:
                peso_arco = self.G[parziale[-1]][v]['weight']
                if peso_arco > S:
                    if peso_attuale + peso_arco < self._pesoMigliore:
                        parziale.append(v)
                        self._dfs(parziale, peso_attuale + peso_arco, S)
                        parziale.pop()

    @property
    def idMap(self):
        self._rifugi = DAO.get_rifugi()
        self._idMap = {rif.id: rif for rif in self._rifugi}
        return self._idMap


