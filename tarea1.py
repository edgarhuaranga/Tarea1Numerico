import sys
from Tkinter import *
import tkMessageBox
import struct
from FloatsClass import FloatsClass

mGui = Tk()


def getEpsilonMachine():
    eps = float(1)
    while float(1)+ eps != float(1):
        last_eps = eps
        eps = eps/float(2)
    res = last_eps
    Label(mGui, text = res,fg='blue').place(x=200,y=65)

def getLongPalabra():
    long_palabra = struct.calcsize('P') * 8 
    texto = str(long_palabra) + ' bits'
    Label(mGui, text = texto,fg='blue').place(x=200,y=25)

def getErrorNum():
    #calcular error ,llamar objeto ErrorCal
    texto = 'Aca ira\nun mensaje complicado con\n saltos de linea'
    tkMessageBox.showinfo('Resultado', texto)

def getSetFloat():
    #Abre nueva ventana para ingresar parametros para armar conjunto de numeros
    sets = FloatsClass()
    return

def main():
    #mGui = Tk()
    mGui.geometry('450x200+200+200')
    mGui.title('Tarea 1 Calculo Numerico')
    
    mbotonLongPalabra = Button(mGui, text = 'Longitud de Palabra',command = getLongPalabra).place(x=20,y=20)
    mbotonEpsilonMachine = Button(mGui, text = 'Epsilon de Maquina',command = getEpsilonMachine).place(x=20,y=60)
    
    mynum = IntVar()
    mtextNum = Entry(mGui, textvariable = mynum).place(x=20,y=110)
    mbotonGetError = Button(mGui, text = 'Calcular error', command = getErrorNum).place(x=200, y=110)
    #print "El beta (base) es ",betha)
    
    mbotonSetnum = Button(mGui, text = 'Calcular numeros maquina', command = getSetFloat).place(x=20, y = 150)
    
    mGui.mainloop()

if __name__ == "__main__":
    main()
