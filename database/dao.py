from database.DB_connect import DBConnect
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