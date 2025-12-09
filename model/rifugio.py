from dataclasses import dataclass

@dataclass
class Rifugio:
    id : int
    nome : str
    localita : str
    altitudine : float
    capienza : float
    aperto : str

    def __hash__(self):
        return hash(self.id)