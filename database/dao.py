from database.DB_connect import DBConnect
from model.connessioni import Connessioni

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
