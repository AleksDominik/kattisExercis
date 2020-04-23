
import tkinter as tk
from tkinter import Tk, BOTH,RIGHT,LEFT,END
from tkinter.ttk import Frame, Label, Style,Entry
from tkinter.ttk import Frame, Button, Style
import random
import time

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Frame.configure(self,bg="#d0a3d8",height=200,width=200)

        tk.Label(self, text="Mini Jeu: \n P-0", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        bt=Button(self, text="Jouer",
                  command=lambda: master.switch_frame(PageOne,num=True))
        bt.pack(fill=BOTH,expand=True)

        
        # tk.Button(self, text="Go to page two",
        #           command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        

        tk.Frame.__init__(self, master)
        # tk.Frame.configure(self,bg='blue')
        # tk.Label(self, text="Page de jeu", font=('Helvetica', 18, "bold")).pack(side="top", fill=BOTH, pady=5)




        
        frame_left=Frame(self)
        self.frame_left=frame_left
        frame_left.pack(fill=BOTH,side=LEFT)


        # add entry to this frame 
        self.label=tk.Label(frame_left , text="", font=('Helvetica', 10), fg='red')
        self.label.pack()

        self.bagniere_bleu=tk.Canvas(frame_left,width=50,height=3)
        self.bagniere_bleu.pack(side='top',anchor='c')
        self.bagniere_bleu.create_rectangle(0,3,50,0,fill='blue')

        

        self.Nombre_1=Entry(frame_left)
        self.Nombre_1.pack(side='top',anchor='w')

# bagnier pour differencier les couleurs
        self.bagniere_bleu=tk.Canvas(frame_left,width=50,height=3)
        self.bagniere_bleu.pack(side='top',anchor='c')
        self.bagniere_bleu.create_rectangle(0,3,50,0,fill='red')


        self.Nombre_2=Entry(frame_left)
        self.Nombre_2.pack(side='top',anchor='w')

        tk.Button(frame_left, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side='bottom')

        
        self.frame1 = Frame(self)
        self.frame1.pack(fill='x')
        self.rectangle=tk.Canvas(self.frame1)
        self.rectangle.pack()
        self.create_ret(self.rectangle)
        
        # self.update_clock()
        self.master=master
        self.commencer_un_jeu()

        
    def create_circle(self,r, canvasName,color): #center coordinates, radius
        x=random.randint(20,300)
        y=random.randint(20,250)
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1,fill=color)
    def create_ret(self,canvas):
        return canvas.create_rectangle(0,500,500,0,fill="#fdffdb")



    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.master.after(1000,self.update_clock)

    def commencer_un_jeu(self):
        try :
            self.rejouer.destroy()
            self.label.config(text='')
            self.Nombre_2.delete(0,END)
            self.Nombre_1.delete(0,END)

        except:
            pass

        self.bt_valider=tk.Button(self.frame_left,text='valider', command=lambda: self.fin_du_jeu())
        self. bt_valider.pack(side='top',anchor='w')

        self.debut=time.time()

        self.rectangle.destroy()
        self.rectangle=tk.Canvas(self.frame1)
        self.rectangle.pack()
        self.create_ret(self.rectangle)

        self.nombre_j1=random.randint(1,10)
        self.nombre_j2=random.randint(1,10)
        for _ in range(self.nombre_j2):
            self.create_circle(20,self.rectangle,'red')
        for _ in range(self.nombre_j1):
            self.create_circle(20,self.rectangle,'blue')
    def fin_du_jeu(self):
        if(int(self.Nombre_1.get())==self.nombre_j1 ) and (int(self.Nombre_2.get())==self.nombre_j2):
            #jeu gagné
            
            self.bt_valider.destroy()
            self.rejouer=Button(self.frame_left, text="Rejouer",
                       command=lambda: self.commencer_un_jeu())
                       
            self.rejouer.pack(side='top',fill='x')

            self.temps_de_rect=(time.time()-self.debut)
            self.temps_de_rect=time.strftime("%H:%M:%S", time.gmtime(self.temps_de_rect))
            self.label.configure(text=self.temps_de_rect)
            self.rectangle.create_text(200,150,fill="darkblue",font="Times 20 italic bold",
                        text="Victoire")
        else:

            
            self.bt_valider.destroy()
            self.rejouer=Button(self.frame_left, text="Rejouer",
                       command=lambda: self.commencer_un_jeu())

            self.rejouer.pack(side='top',fill='x')

            self.temps_de_rect=(time.time()-self.debut)
            self.temps_de_rect=time.strftime("%H:%M:%S", time.gmtime(self.temps_de_rect))
            self.label.configure(text=self.temps_de_rect)
            self.rectangle.create_text(200,150,fill="darkblue",font="Times 20 italic bold",
                        text="Defaite")


        

        




    
class SampleApp(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        
        self._frame = None
        self.switch_frame(StartPage)
        

    def timer(self,frame_game):
        self.after(1000,frame_game.update_clock)


    def switch_frame(self, frame_class,num=False):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        # try:
        
        # if num:
        #     print(frame_class)
        #     self.timer(frame_class) 
        # except:
        #     print("le frame n'est pas le bon")







class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry('800x800')
    app.mainloop()