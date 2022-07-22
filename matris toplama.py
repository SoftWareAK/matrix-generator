from tkinter import*
import random as r
m1=[]
m2=[]
ms=[]

def hesapla():
    global m1,m2,ms
    m1=[]
    m2=[]
    t1.delete(1.0,END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    for i in range(0,3):
        satir=[r.randint(0,4),r.randint(0,4),r.randint(0,4)]
        m1.append(satir)
        t1.insert(INSERT,str(satir)+"\n")
        satir2 = [r.randint(0, 4), r.randint(0, 4), r.randint(0, 4)]
        m2.append(satir2)
        t2.insert(INSERT, str(satir2) + "\n")

    #toplama işlemi
    ms=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
             ms[i][j]= m1[i][j]+ m2[i][j]
        t3.insert(INSERT, str(ms[i]) + "\n")
    print(ms)

pencere=Tk()
pencere.geometry("400x150")

t1=Text(width=7,height=3,font="Verdana 14 bold")
t1.place(x=10,y=10)


t2=Text(width=7,height=3,font="Verdana 14 bold")
t2.place(x=150,y=10)

t3=Text(width=7,height=3,font="Verdana 14 bold",bg="yellow")
t3.place(x=290,y=10)

b=Button(text="Oluştur ve topla",font="Verdana 14 bold",command=hesapla)
b.place(x=100,y=100)











pencere.mainloop()