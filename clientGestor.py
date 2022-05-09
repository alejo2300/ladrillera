import conectionToDb as cn
import tkinter as tk

from tkinter import *
from tkinter import ttk


def main():
    #CRUD Pop's windows
    #Add window
    def addClientWindow():
        new_window = tk.Toplevel(rootnode)
        new_window.title("Agregar cliente")
        new_window.geometry("500x250")
        tk.Label(new_window, text="Nombre:").grid(row=0, column=0)
        name = tk.Entry(new_window).grid(row=0, column=1)
        tk.Label(new_window, text="Canal:").grid(row=1, column=0)
        channel = tk.Entry(new_window).grid(row=1, column=1)
        dbname = name.get()
        dbchannel = channel.get()
        print(dbname)
        tk.Button(new_window, text="Agregar", command=lambda: cn.addClient(dbname,dbchannel)).grid(row=2, column=1)
        

    def editClientWindow(client):
        new_windowEdit = tk.Toplevel(rootnode)
        new_windowEdit.title("Editar cliente")
        new_windowEdit.geometry("500x250")
        print(client)
        
    def deleteClient(clientId):
        #cn.deleteClientById(clientId)
        print(clientId)
        
    sClient = []

    def selectedClient(a):
        global sClient
        currItem = tv.focus()
        sClient = tv.item(currItem)['values']
        print(sClient[0])
    

    rootnode = tk.Tk()
    clientList = cn.getClients()  

    #Set main screen properties
    rootnode.title("Gestor de clientes")
    width = 650
    height = 600
    rootnode.geometry("%dx%d" % (width, height))
    frm =  tk.Frame(rootnode)
    frm.pack(side=tk.LEFT, padx=20)
    #Create table for clients
    tv = ttk.Treeview(frm, columns=(1,2,3), show="headings", height=25) 
    tv.heading(1, text="Identificador")
    tv.heading(2, text="Nombre")
    tv.heading(3, text="Canal")
    tv.bind('<ButtonRelease-1>',selectedClient)
    tv.pack()

    for i in clientList:
        tv.insert('', 'end', values=(i[0], i[1], i[2]))
        
    #Create CRUD buttons
    addClient = tk.Button(frm, text="Agregar cliente", command=addClientWindow)
    editClient = tk.Button(frm, text="Editar cliente", command= lambda: editClientWindow(sClient))
    deleteClientBtn = tk.Button(frm, text="Eliminar cliente", command= lambda: deleteClient(sClient[0]) )
    addClient.pack(side=tk.RIGHT)
    editClient.pack(side=tk.RIGHT)
    deleteClientBtn.pack(side=tk.RIGHT)
        
    rootnode.resizable(False, False)
    rootnode.mainloop()
                


