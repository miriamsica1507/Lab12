from database.DB_connect import DBConnect
from model.cammini import Cammini
from model.connessioni import Connessioni
from model.rifugio import Rifugio


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def get_connessioni():
        connessioni = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "select * from connessione"
        cursor.execute(query)
        for row in cursor:
            connessioni.append(Connessioni(**row))
        return connessioni

    @staticmethod
    def get_rifugi():
        rifugi = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "select * from rifugio"
        cursor.execute(query)
        for row in cursor:
            rifugi.append(Rifugio(**row))
        return rifugi

    @staticmethod
    def get_cammini():
        cammini = []
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = (
        'select c.id as id_connessione, c.id_rifugio1, c.id_rifugio2, '
        'c.distanza, c.difficolta, c.durata, c.anno, '
        'r1.nome as nome1, r2.nome as nome2, '
        'r1.localita as localita1, r2.localita as localita2 '
        'from rifugio r1, rifugio r2, connessione c '
        'where c.id_rifugio1 = r1.id AND c.id_rifugio2 = r2.id'
)
        cursor.execute(query)
        for row in cursor:
            cammini.append(Cammini(**row))
        cursor.close()
        conn.close()
        return cammini