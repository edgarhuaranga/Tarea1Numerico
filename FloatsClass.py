import sys
from Tkinter import *
import tkMessageBox
import struct

class FloatsClass:

    def __init__(self):
        #default para MARC-32
        self.betha = 2
        self.mantisa = 23
        self.expU = 2
        self.expL = -2
        self.graphics()
        
    def graphics(self):
        mGui = Tk()
        mGui.geometry('450x250+450+300')
        mGui.title('Ingrese datos para armar el conjunto')
        mlabel1 = Label(mGui, text= 'Numero betha (base)').place(x=20,y=20)  
        mbetha = Entry(mGui, textvariable = self.betha).place(x=200,y=20)
        mlabel2 = Label(mGui, text= 'Tamano mantisa (t)').place(x=20,y=60)  
        mmantisa = Entry(mGui, textvariable = self.mantisa).place(x=200,y=60)
        mlabel3 = Label(mGui, text= 'Minima potencia (L)').place(x=20,y=100)  
        mlowexp = Entry(mGui, textvariable = self.expL).place(x=200,y=100)
        mlabel4 = Label(mGui, text= 'Maxima potencia (U)').place(x=20,y=140)  
        mupexp = Entry(mGui, textvariable = self.expU).place(x=200,y=140)
        mbuton = Button(mGui, text = 'Calcular numeros',command = self.getFloats).place(x=20, y = 180)
        mbuton = Button(mGui, text = 'Calcular cantidad de numeros',command = self.getTotalSet).place(x=200, y = 180)
        #mGui.mainloop()          
       
       
    def getTotalSet(self):
        total = (self.betha -1)*(pow(self.betha, self.mantisa-1))*(self.expU - self.expL +1)
        total = total*2 +1
        tkMessageBox.showinfo('Total de elementos', 'Hay en total ' + str(total) + ' numeros maquina')
    
    def getFloats(self):
        #calcula el conjunto
        #muestra en un archivo de texto
        pass
        return
