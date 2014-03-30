import sys

class ErrorCal:


    def __init__(self,num,epsilon):
        self.num = num
     
    def getRelativeError():
        pass
        return
        
    def getAbsoluteError():
        st = str(self.num)
        n = '%.52f' % float(st)
        pos_pto = n.find('.')
        tam = len(st)-pos_pto-1
        tam = 52-tam
        for i in range (0, tam):
            st+='0'
 
        x = "0."
        flx = "0."
        for i in range(0,len(st)):
            if(n[i]!=st[i]):
                pot = i-pos_pto-1
                x += st[i:]
                flx += n[i:]
                break
        error = '%.17f' % (float(x) - float(flx))
        return error, pot
