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
        fattori = {'facile': 1,
                   'medio' : 1.5,
                   'difficile' : 2}
        for edge in self._edges:
            if edge.anno <= year and edge.id is not None:
                fattore_difficolta = fattori.get(edge.difficolta)
                peso = edge.distanza * fattore_difficolta
                self.G.add_edge(edge.id_rifugio1, edge.id_rifugio2, weight=peso)
        return self.G

    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        # TODO


    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        # TODO

    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
