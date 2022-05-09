import sqlite3

connection =  sqlite3.connect('maguncia.db')

cursor = connection.cursor()

def getClients():
    cursor.execute("SELECT * FROM CLIENT")
    clients = cursor.fetchall()
    return clients

def deleteClientById(clientId):
    cursor.execute("DELETE FROM CLIENT WHERE ID = ?", (clientId,))
    cursor.commit()
    
def addClient(name, channel):
    #Get previous max value
    cursor.execute("SELECT MAX(id_client) FROM CLIENT")
    mvalue = cursor.fetchone()[0]
    cursor.execute("INSERT INTO CLIENT (NAME, CHANNEL) VALUES ( ?, ?, ?)", (mvalue, name, channel))
    cursor.commit()

def closeDB():
    connection.close()
    
