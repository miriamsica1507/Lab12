from dataclasses import dataclass

@dataclass
class Connessioni:
    id : int
    id_rifugio1 : int
    id_rifugio2 : int
    distanza : float
    difficolta : int
    durata : int
    anno : int

    def __hash__(self):
        return hash(self.id)