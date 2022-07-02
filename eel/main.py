from http import client
from itertools import permutations, product
import math
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
def updateProduct(productId, productName, productInventary, productCut, productDryNat, productDryArt, productOven, productCellar):
    productid = float(productId)
    productName = str(productName)
    productInventary = float(productInventary)
    productCut = float(productCut)
    productDryNat = float(productDryNat)
    productDryArt = float(productDryArt)
    productOven = float(productOven)
    productCellar = float(productCellar)
    db.updateProduct(productid, productName, productInventary, productCut, productDryNat, productDryArt, productOven, productCellar)
    
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
  
#ORDER
#Crud operations for order
#get order
@eel.expose
def readOrder():
    orderList =  db.getOrders()
    eel.readOrderResponse(orderList)
 
#delete order
@eel.expose
def deleteOrder(orderId):
    orderIdDelete = int(orderId)
    db.deleteOrderById(orderIdDelete)
    
#get order by id
@eel.expose
def getOrderById(orderId):
    orderId = int(orderId)
    order = db.getOrderById(orderId)
    eel.getOrderByIdResponse(order)

#update order
@eel.expose
def updateOrder(orderId, orderProductId, orderClientId, orderQuantity, orderDate, orderStatus, orderDeliveryTime):
    orderId = int(orderId)
    orderClientId = int(orderClientId)
    orderProductId = int(orderProductId)
    orderQuantity = int(orderQuantity)
    orderDate = str(orderDate)
    orderStatus = str(orderStatus)
    orderDeliveryTime = str(orderDeliveryTime)
    db.updateOrder(orderId, orderClientId, orderProductId, orderQuantity, orderDate, orderStatus, orderDeliveryTime)
    
#add order
@eel.expose
def addOrder(productId, clientId, quantity, date, status, deliveryTime):
    print(productId + clientId + quantity + date + status + deliveryTime)
    clientId = int(clientId)
    productId = int(productId)
    quantity = int(quantity)
    date = str(date)
    status = str(status)
    deliveryTime = int(deliveryTime)
    db.addOrder(clientId, productId, quantity, date, status, deliveryTime)
#This line come after all expose functions


#Programation querys
#get programation by priority
@eel.expose
def getProgramationByPriority():
    programationList = db.getProgramationByPriority()
    getProgramationduration(programationList)
    eel.getProgramationResponse(programationList)
  
@eel.expose
def getProgramationByMount():
    programationList = db.getProgramationByMount()
    getProgramationduration(programationList)
    eel.getProgramationResponse(programationList)
    
@eel.expose
def getProgramationByPriorityMMount():
    programationList = db.getProgramationByPriorityMMount()
    getProgramationduration(programationList)
    eel.getProgramationResponse(programationList)
    
@eel.expose
def getProgramationByMountDesc():
    programationList = db.getProgramationByMountDesc()
    getProgramationduration(programationList)
    eel.getProgramationResponse(programationList)

@eel.expose    
def getProgramationduration(programationList):
    programationAndWaiting = []
    processWaitingTimes = [0,0,0]
    forindex = 0
    for order in programationList:
        orderWithWaits = []
        #Saving client name
        orderWithWaits.append(order[0])
        #Saving client chanel
        orderWithWaits.append(order[1])
        #Saving order Mount
        orderWithWaits.append(order[2])
        #Saving order product name
        orderWithWaits.append(order[3])
        #Get times by products
        product = db.getProductByName(order[3])
       
        totalSingleProcessDuration = 0
        #Estimate each time process in hr
        cutCost = math.ceil((order[2]/product[3])/60)
        dryNCost = math.ceil((product[6]))
        dryACost = math.ceil((product[7]))   
        ovenCost = math.ceil((product[4]))
        #Calculate waiting time
        cutWait = 0
        ovenWait = 0
        #Exexute individual process
        
        #Cut
        cutWait = processWaitingTimes[0]
        processWaitingTimes[0] += cutCost
        totalSingleProcessDuration += cutWait + cutCost
        #Saving on list
        orderWithWaits.append(cutWait)
        orderWithWaits.append(cutCost)
        
        #Dry
        #If artificial doesnt have wait time uses that
        drySelectedType = ""
        if(totalSingleProcessDuration >= processWaitingTimes[1]):
            drySelectedType = "Artificial"
            totalSingleProcessDuration += dryACost
            processWaitingTimes[1] += dryACost
            #Saving on list
            orderWithWaits.append(drySelectedType)
            orderWithWaits.append(dryACost)
        else:
            drySelectedType = "Natural"
            totalSingleProcessDuration += dryNCost
            #Saving on list
            orderWithWaits.append(drySelectedType)
            orderWithWaits.append(dryNCost)
            
        #Oven
        ovenWait = 0
        if(forindex != 0):
            endTime = programationAndWaiting[forindex-1][10]
            if(totalSingleProcessDuration >= endTime):
                processWaitingTimes[2] = 0
            else:
                ovenWait = endTime - totalSingleProcessDuration
                processWaitingTimes[2] = ovenWait
            
        totalSingleProcessDuration += ovenWait + ovenCost
        #Save oven data on list
        orderWithWaits.append(ovenWait)
        orderWithWaits.append(ovenCost)
        
        #Save all cost on list
        orderWithWaits.append(totalSingleProcessDuration)
        
        #Save list into general list
        programationAndWaiting.append(orderWithWaits)
        forindex += 1
    
    eel.productionSolve(programationAndWaiting)
    
    

        
    
    
eel.start("index.html")