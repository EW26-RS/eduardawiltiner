
# coding: utf-8

# In[ ]:


from tkinter import *
import serial
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import csv
import numpy as np
import time
from datetime import datetime
import keyboard
import fbs_runtime
import fbs_runtime._frozen                                  
import webbrowser                                                  
import tkinter as tk                                                                                  
import numpy as np
import webbrowser
from tkinter import filedialog
import numpy.random.common                                                                               
import numpy.random.bounded_integers
import numpy.random.entropy


   
janela = tk.Tk()                                                        
janela.title('LEDTR')                        
janela.configure(bg = 'alice blue')                                    
janela.geometry("950x520")                                            
janela.focus_set()                                                                            
janela.resizable(0, 0)

       
Frame1 = tk.Frame(janela , bd = 60, bg = '#B0C4DE', width = 500, height= 550)  
Frame1.pack()
       

text1f1 = tk.Label(Frame1, text = 'Leitura de dados em tempo real', width=40, bg = '#B0C4DE',fg = 'black', font = ("Verdana","11","bold"))  
text1f1.pack()

text18f1 = tk.Label(Frame1, text = 'Taxa de transferência (bps) :',bg = '#B0C4DE',fg = 'black')    
text18f1.pack()

text4f1 = tk.Label(Frame1, text = 'Porta USB (ex:COM7) :',bg = '#B0C4DE',fg = 'black')    
text4f1.pack()

text17f1 = tk.Label(Frame1, text = 'Com :',bg = '#B0C4DE',fg = 'black')    
text17f1.pack()

text9f1 = tk.Label(Frame1, text = 'Título do gráfico :', bg = '#B0C4DE',fg = 'black')    
text9f1.pack()

text10f1 = tk.Label(Frame1, text = 'Eixo X :', bg = '#B0C4DE',fg = 'black')    
text10f1.pack()

text11f1 = tk.Label(Frame1, text = 'Eixo Y1, Y2, Y3... :', bg = '#B0C4DE',fg = 'black')
text11f1.pack()

text6f1 = tk.Label(Frame1, text = 'Especificação da porta USB :', bg = '#B0C4DE',fg = 'black', font = ("Verdana","10","bold"))  
text6f1.pack()

text7f1 = tk.Label(Frame1, text = 'Características do gráfico :', bg = '#B0C4DE',fg = 'black', font = ("Verdana","10","bold"))        
text7f1.pack()



text14f1 = tk.Label(Frame1, text = 'Tempo entre as medições (s) :',  bg = '#B0C4DE',fg = 'black')          
text14f1.pack()

text15f1 = tk.Label(Frame1, text = 'Plotar : (máx: 2curvas/gráfico)',  bg = '#B0C4DE',fg = 'black')          
text15f1.pack()
       
input1 = tk.StringVar()    
input3 = tk.StringVar()    
input4 = tk.IntVar()      
input6 = tk.StringVar()
input7 = tk.StringVar()
input8 = tk.StringVar()


       
Frame4 = tk.Frame(janela,bd = 50, width= 570, height = 80, bg = '#050951')
Frame4.pack()
       
text2f4 = tk.Label(Frame4, text = 'Lendo dados da porta USB...', width=40, bg = '#050951',fg = 'white', font = ("Verdana","11","bold"))  # Título do Frame4
text2f4.pack()

v = tk.IntVar()

F=Radiobutton(Frame1, text='Fundo Preto', variable=v, value=1,activeforeground='white',activebackground= 'black')
T=Radiobutton(Frame1, text='Fundo Branco', variable=v, value=2,activeforeground='black',activebackground= 'white')


F.pack()
T.pack()
variable = tk.StringVar()
variable.set("Uma curva")

e = OptionMenu(Frame1, variable, "Uma curva", "Duas curvas","Três curvas", "Quatro curvas", "Cinco curvas", "Seis curvas", "Sete curvas", "Oito curvas")
e.pack()

variable1 = tk.StringVar()
variable1.set("Um gráfico")

r = OptionMenu(Frame1, variable1, "Um gráfico", "Dois gráficos","Três gráficos","Quatro gráficos")
r.pack()

c = Spinbox(Frame1, from_ =1, to = 60, increment=0.5)
c.pack()

def ajuda():
    webbrowser.open('https://drive.google.com/open?id=1QUQvZ9A92PDerLRtQ9v4GAcqWdoChJ0i') 

