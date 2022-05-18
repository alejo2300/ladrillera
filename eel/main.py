from http import client
from itertools import product
import eel
import conectionToDb as db

eel.init("www")

#CLIENT
#Crud operations for client

#get client
@eel.expose
def readClient():
    clientsList =  db.getClients()
    eel.readClientResponse(clientsList)

#delete client
@eel.expose
def deleteClient(clientId):
    print(clientId)
    clientIdDelete = int(clientId)
    db.deleteClientById(clientIdDelete)
    
#get client by id  
@eel.expose
def getClientById(clientId):
    clientId = int(clientId)
    client = db.getClientById(clientId)
    eel.getClientByIdResponse(client)

#update client    
@eel.expose
def updateClientChanges(id, name, chanel):
    clientid = int(id)
    clientName = str(name)
    clientChanel = int(chanel)
    db.updateClient(clientid, clientName, clientChanel)

#add client    
@eel.expose
def addClient(name, channel):
    clientName = str(name)
    clientChanel = int(channel)
    db.addClient(clientName, clientChanel)
    
#PRODUCT
# Crud operations for product

#get product
@eel.expose
def readProduct():
    productList =  db.getProducts()
    eel.readProductResponse(productList)
    
#delete product
@eel.expose
def deleteProduct(productId):
    print(productId)
    productIdDelete = int(productId)
    db.deleteProductById(productIdDelete)
    
#get product by id
@eel.expose
def getProductById(productId):
    print(productId)
    productId = int(productId)
    product = db.getProductById(productId)
    eel.getProductByIdResponse(product)

#update product
@eel.expose
def updateProduct(productId, productName, productInventary, productPrecut, productCut, productDry, productOven, productCellar):
    productid = float(productId)
    productName = str(productName)
    productInventary = float(productInventary)
    productPrecut = float(productPrecut)
    productCut = float(productCut)
    productDry = float(productDry)
    productOven = float(productOven)
    productCellar = float(productCellar)
    db.updateProduct(productid, productName, productInventary, productPrecut, productCut, productDry, productOven, productCellar)
    
#add product
@eel.expose
def addProduct(name, inventary, precut, cut, dry, oven, cellar):
    productName = str(name)
    productInventary = float(inventary)
    productPrecut = float(precut)
    productCut = float(cut)
    productDry = float(dry)
    productOven = float(oven)
    productCellar = float(cellar)
    db.addProduct(productName, productInventary, productPrecut, productCut, productDry, productOven, productCellar)
  
#This line come after all expose functions  
eel.start("index.html")