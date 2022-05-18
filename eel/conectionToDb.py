import sqlite3

connection =  sqlite3.connect('maguncia.db')

cursor = connection.cursor()

# CLIENTS CRUD OPERATIONS

def getClients():
    cursor.execute("SELECT * FROM CLIENT")
    clients = cursor.fetchall()
    return clients

def deleteClientById(clientId):
    cursor.execute("DELETE FROM CLIENT WHERE ID_CLIENT = ?", (clientId,))
    sqlite3.Connection.commit(connection)
    
def addClient(name, channel):
    cursor.execute("INSERT INTO CLIENT (NAME, CHANEL) VALUES ( ?, ?)", (name, channel))
    sqlite3.Connection.commit(connection)
    
def getClientById(clientId):
    cursor.execute("SELECT * FROM CLIENT WHERE ID_CLIENT = ?", (clientId,))
    client = cursor.fetchone()
    return client

def updateClient(clientid, clientName, clientChanel):
    cursor.execute("UPDATE CLIENT SET NAME = ?, CHANEL = ? WHERE ID_CLIENT = ?", (clientName, clientChanel, clientid))
    sqlite3.Connection.commit(connection)
    
# PRODUCTS CRUD OPERATIONS
def getProducts():
    cursor.execute("SELECT * FROM PRODUCT")
    products = cursor.fetchall()
    return products

def deleteProductById(productId):
    cursor.execute("DELETE FROM PRODUCT WHERE ID_PRODUCT = ?", (productId,))
    sqlite3.Connection.commit(connection)

def addProduct(name,inventary,precut,cut,dry,oven,cellar):
    cursor.execute("INSERT INTO PRODUCT (NAME, INVENTARY, PRECUT, CUT, DRY, OVEN, CELLAR) VALUES ( ?, ?, ?, ?, ?, ?, ?)", (name, inventary, precut, cut, dry, oven, cellar))
    sqlite3.Connection.commit(connection)

def getProductById(productId):
    cursor.execute("SELECT * FROM PRODUCT WHERE ID_PRODUCT = ?", (productId,))
    sproduct = cursor.fetchone()
    return sproduct

def updateProduct(productid, productName, productInventary, productPrecut, productCut, productDry, productOven, productCellar):
    cursor.execute("UPDATE PRODUCT SET NAME = ?, INVENTARY = ?, PRECUT = ?, CUT = ?, DRY = ?, OVEN = ?, CELLAR = ? WHERE ID_PRODUCT = ?", (productName, productInventary, productPrecut, productCut, productDry, productOven, productCellar, productid))
    sqlite3.Connection.commit(connection)
    
# CLOSE DATABASE

def closeDB():
    connection.close()
    