class A:
   
       
    def ajuste(self):
       
        if self.r == 'Um gráfico':
           
            if self.e == 'Duas curvas':
             
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
       
        if self.r == 'Dois gráficos':
           
            if self.e == 'Três curvas':
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
               
            if self.e == 'Quatro curvas':
               
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
               
        if self.r == 'Três gráficos':
           
            if self.e == 'Quatro curvas':
         
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
               
            if self.e == 'Cinco curvas':
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                       
            if self.e == 'Seis curvas':
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p6.setGeometry (self.p5.vb.sceneBoundingRect ())
                self.p6.linkedViewChanged (self.p5.vb, self.p6.XAxis)
           
        if self.r == 'Quatro gráficos':
           
            if self.e == 'Cinco curvas':
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
               
            if self.e == 'Seis curvas':
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
               
            if self.e == 'Sete curvas':
               
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p6.setGeometry (self.p5.vb.sceneBoundingRect ())
                self.p6.linkedViewChanged (self.p5.vb, self.p6.XAxis)
               
            if self.e == 'Oito curvas':
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)  
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p6.setGeometry (self.p5.vb.sceneBoundingRect ())
                self.p6.linkedViewChanged (self.p5.vb, self.p6.XAxis)
                self.p8.setGeometry (self.p7.vb.sceneBoundingRect ())
                self.p8.linkedViewChanged (self.p7.vb, self.p8.XAxis)
               
       
    def parar(self):
       
        try:
            self.novodado = self.arduino.readline().decode('utf-8')
            self.arduino.close()
           
       
        except:
            root = tk.Tk()
            root.title('Aviso')  
            w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: Não há leitura de dados!' , padx=20, pady=20, bg='black', fg='red')
            w.pack()
            root.mainloop()
    def arm(self):
       
        try:
            self.arq.close()
        except:
            root = tk.Tk()
            root.title('Aviso')  
            w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: Não há arquivo para armazenar!' , padx=20, pady=20, bg='black', fg='red')
            w.pac
            root.mainloop()
   
    
    def continuar (self):
       
        try:
           
            self.arduino = serial.Serial('%s'%self.p,'%d'%self.f,timeout=3)
            print('Conectando-se novamente...')
            if self.r == 'Um gráfico':
       
                if self.e == 'Duas curvas':
             
                    self.update_label2()
           
                if self.e == 'Uma curva':
               
                    self.update_label1()
       
            if self.r == 'Dois gráficos':
           
                if self.e == 'Duas curvas':
               
                    self.update_label4()
           
                if self.e == 'Três curvas':
           
                    self.update_label3()
               
                if self.e == 'Quatro curvas':
               
                    self.update_label5()
           
            if self.r == 'Três gráficos':
           
                if self.e == 'Três curvas':
           
                    self.update_label6()
           
                if self.e == 'Quatro curvas':
         
                    self.update_label7()
               
                if self.e == 'Cinco curvas':
           
                    self.update_label8()
               
                if self.e == 'Seis curvas':
           
                    self.update_label9()
           
            if self.r == 'Quatro gráficos':
           
                if self.e == 'Quatro curvas':
         
                    self.update_label10()
           
                if self.e == 'Cinco curvas':
           
                    self.update_label11()
               
                if self.e == 'Seis curvas':
           
                    self.update_label12()
               
                if self.e == 'Sete curvas':
               
                    self.update_label13()
               
                if self.e == 'Oito curvas':
           
                    self.update_label14()
       
        except:
            print('Não há leitura de dados...')
   
               
   

    def __init__(self):
       
        self.v= v.get()
        self.w= c.get()
        self.e= variable.get()
        self.r= variable1.get()
        self.nome= input7.get()
        self.eixox = input8.get()
       
        self.eixoy= input1.get()
        self.eixoy0 = self.eixoy.split(',')
       
        self.eixoy1 = ''      
        self.eixoy2 = ''
        self.eixoy3 = ''
        self.eixoy4 = ''
        self.eixoy5 = ''
        self.eixoy6 = ''
        self.eixoy7 = ''
        self.eixoy8 = ''
           
       
        try:
           
            self.eixoy1 = self.eixoy0[0]      
            self.eixoy2 = self.eixoy0[1]
            self.eixoy3 = self.eixoy0[2]
            self.eixoy4 = self.eixoy0[3]
            self.eixoy5 = self.eixoy0[4]
            self.eixoy6 = self.eixoy0[5]
            self.eixoy7 = self.eixoy0[6]
            self.eixoy8 = self.eixoy0[7]
           
        except IndexError:

            print('Caracterização dos eixos...')
           
        self.d = input6.get()
     
       
        if self.v == 2:
       
            pg.setConfigOption('background', 'w')
            pg.setConfigOption('foreground', 'k')
            self.ponto1 ='r'
            self.ponto2 ='y'
            self.ponto3 ='b'
            self.ponto4 ='g'
            self.ponto5 ='#f56811'
            self.ponto6 ='#d6112b'
            self.ponto7 ='#7f98f0'
            self.ponto8 ='#9111d6'
            print('Fundo branco')
           
        if self.v == 1 or self.v ==0:
       
            pg.setConfigOption('background', 'k')
            pg.setConfigOption('foreground', 'w')
            self.ponto1 ='r'
            self.ponto2 ='y'
            self.ponto3 ='b'
            self.ponto4 ='g'
            self.ponto5 ='#f56811'
            self.ponto6 ='#d6112b'
            self.ponto7 ='#7f98f0'
            self.ponto8 ='#9111d6'  
            print('Fundo preto')  
           
        self.p= input3.get()
        self.f= input4.get()
   
        if self.f == 0:
            
            root = tk.Tk(); 
            root.title('Aviso')  
            n = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: Taxa de transferência e/ou porta USB incorreta!' , padx=20, pady=20, bg='black', fg='red')
            n.pack()
            self.arduino.close()
            root.mainloop()
         
        try:
            self.arduino = serial.Serial('%s'%self.p,'%d'%self.f,timeout=float(self.w)+1) 
            self.novodado = self.arduino.readline().decode('utf-8').strip()
            print('Conectando-se a porta serial...')
        except:
            try:
                self.arduino = serial.Serial('%s'%self.p,'%d'%self.f,timeout=float(self.w)+1) 
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                print('Conectando-se a porta serial...')
            except:
                try:
                    self.arduino.close()
                    root = tk.Tk();
                    root.title('Aviso')  
                    n = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: Taxa de transferência incorreta!' , padx=20, pady=20, bg='black', fg='red')
                    n.pack()
                    self.arduino.close()
                    root.mainloop()
                   
                   
                except:
                    root = tk.Tk()
                    root.title('Aviso')    
                    w = tk.Label(root, wraplength= 200,width=30, height = 7,text='ATENÇÃO: Cheque se a leitura atual do monitor serial foi interropinda (pressione parar) ou se o cabo USB está bem conectado ao computador. Também, pode ser que a configuração da porta USB esteja incorreta!', padx=20, pady=20, bg='black', fg='red')
                    w.pack()
                    self.arduino.close()
                    root.mainloop()  


            
       
        try:
            self.arq = tk.filedialog.asksaveasfile(defaultextension=".csv",mode='w',filetypes = (("csv","*.csv"),("","*.csv")))
        except PermissionError:
            root = tk.Tk() 
            root.title('Aviso')    
            w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: Cheque se arquivo que deseja substituir não está aberto!', padx=20, pady=20, bg='black', fg='red') 
            w.pack()  
            self.arduino.close()
            root.mainloop()

        
        self.Frame3 = tk.Frame(janela,bd = 20, bg = 'alice blue', width= 500, height = 400)  # Criação do Frame3, região onde o gráfico de f(x) é plotado
        self.Frame3.pack(side='left')    
        self.Frame3.place(relx=.54, rely =.16)
        self.Bu1f3 = tk.Button(janela, text = 'Parar', command = self.parar, fg = 'black' ,bg = 'white')
        self.Bu1f3.pack()
        self.Bu1f3.place(relx = .89, rely = 0.91)
        self.Bu2f3 = tk.Button(janela, text = 'Continuar', command = self.continuar, fg = 'black' ,bg = 'white')
        self.Bu2f3.pack()
        self.Bu2f3.place(relx = .783, rely = 0.91)
        self.Bu3f3 = tk.Button(janela, text = 'Ajustar', command = self.ajuste, fg = 'black' ,bg = 'white')
        self.Bu3f3.pack()
        self.Bu3f3.place(relx = .69, rely = 0.91)
        self.Bu4f3 = tk.Button(janela, text = 'Armazenar', command = self.arm, fg = 'black' ,bg = 'white') 
        self.Bu4f3.pack()
        self.Bu4f3.place(relx = .567, rely = 0.91)
           
        self.scrollbar = Scrollbar(self.Frame3,orient=HORIZONTAL)  
        self.scrollbar.pack(side=BOTTOM, fill=X)  
        self.scrollbar1 = Scrollbar(self.Frame3,orient=VERTICAL)
        self.scrollbar1.pack(side=RIGHT, fill=Y)  
        self.listbox = Listbox(self.Frame3)
        self.listbox.pack(fill = BOTH)
        self.scrollbar1.config(command=self.listbox.yview)
        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(width= 46, height = 19,xscrollcommand=self.scrollbar.set,yscrollcommand=self.scrollbar1.set)
       
        self.a =  datetime.now()
       
        self.tempo=0  
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title="Gráfico")

       
        self.count = 0
        self.dataC = []
        self.dataX = []
        self.dataY1 = []
        self.dataY2 = []
        self.dataY3 = []
        self.dataY4 = []
        self.dataY5 = []
        self.dataY6 = []
        self.dataY7 = []
        self.dataY8 = []
        self.dataY0 = []
       
       
        if self.r == 'Um gráfico':
            if self.e == 'Três curvas' or self.e == 'Cinco curvas' or self.e == 'Quatro curvas' or self.e == 'Seis curvas' or self.e == 'Sete curvas' or self.e == 'Oito curvas':
                root = tk.Tk()
                root.title('Aviso')  
                w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: O número de curvas não corresponde ao número de gráficos ou vice-versa!' , padx=20, pady=20, bg='black', fg='red')
                w.pack()
                self.arduino.close()
                root.mainloop()
            if self.e == 'Duas curvas':
                self.p1 = self.win.addPlot(title="%s" %self.nome)
           
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
               
               
                self.p1.setLabel ( 'left' , "%s" %self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s" %self.eixoy2)
                self.p1.setLabel ( 'bottom' , "%s" %self.eixox)
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
       
                self.update_label2()
           
            if self.e == 'Uma curva':
               
                self.p1 = self.win.addPlot(title="%s" %self.nome)
               
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50, name= "    %s"%self.eixoy1)    
               
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'bottom' , "%s"%self.eixox)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
       
                self.update_label1()
       
       
        if self.r == 'Dois gráficos':
            if self.e == 'Uma curva' or self.e == 'Cinco curvas' or self.e == 'Seis curvas' or self.e == 'Sete curvas' or self.e == 'Oito curvas':
                root = tk.Tk()
                root.title('Aviso')  
                w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: O número de curvas não corresponde ao número de gráficos ou vice-versa!' , padx=20, pady=20, bg='black', fg='red')
                w.pack()
                self.arduino.close()
                root.mainloop()
       
            if self.e == 'Duas curvas':
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
               
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50,  name="%s"%self.eixoy1)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50,  name ="%s"%self.eixoy2)
       
                self.p3.setLabel ( 'left' , "%s"%self.eixoy2)
                self.p3.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy2)
       
                self.update_label4()
           
            if self.e == 'Três curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
                self.p3 = self.win.addPlot(row=2, col=0)
               
                '''
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                '''
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
               
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy3)
       
                self.update_label3()
               
            if self.e == 'Quatro curvas':
               
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
     
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
       
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'right' , "%s"%self.eixoy4)
                self.p3.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
             
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
                self.p4 = pg.ViewBox ()
                self.p3.showAxis ('right')
                self.p3.scene (). addItem (self.p4)
                self.p3.getAxis ('right'). linkToView (self.p4)
                self.p4.setXLink (self.p3)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy3)
       
                self.update_label5()
           
        if self.r == 'Três gráficos':
            if self.e == 'Duas curvas'  or self.e == 'Uma curva'  or self.e == 'Sete curvas' or self.e == 'Oito curvas':
                self.arduino.close()
                root = tk.Tk()
                root.title('Aviso')  
                w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: O número de curvas não corresponde ao número de gráficos ou vice-versa!' , padx=20, pady=20, bg='black', fg='red')
                w.pack()
                root.mainloop()
           
            if self.e == 'Três curvas':
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
                self.p2 = self.win.addPlot(row=2, col=0)
                self.p3 = self.win.addPlot(row=3, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
     
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
                self.curva2 = self.p2.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
     
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p2.setLabel ( 'left' , "%s"%self.eixoy2)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
               
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p2.graphicsItem())
                self.legend1.addItem(self.curva2,'   %s' %self.eixoy2)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p3.graphicsItem())
                self.legend2.addItem(self.curva3,'   %s' %self.eixoy3)
       
                self.update_label6()
           
            if self.e == 'Quatro curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
       
                self.p4 = self.win.addPlot(row=3, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
     
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva4 = self.p4.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
       
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p4.setLabel ( 'left' , "%s"%self.eixoy4)
                self.p4.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p4.graphicsItem())
                self.legend2.addItem(self.curva4,'   %s' %self.eixoy4)
               
                self.update_label7()
               
            if self.e == 'Cinco curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
                self.p5 = self.win.addPlot(row=3, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
       
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva5 = self.p5.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
       
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'right' , "%s"%self.eixoy4)
                self.p5.setLabel ( 'left' , "%s"%self.eixoy5)
                self.p5.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
                self.p4 = pg.ViewBox ()
                self.p3.showAxis ('right')
                self.p3.scene (). addItem (self.p4)
                self.p3.getAxis ('right'). linkToView (self.p4)
                self.p4.setXLink (self.p3)
               
                self.legend = pg.LegendItem(None, (60,27))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p5.graphicsItem())
                self.legend2.addItem(self.curva5,'   %s' %self.eixoy5)
                self.update_label8()
               
            if self.e == 'Seis curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
                self.p5 = self.win.addPlot(row=3, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
       
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva5 = self.p5.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
       
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'right' , "%s"%self.eixoy4)
                self.p5.setLabel ( 'left' , "%s"%self.eixoy5)
                self.p5.setLabel ( 'right' , "%s"%self.eixoy6)
                self.p5.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
                self.p4 = pg.ViewBox ()
                self.p3.showAxis ('right')
                self.p3.scene (). addItem (self.p4)
                self.p3.getAxis ('right'). linkToView (self.p4)
                self.p4.setXLink (self.p3)
                self.p6 = pg.ViewBox ()
                self.p5.showAxis ('right')
                self.p5.scene (). addItem (self.p6)
                self.p5.getAxis ('right'). linkToView (self.p6)
                self.p6.setXLink (self.p5)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p5.graphicsItem())
                self.legend2.addItem(self.curva5,'   %s' %self.eixoy5)
                self.update_label9()
           
        if self.r == 'Quatro gráficos':
            if self.e == 'Uma curva' or self.e == 'Duas curvas' or self.e == 'Três curvas':
                root = tk.Tk()
                root.title('Aviso')  
                w = tk.Label(root, wraplength= 170,width=29, height = 6,text='ATENÇÃO: O número de curvas não corresponde ao número de gráficos ou vice-versa!' , padx=20, pady=20, bg='black', fg='red')
                w.pack()
                self.arduino.close()
                root.mainloop()
           
            if self.e == 'Quatro curvas':
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p2 = self.win.addPlot(row=2, col=0)
                self.p3 = self.win.addPlot(row=3, col=0)
                self.p4 = self.win.addPlot(row=4, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
                qGraphicsGridLayout.setRowPreferredHeight(4,295)

                self.curva4 = self.p4.plot(symbol= 'o',symbolBrush='%s' %self.ponto7, width=50)
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
                self.curva2 = self.p2.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
     
               
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p4.setLabel ( 'left' , "%s"%self.eixoy4)
                self.p4.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p2.setLabel ( 'left' , "%s"%self.eixoy2)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
               
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p2.graphicsItem())
                self.legend1.addItem(self.curva2,'   %s' %self.eixoy2)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p3.graphicsItem())
                self.legend2.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend3 = pg.LegendItem(None, (60,1))
                self.legend3.setParentItem(self.p4.graphicsItem())
                self.legend3.addItem(self.curva4,'   %s' %self.eixoy4)
               
                self.update_label10()
           
            if self.e == 'Cinco curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
       
                self.p4 = self.win.addPlot(row=3, col=0)
       
                self.p5 = self.win.addPlot(row=4, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
                qGraphicsGridLayout.setRowPreferredHeight(4,295)
               
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva4 = self.p4.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
                self.curva5 = self.p5.plot(symbol= 'o',symbolBrush='%s' %self.ponto7, width=50)

       
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p4.setLabel ( 'left' , "%s"%self.eixoy4)
                self.p5.setLabel ( 'left' , "%s"%self.eixoy5)
                self.p5.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p3.graphicsItem())
                self.legend1.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p5.graphicsItem())
                self.legend2.addItem(self.curva5,'   %s' %self.eixoy5)
                self.legend3 = pg.LegendItem(None, (60,1))
                self.legend3.setParentItem(self.p4.graphicsItem())
                self.legend3.addItem(self.curva4,'   %s' %self.eixoy4)
               
                self.update_label11()
               
            if self.e == 'Seis curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
       
                self.p3 = self.win.addPlot(row=2, col=0)
                self.p5 = self.win.addPlot(row=3, col=0)
                self.p6 = self.win.addPlot(row=4, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
                qGraphicsGridLayout.setRowPreferredHeight(4,295)
       
     
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva5 = self.p5.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
                self.curva6 = self.p6.plot(symbol= 'o',symbolBrush='%s' %self.ponto7, width=50)

                self.p6.setLabel ( 'left' , "%s"%self.eixoy6)
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'right' , "%s"%self.eixoy4)
                self.p5.setLabel ( 'left' , "%s"%self.eixoy5)
                self.p6.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
                self.p4 = pg.ViewBox ()
                self.p3.showAxis ('right')
                self.p3.scene (). addItem (self.p4)
                self.p3.getAxis ('right'). linkToView (self.p4)
                self.p4.setXLink (self.p3)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend1 = pg.LegendItem(None, (60,1))
                self.legend1.setParentItem(self.p5.graphicsItem())
                self.legend1.addItem(self.curva5,'   %s' %self.eixoy5)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p3.graphicsItem())
                self.legend2.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend3 = pg.LegendItem(None, (60,1))
                self.legend3.setParentItem(self.p6.graphicsItem())
                self.legend3.addItem(self.curva6,'   %s' %self.eixoy6)
               
                self.update_label12()
               
            if self.e == 'Sete curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
                self.p3 = self.win.addPlot(row=2, col=0)
                self.p5 = self.win.addPlot(row=3, col=0)
                self.p7 = self.win.addPlot(row=4, col=0)
       
                qGraphicsGridLayout = self.win.ci.layout
                qGraphicsGridLayout.setRowPreferredHeight(1,300)
                qGraphicsGridLayout.setRowPreferredHeight(2,295)
                qGraphicsGridLayout.setRowPreferredHeight(3,295)
                qGraphicsGridLayout.setRowPreferredHeight(4,295)

     
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva5 = self.p5.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
                self.curva7 = self.p7.plot(symbol= 'o',symbolBrush='%s' %self.ponto7, width=50)
     
                self.p7.setLabel ( 'left' , "%s"%self.eixoy7)
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'right' , "%s"%self.eixoy4)
                self.p5.setLabel ( 'left' , "%s"%self.eixoy5)
                self.p5.setLabel ( 'right' , "%s"%self.eixoy6)
                self.p7.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
               
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
                self.p4 = pg.ViewBox ()
                self.p3.showAxis ('right')
                self.p3.scene (). addItem (self.p4)
                self.p3.getAxis ('right'). linkToView (self.p4)
                self.p4.setXLink (self.p3)
                self.p6 = pg.ViewBox ()
                self.p5.showAxis ('right')
                self.p5.scene (). addItem (self.p6)
                self.p5.getAxis ('right'). linkToView (self.p6)
                self.p6.setXLink (self.p5)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p3.graphicsItem())
                self.legend2.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend3 = pg.LegendItem(None, (60,1))
                self.legend3.setParentItem(self.p5.graphicsItem())
                self.legend3.addItem(self.curva5,'   %s' %self.eixoy5)
                self.legend4 = pg.LegendItem(None, (60,1))
                self.legend4.setParentItem(self.p7.graphicsItem())
                self.legend4.addItem(self.curva7,'   %s' %self.eixoy7)
               
               
                self.update_label13()
               
            if self.e == 'Oito curvas':
           
                self.p1 = self.win.addPlot(row=1, col=0,title="%s" %self.nome)
                self.p3 = self.win.addPlot(row=2, col=0)
                self.p5 = self.win.addPlot(row=3, col=0)
                self.p7 = self.win.addPlot(row=4, col=0)
               
     
                self.curva1 = self.p1.plot(symbol= 'o',symbolBrush='%s' %self.ponto1, width=50)
                self.curva3 = self.p3.plot(symbol= 'o',symbolBrush='%s' %self.ponto3, width=50)
                self.curva5 = self.p5.plot(symbol= 'o',symbolBrush='%s' %self.ponto5, width=50)
                self.curva7 = self.p7.plot(symbol= 'o',symbolBrush='%s' %self.ponto7, width=50)
               
               
                self.p7.setLabel ( 'left' , "%s"%self.eixoy7)
                self.p7.setLabel ( 'right' , "%s"%self.eixoy8)
                self.p3.setLabel ( 'left' , "%s"%self.eixoy3)
                self.p3.setLabel ( 'right' , "%s"%self.eixoy4)
                self.p5.setLabel ( 'left' , "%s"%self.eixoy5)
                self.p5.setLabel ( 'right' , "%s"%self.eixoy6)
                self.p1.setLabel ( 'left' , "%s"%self.eixoy1)
                self.p1.setLabel ( 'right' ,"%s"%self.eixoy2)
                self.p7.setLabel ( 'bottom' , "%s"%self.eixox)
                self.p2 = pg.ViewBox ()
                self.p1.showAxis ('right')
                self.p1.scene (). addItem (self.p2)
                self.p1.getAxis ('right'). linkToView (self.p2)
                self.p2.setXLink (self.p1)
                self.p4 = pg.ViewBox ()
                self.p3.showAxis ('right')
                self.p3.scene (). addItem (self.p4)
                self.p3.getAxis ('right'). linkToView (self.p4)
                self.p4.setXLink (self.p3)
                self.p6 = pg.ViewBox ()
                self.p5.showAxis ('right')
                self.p5.scene (). addItem (self.p6)
                self.p5.getAxis ('right'). linkToView (self.p6)
                self.p6.setXLink (self.p5)
                self.p8 = pg.ViewBox ()
                self.p7.showAxis ('right')
                self.p7.scene (). addItem (self.p8)
                self.p7.getAxis ('right'). linkToView (self.p8)
                self.p8.setXLink (self.p7)
               
                self.legend = pg.LegendItem(None, (60,31))
                self.legend.setParentItem(self.p1.graphicsItem())
                self.legend.addItem(self.curva1,'   %s' %self.eixoy1)
                self.legend2 = pg.LegendItem(None, (60,1))
                self.legend2.setParentItem(self.p3.graphicsItem())
                self.legend2.addItem(self.curva3,'   %s' %self.eixoy3)
                self.legend3 = pg.LegendItem(None, (60,1))
                self.legend3.setParentItem(self.p5.graphicsItem())
                self.legend3.addItem(self.curva5,'   %s' %self.eixoy5)
                self.legend4 = pg.LegendItem(None, (60,1))
                self.legend4.setParentItem(self.p7.graphicsItem())
                self.legend4.addItem(self.curva7,'   %s' %self.eixoy7)
               
                self.update_label14()
           
           
   
    def update_label7(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva4.setData(self.dataX,self.dataY4)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label7)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label7)
               
    def update_label11(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.data5 = float(self.dataC[4])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataY5.append(self.data5)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva4.setData(self.dataX,self.dataY4)
                self.curva5.setData(self.dataX,self.dataY5)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label11)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label11)
               
               
    def update_label8(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.data5 = float(self.dataC[4])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataY5.append(self.data5)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva5.setData(self.dataX,self.dataY5)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                self.curva4 = pg.PlotDataItem(self.dataY4, symbol= 'o',symbolBrush='%s' %self.ponto4, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                    self.legend1.addItem(self.curva4,'  %s' %self.eixoy4)
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
       
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
   
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p4.addItem (self.curva4)
       
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label8)

   
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label8)
                                     
                                     
    def update_label12(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.data5 = float(self.dataC[4])
                self.data6 = float(self.dataC[5])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataY5.append(self.data5)
                self.dataY6.append(self.data6)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva5.setData(self.dataX,self.dataY5)
                self.curva6.setData(self.dataX,self.dataY6)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                self.curva4 = pg.PlotDataItem(self.dataY4, symbol= 'o',symbolBrush='%s' %self.ponto4, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                    self.legend2.addItem(self.curva4,'  %s' %self.eixoy4)
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
       
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
   
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p4.addItem (self.curva4)
       
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label12)

   
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label12)
                                     
                           
    def update_label4(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data3 = float(self.dataC[1])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data3))  
                self.listbox.see('end')
                try:
                    self.arq.write("%.10s,%.1f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data3))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY3.append(self.data3)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
           
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label4)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label4)
               
    def update_label9(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.data5 = float(self.dataC[4])
                self.data6 = float(self.dataC[5])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataY5.append(self.data5)
                self.dataY6.append(self.data6)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva5.setData(self.dataX,self.dataY5)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                self.curva4 = pg.PlotDataItem(self.dataY4, symbol= 'o',symbolBrush='%s' %self.ponto4, width=50) # pen=(255,0,0)
                self.curva6 = pg.PlotDataItem(self.dataY6, symbol= 'o',symbolBrush='%s' %self.ponto6, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                    self.legend1.addItem(self.curva4,'  %s' %self.eixoy4)
                    self.legend2.addItem(self.curva6,'  %s' %self.eixoy6)
           
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
       
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
   
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p4.addItem (self.curva4)
       
                self.p6.setGeometry (self.p5.vb.sceneBoundingRect ())
   
                self.p6.linkedViewChanged (self.p5.vb, self.p6.XAxis)
                self.p6.addItem (self.curva6)
       
       
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label9)

   
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label9)
                                     
    def update_label13(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.data5 = float(self.dataC[4])
                self.data6 = float(self.dataC[5])
                self.data7 = float(self.dataC[6])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6, self.data7))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6, self.data7))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataY5.append(self.data5)
                self.dataY6.append(self.data6)
                self.dataY7.append(self.data7)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva5.setData(self.dataX,self.dataY5)
                self.curva7.setData(self.dataX,self.dataY7)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                self.curva4 = pg.PlotDataItem(self.dataY4, symbol= 'o',symbolBrush='%s' %self.ponto4, width=50) # pen=(255,0,0)
                self.curva6 = pg.PlotDataItem(self.dataY6, symbol= 'o',symbolBrush='%s' %self.ponto6, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                    self.legend2.addItem(self.curva4,'  %s' %self.eixoy4)
                    self.legend3.addItem(self.curva6,'  %s' %self.eixoy6)
                   
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
       
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
   
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p4.addItem (self.curva4)
       
                self.p6.setGeometry (self.p5.vb.sceneBoundingRect ())
   
                self.p6.linkedViewChanged (self.p5.vb, self.p6.XAxis)
                self.p6.addItem (self.curva6)
       
       
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label13)

   
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label13)
                                     
    def update_label14(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.data5 = float(self.dataC[4])
                self.data6 = float(self.dataC[5])
                self.data7 = float(self.dataC[6])
                self.data8 = float(self.dataC[7])
                self.listbox.insert(END,"%.10s    %.1f    %.2f    %.2f    %.2f    %.2f    %.2f    %.2f    %.2f    %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6, self.data7, self.data8))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3, self.data4, self.data5, self.data6, self.data7, self.data8))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataY5.append(self.data5)
                self.dataY6.append(self.data6)
                self.dataY7.append(self.data7)
                self.dataY8.append(self.data8)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva5.setData(self.dataX,self.dataY5)
                self.curva7.setData(self.dataX,self.dataY7)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                self.curva4 = pg.PlotDataItem(self.dataY4, symbol= 'o',symbolBrush='%s' %self.ponto4, width=50) # pen=(255,0,0)
                self.curva6 = pg.PlotDataItem(self.dataY6, symbol= 'o',symbolBrush='%s' %self.ponto6, width=50)
                self.curva8 = pg.PlotDataItem(self.dataY8, symbol= 'o',symbolBrush='%s' %self.ponto8, width=50)# pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                    self.legend2.addItem(self.curva4,'  %s' %self.eixoy4)
                    self.legend3.addItem(self.curva6,'  %s' %self.eixoy6)
                    self.legend4.addItem(self.curva8,'  %s' %self.eixoy8)
             
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
       
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
   
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p4.addItem (self.curva4)
       
                self.p6.setGeometry (self.p5.vb.sceneBoundingRect ())
   
                self.p6.linkedViewChanged (self.p5.vb, self.p6.XAxis)
                self.p6.addItem (self.curva6)
       
                self.p8.setGeometry (self.p7.vb.sceneBoundingRect ())
   
                self.p8.linkedViewChanged (self.p7.vb, self.p8.XAxis)
                self.p8.addItem (self.curva8)
       
       
       
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label14)

   
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label14)
                                     
                                                                 
           
    def update_label6(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva2.setData(self.dataX,self.dataY2)
               
               
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label6)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label6)
       
    def update_label10(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3,self.data4))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3,self.data4))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva2.setData(self.dataX,self.dataY2)
                self.curva4.setData(self.dataX,self.dataY4)
               
               
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label10)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label10)
               
       
    def update_label5(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.data4 = float(self.dataC[3])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3,self.data4))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3,self.data4))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataY4.append(self.data4)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50) # pen=(255,0,0)
                self.curva4 = pg.PlotDataItem(self.dataY4, symbol= 'o',symbolBrush='%s' %self.ponto4, width=50) # pen=(255,0,0)
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
                    self.legend1.addItem(self.curva4,'  %s' %self.eixoy4)

                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
   
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
       
                self.p4.setGeometry (self.p3.vb.sceneBoundingRect ())
   
                self.p4.linkedViewChanged (self.p3.vb, self.p4.XAxis)
                self.p4.addItem (self.curva4)
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label5)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label5)
               
    def update_label3(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.data3 = float(self.dataC[2])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2,self.data3))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2,self.data3))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataY3.append(self.data3)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva3.setData(self.dataX,self.dataY3)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2) # pen=(255,0,0)
                if self.tempo ==0:
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
               
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
               
               
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label3)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label3)
               
   
       
                   
    def update_label2(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.data2 = float(self.dataC[1])
                self.listbox.insert(END,"%.10s   %.1f   %.2f   %.2f " %(self.a,self.tempo,self.data1,self.data2))  
                self.listbox.see('end')
                try:
                    self.arq.write("\n%.10s,%.1f,%.2f,%.2f" %(self.a,self.tempo,self.data1,self.data2))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataY2.append(self.data2)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                self.curva2 = pg.PlotDataItem(self.dataY2, symbol= 'o',symbolBrush='%s' %self.ponto2, width=50)
               
                if self.tempo ==0:
                #self.legend.setParentItem(plotItem)
                    self.legend.addItem(self.curva2,'  %s' %self.eixoy2)
               
                self.p2.setGeometry (self.p1.vb.sceneBoundingRect ())
                self.p2.linkedViewChanged (self.p1.vb, self.p2.XAxis)
                self.p2.addItem (self.curva2)
   
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label2)

               
            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label2)
               
           
    def update_label1(self):
           
                   
            try:
               
                self.a = datetime.now().strftime('%H:%M:%S.%f')    
                self.novodado = self.arduino.readline().decode('utf-8').strip()
                self.dataC = self.novodado.split(',')
                self.data1 = float(self.dataC[0])
                self.listbox.insert(END,"%.10s   %.1f   %.2f " %(self.a,self.tempo,self.data1))  
                self.listbox.see('end')
                try:
                    self.arq.write('\n%.10s,%.1f,%.2f'%(self.a,self.tempo,self.data1))
                except AttributeError:
                    print('Sem arquivo salvo!')
                self.dataY1.append(self.data1)
                self.dataX.append(self.tempo)
                self.curva1.setData(self.dataX,self.dataY1)
                QtGui.QApplication.processEvents()
                self.tempo += float(self.w)
                self.listbox.after(int(float(self.w))*1000, self.update_label1)

            except ValueError:
               
                print('O aplicativo está procurando os dados no formato CSV...')
                print(self.dataC)
                self.listbox.after(1, self.update_label1)
               
           
           
       
           
