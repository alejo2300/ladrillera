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
  
  
#This line come after all expose functions  
eel.start("index.html")