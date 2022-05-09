import conectionToDb as cn
import clientGestor as cg
import tkinter as tk

print(cn.getClients())

#open Client gestor
def openClientGestor():
    cg.main()
    
#Iniciando la interfaz grafica
rootnode = tk.Tk()
#Set main screen properties
rootnode.title("Maguncia gestor")
width = rootnode.winfo_screenwidth()
height = rootnode.winfo_screenheight()
rootnode.geometry("%dx%d" % (width, height))

#create a frame para el main
frame = tk.Frame(rootnode)
frame.config(bg="white")
frame.pack()

#Buttons for go to the other screens
button_client = tk.Button(frame, text="Clientes", command=openClientGestor)
button_client.pack(side=tk.LEFT)
#button_client.pack(relx=0.5, rely=0.5, anchor='center')

rootnode.mainloop()