Lim1 = tk.Entry(Frame1, textvariable = input3 , bd = 10, borderwidth= 0)      
Lim1.pack()
Lim3 = tk.Entry(Frame1, textvariable = input7 , bd = 10,borderwidth= 0,width= 21)      
Lim3.pack()
Lim4 = tk.Entry(Frame1, textvariable = input8 , bd = 10,borderwidth= 0)        
Lim4.pack()
Lim5 = tk.Entry(Frame1, textvariable = input1 , bd = 10,borderwidth= 0)        
Lim5.pack()
Lim2 = tk.Entry(Frame1, textvariable = input4 , bd = 10, borderwidth= 0)      
Lim2.pack()

Bu1f1 = tk.Button(Frame1, text = 'Salvar e Plotar', command =  A ,height= 1, fg = 'black' ,bg = 'white',width=10)
Bu1f1.pack()
Bu2f1 = tk.Button(Frame1, text = 'Ajuda', command =  ajuda , fg = 'black' ,bg = 'white')
Bu2f1.pack()


Frame1.place(anchor = 'nw')                    
text1f1.place(relx = .0, rely = -0.06) #          
text4f1.place(relx = 0.1, rely = .12) #        
text6f1.place(relx = -.1, rely =.05) #          
text7f1.place(relx = -.1, rely =.29)
text9f1.place(relx = 0.08, rely =.36)
text14f1.place(relx = 0.58, rely =.36)

text15f1.place(relx = 0.58, rely =.48)
F.place(relx = 0.08, rely =.68)
T.place(relx = 0.08, rely =.78)
text18f1.place(relx = 0.1, rely =.20)
text10f1.place(relx = 0.08, rely =.45)
text11f1.place(relx = 0.08, rely =.55)
e.place(relx = .58, rely = .68)
text17f1.place(relx = 0.58, rely =.635)
r.place(relx = .58, rely = .53)

Bu1f1.place(relx = .79, rely = 0.9)#
Bu2f1.place(relx = 0.94, rely =- 0.06)

Lim3.place(relx = .085, rely = .403)
Lim4.place(relx = .085, rely = .50)
Lim5.place(relx = .085, rely = .60)

c.place(relx = .585, rely = .410)
Lim1.place(relx = 0.5, rely = .13)#
Lim2.place(relx = 0.605, rely = .205)#
Frame4.place(relx =.526) #                          
text2f4.place(relx = -.01, rely = 0.7)#

janela.mainloop()

