from os import stat
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

def getProductByName(name):
    cursor.execute("SELECT * FROM PRODUCT WHERE NAME = ?", (name,))
    selectedProduct = cursor.fetchone()
    return selectedProduct
    
#ORDER CRUD OPERATIONS
def getOrders():
    cursor.execute("SELECT * FROM ORDERS")
    orders = cursor.fetchall()
    return orders

def deleteOrderById(orderId):
    cursor.execute("DELETE FROM ORDERS WHERE ID_ORDER = ?", (orderId,))
    sqlite3.Connection.commit(connection)
    
def addOrder(clientId, productId, quantity, date, status, deliveryTime):
    cursor.execute("INSERT INTO ORDERS (ID_CLIENT, ID_PRODUCT, MOUNT, DATE, STATUS, DELIVERY_TIME) VALUES ( ?, ?, ?, ?, ?, ?)", (clientId, productId, quantity, date, status, deliveryTime))
    sqlite3.Connection.commit(connection)

def getOrderById(orderId):
    cursor.execute("SELECT * FROM ORDERS WHERE ID_ORDER = ?", (orderId,))
    sorder = cursor.fetchone()
    return sorder

def updateOrder(orderid, clientId, productId, quantity, date, status, deliveryTime):
    cursor.execute("UPDATE ORDERS SET ID_CLIENT = ?, ID_PRODUCT = ?, MOUNT = ?, DATE = ?, STATUS = ?, DELIVERY_TIME = ? WHERE ID_ORDER = ?", (clientId, productId, quantity, date, status, deliveryTime, orderid))
    sqlite3.Connection.commit(connection)
    
    
#PROGRAMATION QUERIES
def getProgramationByPriority():
    status = "Activa"
    cursor.execute("SELECT c.name as cliente, c.chanel as prioridad, o.mount as cantidad, p.name as producto, o.delivery_time from ORDERS as o, CLIENT as c, PRODUCT as p where o.id_client=c.id_client AND p.id_product=o.id_product  and status=? ORDER by c.chanel DESC",(status,))
    programation = cursor.fetchall()
    return programation

def getProgramationByMount():
    status = "Activa"
    cursor.execute("SELECT c.name as cliente, c.chanel as prioridad, o.mount as cantidad, p.name as producto, o.delivery_time from ORDERS as o, CLIENT as c, PRODUCT as p where o.id_client=c.id_client AND p.id_product=o.id_product  and status=? ORDER by o.mount DESC",(status,))
    programation = cursor.fetchall()
    return programation

def getProgramationByPriorityMMount():
    status = "Activa"
    cursor.execute("SELECT c.name as cliente, c.chanel as prioridad, o.mount as cantidad, p.name as producto, o.delivery_time from ORDERS as o, CLIENT as c, PRODUCT as p where o.id_client=c.id_client AND p.id_product=o.id_product  and status=? ORDER by o.mount*c.chanel DESC",(status,))
    programation = cursor.fetchall()
    return programation
    
# CLOSE DATABASE

def closeDB():
    connection.close()
    
