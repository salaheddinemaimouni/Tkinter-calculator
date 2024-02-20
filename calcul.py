from tkinter import *
from math import *

app = Tk()
app.title("calculatrice")
app.resizable(0,0)
app.geometry("315x250")

def checksyntax():
    if all(e=="(" or e==")" or type(e)==int or e=="+" or e=="-" or e=="/" or e=="x" or e=="." for e in char):
        pass
    else:
        return "syntaxt erreur"

def topy(char):
    lstchar=[]
    for e in char:
        lstchar.append(e)
    for e,i in zip(lstchar,range(len(lstchar))):
        if e=="x":
            lstchar[i]="*"
        if e=="^":
            lstchar[i]="**"
    return "".join(lstchar)

        
            
    
    


class Calculatrice(Frame):
    
    def __init__(self,master=None):
        calcul=""
        result=""
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        self.calcul=calcul
        self.result=result

    def createWidgets(self):
        #row0
        self.Text =  Listbox(self,font=("Arial", 20),height=2)
        self.Text["width"]=15
        self.Text.grid(row=0, column=0,columnspan=10)
        
        #row1
        self.un = Button(self)
        self.un ["text"] = "1"
        self.un ["width"] =5
        self.un ["height"] =2
        self.un ["command"] = self.unfun
        self.un.grid(row=1, column=0)

        self.deux = Button(self)
        self.deux ["text"] ="2"
        self.deux ["width"] =5
        self.deux ["height"] =2
        self.deux ["command"] = self.deuxfun
        self.deux.grid(row=1, column=1)

        self.trois = Button(self)
        self.trois ["text"] ="3"
        self.trois ["width"] =5
        self.trois ["height"] =2
        self.trois ["command"] = self.troisfun
        self.trois.grid(row=1, column=2)

        self.plus = Button(self)
        self.plus ["text"] = "+"
        self.plus ["width"] =5
        self.plus ["height"] =2
        self.plus ["command"] = self.plusfun
        self.plus.grid(row=1, column=3)

        self.power = Button(self)
        self.power ["text"] = "^"
        self.power ["width"] =5
        self.power ["height"] =2
        self.power ["command"] = self.powerfun
        self.power.grid(row=1, column=4)

        self.sinus = Button(self)
        self.sinus ["text"] = "sin"
        self.sinus ["width"] =5
        self.sinus ["height"] =2
        self.sinus ["command"] = self.sinusfun
        self.sinus.grid(row=1, column=5)

        self.tang = Button(self)
        self.tang ["text"] = "tan"
        self.tang ["width"] =5
        self.tang ["height"] =2
        self.tang ["command"] = self.tangfun
        self.tang.grid(row=1, column=6)

        #row2
        self.quatre = Button(self)
        self.quatre ["text"] ="4"
        self.quatre ["width"] =5
        self.quatre ["height"] =2
        self.quatre ["command"] = self.quatrefun
        self.quatre.grid(row=2, column=0)

        self.cinque = Button(self)
        self.cinque ["text"] ="5"
        self.cinque ["width"] =5
        self.cinque ["height"] =2
        self.cinque ["command"] = self.cinquefun
        self.cinque.grid(row=2, column=1)

        self.six = Button(self)
        self.six ["text"] ="6"
        self.six ["width"] =5
        self.six ["height"] =2
        self.six ["command"] = self.sixfun
        self.six.grid(row=2, column=2)

        self.moins = Button(self)
        self.moins ["text"] = "-"
        self.moins ["width"] =5
        self.moins ["height"] =2
        self.moins ["command"] = self.moinsfun
        self.moins.grid(row=2, column=3)

        self.square = Button(self)
        self.square ["text"] = "sqrt"
        self.square ["width"] =5
        self.square ["height"] =2
        self.square ["command"] = self.sqrtfun
        self.square.grid(row=2, column=4)

        self.cosinus = Button(self)
        self.cosinus ["text"] = "cos"
        self.cosinus ["width"] =5
        self.cosinus ["height"] =2
        self.cosinus ["command"] = self.cosinusfun
        self.cosinus.grid(row=2, column=5)

        self.pie = Button(self)
        self.pie ["text"] = "pi"
        self.pie ["width"] =5
        self.pie ["height"] =2
        self.pie ["command"] = self.piefun
        self.pie.grid(row=2, column=6)

        #row3
        self.sept = Button(self)
        self.sept ["text"] ="7"
        self.sept ["width"] =5
        self.sept ["height"] =2
        self.sept ["command"] = self.septfun
        self.sept.grid(row=3, column=0)

        self.huit = Button(self)
        self.huit ["text"] = "8"
        self.huit ["width"] =5
        self.huit ["height"] =2
        self.huit ["command"] = self.huitfun
        self.huit.grid(row=3, column=1)

        self.neuf = Button(self)
        self.neuf ["text"] ="9"
        self.neuf ["width"] =5
        self.neuf ["height"] =2
        self.neuf ["command"] = self.neuffun
        self.neuf.grid(row=3, column=2)

        self.div = Button(self)
        self.div ["text"] = "/"
        self.div ["width"] =5
        self.div ["height"] =2
        self.div ["command"] = self.divfun
        self.div.grid(row=3, column=3)

        self.open = Button(self)
        self.open ["text"] = "("
        self.open ["width"] =5
        self.open ["height"] =2
        self.open ["command"] = self.openfun
        self.open.grid(row=3, column=4)

        self.closed = Button(self)
        self.closed ["text"] = ")"
        self.closed ["width"] =5
        self.closed ["height"] =2
        self.closed ["command"] = self.closedfun
        self.closed.grid(row=3, column=5)

        #row4
        self.zero = Button(self)
        self.zero ["text"] = "0"
        self.zero ["width"] =5
        self.zero ["height"] =2
        self.zero ["command"] = self.zerofun
        self.zero.grid(row=4, column=1)

        self.mul = Button(self)
        self.mul ["text"] = "x"
        self.mul ["width"] =5
        self.mul ["height"] =2
        self.mul ["command"] = self.mulfun
        self.mul.grid(row=4, column=3)
        
        self.point = Button(self)
        self.point ["text"] = "."
        self.point ["width"] =5
        self.point ["height"] =2
        self.point ["command"] = self.pointfun
        self.point.grid(row=4, column=0)

        self.equal = Button(self)
        self.equal ["text"] = "="
        self.equal ["width"] =5
        self.equal ["height"] =2
        self.equal ["command"] = self.equalfun
        self.equal.grid(row=4, column=2)

        self.delete = Button(self)
        self.delete ["text"] = "C"
        self.delete ["width"] =5
        self.delete ["height"] =2
        self.delete ["command"] = self.deletefun
        self.delete.grid(row=4, column=4)

        self.clear = Button(self)
        self.clear ["text"] = "clear all"
        self.clear ["width"] =5
        self.clear ["height"] =2
        self.clear ["command"] = self.clearfun
        self.clear.grid(row=4, column=5)

        

        

    def unfun(self):
        self.calcul=self.calcul+"1"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)
        
    def deuxfun(self):
        self.calcul=self.calcul+"2"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def troisfun(self):
        self.calcul=self.calcul+"3"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def quatrefun(self):
        self.calcul=self.calcul+"4"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def cinquefun(self):
        self.calcul=self.calcul+"2"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def sixfun(self):
        self.calcul=self.calcul+"6"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def septfun(self):
        self.calcul=self.calcul+"7"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def huitfun(self):
        self.calcul=self.calcul+"8"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def neuffun(self):
        self.calcul=self.calcul+"9"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def zerofun(self):
        self.calcul=self.calcul+"0"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)
        
    def plusfun(self):
        self.calcul=self.calcul+"+"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def moinsfun(self):
        self.calcul=self.calcul+"-"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def divfun(self):
        self.calcul=self.calcul+"/"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def mulfun(self):
        self.calcul=self.calcul+"x"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def equalfun(self):
        try:
            self.result=eval(topy(self.calcul))
            self.Text.insert(END,self.result)
            self.calcul=""
        except SyntaxError:
            self.Text.insert(END,"SyntaxError")
            self.calcul=""
        except ZeroDivisionError:
            self.Text.insert(END,"ZeroDivisionError")
            self.calcul=""
        
    def pointfun(self):
        self.calcul=self.calcul+"."
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)
        
    def powerfun(self):
        self.calcul=self.calcul+"^"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def sqrtfun(self):
        self.calcul=self.calcul+"sqrt("
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def openfun(self):
        self.calcul=self.calcul+"("
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def closedfun(self):
        self.calcul=self.calcul+")"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)
        
    def clearfun(self):
        self.calcul=""
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def deletefun(self):
        try:
            a=list(self.calcul)
            a[-1]=""
            self.calcul="".join(a)
            self.Text.delete(0,END)
            self.Text.insert(END,self.calcul)
        except:
            self.calcul=""
            self.Text.delete(0,END)
            self.Text.insert(END,self.calcul)

    def cosinusfun(self):
        self.calcul=self.calcul+"cos("
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def sinusfun(self):
        self.calcul=self.calcul+"sin("
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def tangfun(self):
        self.calcul=self.calcul+"tan("
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)

    def piefun(self):
        self.calcul=self.calcul+"pi"
        self.Text.delete(0,END)
        self.Text.insert(END,self.calcul)
    
eval("print(1)")
        

root = Calculatrice(master=app)

root.mainloop()
