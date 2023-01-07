import tkinter as tk
from tkinter import messagebox
class Mgc_Square():
 
 
    
    def __init__(self,w):
        self.w=w
        self.w.configure(bg="dark blue")
        self.w.title('MAGIC SQUARE')   
        self.l=tk.Label(self.w,text='WELCOME TO THE MAGIC SQUARE',font=('castellar',18),bg='dark blue',fg='white')
        self.l.pack()
        self.f1=tk.Frame(self.w)
        self.f1.pack()
        self.f1.config(bg = "dark blue")
        self.f2=tk.Frame(self.w,background='dark blue')
        self.f2.pack()
        self.e1=tk.Entry(self.f1,font=('Bold',18),width=20)
        self.e1.grid(row=0,column=1,columnspan=6,rowspan=2)
        self.show_prompt(1)
        self.e1.bind("<FocusIn>",self.delete_prompt)
        self.e1.bind("<FocusOut>",self.show_prompt)
        self.b1=tk.Button(self.f1,text='Magic',command=self.func,bg = "#2929CC",fg = 'white',font = ('Arial',10,'bold'))
        self.w.bind("<Return>", lambda event: self.func())
        self.b1.grid(row=1,column=0)
        self.number=1
        self.b2=tk.Button(self.f1,text='Clear',command=self.clear,bg = "#2929CC",fg = 'white',font = ('Arial',10,'bold'))
        self.b2.grid(row=1,column=7)
        self.w.bind("<Delete>", lambda event: self.clear())
        self.w.bind('<Escape>', lambda event: self.back3())

        
 
    def delete_prompt(self, e1):
        self.e1.delete(0, tk.END)
        self.e1.config(fg='black')
                                                                                                      
    def show_prompt(self, e1):                                                         
        self.delete_prompt(e1)
        self.e1.config(fg = "#C4C4C4",font=('arial',12))
        self.e1.insert(0, "Insert Dimension e.g(3)")


    def back3(self):
        self.w.destroy()
        root=tk.Tk()
        my_root=Menu(root)
        root.mainloop()
       
        
    def func(self, event = None):
            
            try:
                self.n = int(self.e1.get())  # pairnoume thn diastatsh pou mas dinoun sto entry
                
                
                if self.n!=2 and self.n!=1 and self.n>0:           
                
                    self.c1=tk.Canvas(self.f2,height=40*self.n+20,width=40*self.n+20,bg='dark blue',scrollregion=(0,0,40*self.n+40,40*self.n+40))
                    x_scroll=tk.Scrollbar(self.f2,orient='horizontal',command=self.c1.xview)
                    x_scroll.pack(side='top',fill='x',expand=1)
                    y_scroll=tk.Scrollbar(self.f2,orient='vertical',command=self.c1.yview)
                    y_scroll.pack(side='left',fill='y')
                    self.c1.pack(side='right',fill='both',expand=1)
                    
                    
                    self.c1.configure(yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
                    self.c1.configure(scrollregion=self.c1.bbox('all'))

                    for w in range(10,40*self.n+10,40):
                        for k in range(10,40*self.n+10,40):
                            self.c1.create_line(k,w,k,w+40,fill='#666666',width=2)
                            self.c1.create_line(k+40,w,k+40,w+40,fill='#666666',width=2)
                            self.c1.create_line(k,w,k+40,w,fill='#666666',width=2)
                            self.c1.create_line(k,w+40,k+40,w+40,fill='#666666',width=2)
                    self.size=16
                    r1=10000
 
            
 
 
            
                    for i in range(0,self.n**2+1,r1):
                        self.size=self.size-3
 
                    
 
 
                    if self.n % 2 != 0:
                        self.r=40*self.n//2+10
                        self.c=40*self.n-10
                        self.odd()
                    elif self.n % 4 == 0:
                        self.db_even()
                    else:
                        self.r=40*self.n//4+10
                        self.c=40*self.n//2-10
                        self.c2=40*self.n-10
                        self.r2=30*self.n+10
                        self.c3=40*self.n-10
                        self.r3=10*self.n+10
                        self.c4=40*self.n//2-10
                        self.r4=30*self.n+10
                        self.s_even()
                elif self.n==2 or self.n<0:
                    self.message=messagebox.showerror(title='Error', message='There is not a 2x2 or a Magic Square with a negative dimension')
                else:
                    self.l6=tk.Label(self.f2,text='1',font=('arial',16))
                    self.l6.pack()
            except:
                self.message2=messagebox.showerror(title='Error',message="Please enter only one Natural number for the Dimension of the square!")
        
    def odd(self):
        self.locations=[]
        
        self.y=[self.c,self.r]
        
        while self.number<=self.n**2:
            self.c1.create_text(self.c,self.r,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
            
            self.locations.append(self.y)
            self.c=self.c+40
            self.r=self.r-40
            self.number+=1
            self.forbvalues()
            self.y=[self.c,self.r]
            self.samey()
 
    def db_even(self):
        self.number = 0
        self.LN = [[(self.n * y) + x + 1 for x in range(self.n)] for y in range(self.n)]
        
 
                         
        for r in range(0, self.n // 4):
            for c in range(3 * (self.n // 4), self.n):
                self.number = self.n * self.n + 1 - self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
                
        for r in range(0, self.n // 4):
            for c in range(0, self.n // 4):
                self.number = (self.n * self.n + 1) - self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
        for r in range(3 * (self.n // 4), self.n):
            for c in range(0, self.n // 4):
                self.number = (self.n * self.n + 1) - self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
        for r in range(3 * (self.n // 4), self.n):
            for c in range(3 * (self.n // 4), self.n):
                self.number = (self.n * self.n + 1) - self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
        for r in range(self.n // 4, 3 * (self.n // 4)):
            for c in range(self.n // 4, 3 * (self.n // 4)):
                self.number = (self.n * self.n + 1) - self.LN[r][c]
                self.c1.create_text(40*c+30, 40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
        for r in range(0,self.n//4):
            for c in range(self.n//4,3*(self.n//4)):
                self.number =self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
        for r in range(3*(self.n//4),self.n):
            for c in range(self.n//4,3*(self.n//4)):
                self.number =self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
        for r in range(self.n//4,3*(self.n//4)):
            for c in range(0,self.n//4):
                self.number =self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
                
        for r in range(self.n//4, 3*(self.n//4)):
            for c in range(3*self.n//4,self.n):
                self.number =self.LN[r][c]
                self.c1.create_text(40*c+30,40*r+30,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
               
                
                
 
    def forbvalues(self):
        while self.r not in range(30,40*self.n,40) or self.c not in range(30,40*self.n,40):
            if self.c==40*self.n+30 and self.r==-10:
                self.c=40*self.n-50
                self.r=30
            else:
                if self.c==40*self.n+30:
                    self.c=30
                if self.r<30:
                    self.r=40*self.n-10
 
 
    def samey(self):
        while self.y in self.locations:
            self.c=self.c-80
            self.r=self.r+40
            if self.c==40*self.n+30 and self.r==-10:
                self.c=40*self.n-50
                self.r=30
            else:
                if self.c==40*self.n+30:
                    self.c=30
                if self.r<30:
                    self.r=40*self.n-10
    
            self.y=[self.c,self.r]
    def s_even(self):
 
        self.locations = []
        self.y = [self.c, self.r]
        while self.number <=self.n ** 2 / 4:
            self.c1.create_text(self.c,self.r,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
            self.locations.append(self.y)
            self.c=self.c+40
            self.r=self.r-40
            self.number+=1
            self.forbvalues2()
            self.y=[self.c,self.r]
            self.samey2()
        self.y=[self.c2,self.r2]
        while self.n**2/4<self.number<=self.n**2/2:
            self.c1.create_text(self.c2,self.r2,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
            self.locations.append(self.y)
            self.c2=self.c2+40
            self.r2=self.r2-40
            self.number+=1
            self.forbvalues3()
            self.y=[self.c2,self.r2]
            self.samey3()
        self.y=[self.c3,self.r3]
        while self.n**2/2<self.number<=(self.n**2)*3/4:
            self.c1.create_text(self.c3,self.r3,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
            self.locations.append(self.y)
            self.c3=self.c3+40
            self.r3=self.r3-40
            self.number+=1
            self.forbvalues4()
            self.y=[self.c3,self.r3]
            self.samey4()
        self.y = [self.c4, self.r4]
        while (self.n**2)*3/4 <self.number<= self.n ** 2:
            self.c1.create_text(self.c4,self.r4,text=self.number,fill='white',font=('Helvetica','{}'.format(self.size)))
            self.locations.append(self.y)
            self.c4=self.c4+40
            self.r4=self.r4-40
            self.number+=1
            self.forbvalues5()
            self.y=[self.c4,self.r4]
            self.samey5()
 
    def forbvalues2(self):
        while self.r not in range(30,40*self.n//2,40) or self.c not in range(30,40*self.n//2,40):
            if self.c==40*self.n//2+30 and self.r==-10:
                self.c=40*self.n//2-50
                self.r=30
            else:
                if self.c==40*self.n//2+30:
                    self.c=30
                if self.r<30:
                    self.r=40*self.n//2-10
    def forbvalues3(self):
        while self.r2 not in range(40*self.n//2+30,40*self.n,40) or self.c2 not in range(40*self.n//2+30,40*self.n,40):
            if self.c2==40*self.n+30 and self.r2==40*self.n//2-10:
                self.c2=40*self.n-50
                self.r2=40*self.n//2+30
            else:
                if self.c2==40*self.n+30:
                    self.c2=40*self.n//2+30
                if self.r2<40*self.n//2+30:
                    self.r2=40*self.n-10
    def forbvalues4(self):
        while self.r3 not in range(30,40*self.n//2,40) or self.c3 not in range(40*self.n//2+30,40*self.n,40):
            if self.c3==40*self.n+30 and self.r3==-10:
                self.c3=40*self.n-50
                self.r3=30
            else:
                if self.c3==40*self.n+30:
                    self.c3=40*self.n//2+30
                if self.r3<30:
                    self.r3=40*self.n//2-10
 
    def forbvalues5(self):
        while self.r4 not in range(40*self.n//2+30,40*self.n,40) or self.c4 not in range(30,40*self.n//2,40):
            if self.c4==40*self.n//2+30 and self.r4==40*self.n//2-10:
                self.c4=40*self.n//2-50
                self.r4=40*self.n//2+30
            else:
                if self.c4==40*self.n//2+30:
                    self.c4=30
                if self.r4<40*self.n//2+30:
                    self.r4=40*self.n-10
    
    def samey2(self):
        while self.y in self.locations:
            self.c=self.c-80
            self.r=self.r+40
            if self.c==40*self.n//2+30 and self.r==-10:
                self.c=40*self.n//2-50
                self.r=30
            else:
                if self.c==40*self.n//2+30:
                    self.c=30
                if self.r<30:
                    self.r=40*self.n//2-10
            self.y=[self.c,self.r]
 
    def samey3(self):
        while self.y in self.locations:
            self.c2=self.c2-80
            self.r2=self.r2+40
            if self.c2==40*self.n+30 and self.r2==self.n//2-10:
                self.c2=40*self.n-50
                self.r2=self.n//2+30
            else:
                if self.c2==40*self.n+30:
                    self.c2=self.n//2+30
                if self.r2<self.n//2+30:
                    self.r2=40*self.n-10
            self.y=[self.c2,self.r2]
 
    def samey4(self):
        while self.y in self.locations:
            self.c3=self.c3-80
            self.r3=self.r3+40
            if self.c3==40*self.n+30 and self.r3==-10:
                self.c3=40*self.n-50
                self.r3=30
            else:
                if self.c3==40*self.n+30:
                    self.c3=40*self.n//2+30
                if self.r3<30:
                    self.r3=40*self.n//2-10
            self.y=[self.c3,self.r3]
    def samey5(self):
        while self.y in self.locations:
            self.c4=self.c4-80
            self.r4=self.r4+40
            if self.c4==40*self.n//2+30 and self.r4==40*self.n//2-10:
                self.c4=40*self.n//2-50
                self.r4=40*self.n//2+30
            else:
                if self.c4==40*self.n//2+30:
                    self.c4=30
                if self.r4<40*self.n//2+30:
                    self.r4=40*self.n-10
            self.y=[self.c4,self.r4]
        
            
            
 
    def clear(self):
        self.number = 1
        self.e1.delete(0,'end')
        
 
        for widget in self.f2.winfo_children(): 
          widget.destroy()
        #self.f2.pack_forget()
 
    
class Menu():
    def __init__(self,root):
        self.root = root
        self.root.title('MENU')
        self.root.geometry('700x400')
        self.root.config(bg = '#243763')
        self.lb = tk.Label(self.root,text = 'MAIN MENU',bg = '#243763',fg = 'white',font = ('Helvetica',40,'bold','underline'),height = 1,width = 10)
        self.lb.place(relx = 0.5,rely = 0.12,anchor = 'center')
        self.bt1 = tk.Button(self.root,text = 'MagicSquare',command = self.opensquare,bg ='white',fg = '#243763',font = ('Bodoni',20),width = 10,height = 1)
        self.bt1.place(relx = 0.5, rely = 0.35,anchor = 'center')
        self.bt2 = tk.Button(self.root,text = 'About us',command = self.aboutus,fg = '#243763',font = ('Helvetica',12),width = 9,height = 1)
        self.bt2.place(relx = 0.5,rely = 0.6,anchor = 'center')
        self.bt3 = tk.Button(self.root,text = 'Info',command = self.info,fg = '#243763',font = ('Helvetica',12),width = 9,height = 1)
        self.bt3.place(relx = 0.5,rely = 0.75,anchor = 'center')


    def opensquare(self):
        self.root.destroy()
        self.org_menu()
    def org_menu(self):
        x=tk.Tk()
        mysquare=Mgc_Square(x)
        x.mainloop()
 
 
    def aboutus(self):
        self.root.withdraw()
        self.root1 = tk.Tk()
        self.root1.title('About us')
        self.root1.geometry('800x600')
        self.root1.config(bg = 'dark olive green')
        self.label1 = tk.Label(self.root1,text = 'ΣΧΟΛΗ ΗΛΕΚΤPΟΛΟΓΩΝ ΜΗΧΑΝΙΚΩΝ \n ΚΑΙ ΤΕΧΝOΛΟΓΙΑΣ ΥΠΟΛΟΓΙΣΤΩΝ \n ΠΑΝΕΠIΣΤΗΜΙΟ ΠΑΤΡΩΝ \n--- Ιανουάριος 2023 ---',font = ('Helvetica',25,'bold'),fg = 'white', bg='dark olive green')
        self.label1.place(relx=0.5,rely=0.2,anchor='center')                       
        self.label2 = tk.Label(self.root1,text = 'ΓΑΡΙΔΑΣ ΑΓΓΕΛΟΣ up1100836\n \nΝΤΟΥΝΗΣ ΜΙΧΑΗΛ up1100128 \n \n ΨΑΡΡΟΣ ΓΡΗΓΟΡΙΟΣ up1104673 \n \n ΠΑΠΑΠΑΥΛΟΣ ΣΩΤΗΡΙΟΣ up1100992 ',font = ('Helvetica',20,'bold'),bg = 'dark olive green',fg = 'white')
        self.label2.place(relx  = 0.5,rely = 0.63, anchor = 'center' )
        self.photo=tk.PhotoImage(file=r'C:\Users\Sotos\Desktop\upatraslogo.jpg')
        self.photo3=self.photo.subsample(1, 2)
        self.label3=tk.Label(self.root1, bg='green', image=self.photo3)
        self.label3.place(relx=0.8, rely=0.9)
        self.root1.bind('<Escape>', lambda event: self.back1())
 
 
    def back1(self):
        self.root1.destroy()
        self.root.deiconify()

 
    def info(self):
        self.root.withdraw()
        self.root2 = tk.Tk()
        self.root2.title('Info')
        self.root2.geometry('1250x600')
        self.root2.config(bg = 'white')
        self.root2.title('Info')
        self.title = tk.Label(self.root2,bg = 'white',text = 'Λίγα λόγια για το μαγικό τετράγωνο...',font = ('Arial',20,'bold'))
        self.title.place(relx = 0.5,rely=0.1,anchor = 'center')
        self.lin = tk.Label(self.root2,bg = 'white',text = 'Το μαγικό τετράγωνο αποτελεί διάταξη αριθμών σε συστοιχία ίσου συνόλου γραμμών και στηλών, \n όπου η αριθμητική πράξη μεταξύ των αριθμών στην ίδια σειρά ή στήλη ή διαγώνιο \n του τετραγώνου επιστρέφει πάντα το ίδιο αποτέλεσμα. \n Το κοινό αποτέλεσμα ονομάζεται μαγική σταθερά του μαγικού τετραγώνου. \n Η πλέον συνήθης αριθμητική πράξη στα μαγικά τετράγωνα είναι η πρόσθεση μεταξύ των αριθμών,\n ενώ υπάρχουν και άλλες εκδοχές τους όπως η τέλεση αφαίρεσης ή πολλαπλασιασμού, \n καθώς και είναι δυνατό να αναπαρασταθούν σε τρισδιάστατη μορφή ως μαγικοί κύβοι, \n ή να υπάρξουν τροποποιήσεις όπου αντί για αριθμούς χρησιμοποιούνται σχήματα. \n Η πρώτη περιγραφή μαγικού τετραγώνου υπήρξε στην Κίνα από την 3η χιλιετία π.Χ., \n κατόπιν μεταφέρθηκε στους Ινδούς κατά την ύστερη αρχαιότητα και μετέπειτα στους Άραβες, \n και από εκεί αργότερα στους Βυζαντινούς από όπου μεταδόθηκε στην υπόλοιπη Ευρώπη.\n Κατά τον Μεσαίωνα τα μαγικά τετράγωνα ήταν ιδιαίτερα δημοφιλή ως φυλακτά και αποτροπαϊκά σύμβολα.\n Στην σύγχρονη εποχή αποτελούν συχνό πεδίο ενασχόλησης των ψυχαγωγικών μαθηματικών \n και των μαθηματικών κλάδων της συνδυαστικής και στατιστικής, \n καθώς επίσης της τέχνης και του μυστικισμού, και επίσης σε ότι αφορά τις πρακτικές εφαρμογές τους \n χρησιμοποιούνται για τους σκοπούς της κρυπτογράφησης ψηφιακών εικόνων, \n ενώ στην μηχανική ρευστών για τον υπολογισμό κατακράτησης υδάτων σε επιφάνειες.',
font = ('Arial',18))                            
        self.lin.place(relx=0.5,rely=0.55,anchor='center')
        self.ls = tk.Label(self.root2,text = 'Πηγή :  wikipedia',bg = 'white',font = ('Helvetica',16))
        self.ls.place(relx=0.92,rely=0.97,anchor = 'center')
        self.root2.bind('<Escape>', lambda event: self.back2())


    def back2(self):
        self.root2.destroy()
        self.root.deiconify()



def menu():
    root=tk.Tk()
    my_root=Menu(root)
    root.mainloop()
        
menu()
