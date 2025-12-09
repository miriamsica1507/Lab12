import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        # TODO
        self.G = nx.Graph()
        self._nodes = None
        self._edges = None

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        # TODO
        self.G.clear()
        self._edges = DAO.get_connessioni()
        fattori = {'facile': 1, 'medio' : 1.5, 'difficile' : 2}
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
            if soglia > w > min(weights):
                minori += 1
            if soglia < w < max(weights):
                maggiori += 1
        return minori, maggiori

    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
    def cammino_minimo(self, soglia):
        miglior_cammino = self._ricorsione(soglia, [], 0)

    def _ricorsione(self, soglia, parziale, minimo_peso):
        if len(parziale)>=2:
            miglior_cammino = parziale.copy()
            minimo_peso = 0

