from dataclasses import dataclass

@dataclass
class Cammini:
    id_connessione : int
    id_rifugio1 : int
    id_rifugio2 : int
    distanza : float
    difficolta : str
    durata : float
    anno : int
    nome1 : str
    nome2 : str
    localita1 : str
    localita2 : str

    def __hash__(self):
        return hash(self.id_connessione)

    def __str__(self):
        return f'{self.id_rifugio1}) {self.nome1} ({self.localita1}) --> {self.id_rifugio2}) {self.nome2} ({self.localita2})'