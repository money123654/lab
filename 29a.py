from tkinter import *
def disp():
    f1=Frame(f,width=900,height=900,bg="light blue")
    f1.place(x=0,y=0)
    l6=Label(f,text="Employee details ",bg="yellow",font=20)
    l6.place(x=100,y=100)
    t=Text(f,width=50,height=10)
    t.place(x=100,y=200)
    ename=e.get()
    t.insert(END,"NAME : "+ename+"\n")
    qual=""
    if v.get()==1:
        qual=qual+c["text"]+" "
    if v1.get()==1:
        qual=qual+c1["text"]+" "
    if v2.get()==1:
        qual=qual+c2["text"]+" "
    if v3.get()==1:
        qual=qual+c3["text"]+" "
    t.insert(END,"QUALIFICATION : "+qual+"\n")
    esal=e2.get()
    t.insert(END,"SALARY : "+str(esal)+"\n")
    if v4.get()==1:
        t.insert(END,"GENDER : male "+"\n")
    elif v4.get()==2:
        t.insert(END,"GENDER : female "+"\n")
    des=v5.get()
    t.insert(END,"DESIGNATION : "+des+"\n")
    #f1.tkraise()
r=Tk()
r.geometry('900x900')
f=Frame(r,width=900,height=900,bg="red")
f.place(x=0,y=0)
l=Label(f,text="Employee details ",bg="yellow",font=20)
l.place(x=400,y=100)
l1=Label(f,text="Employee name ",bg="yellow")
l1.place(x=100,y=200)
e=Entry(f,width=15)
e.place(x=230,y=200)
l2=Label(f,text="Enter Qualification ",bg="yellow")
l2.place(x=100,y=250)
v=IntVar()
c=Checkbutton(f,text="SSLC",variable=v)
c.place(x=230,y=300)
v1=IntVar()
c1=Checkbutton(f,text="PUC",variable=v1)
c1.place(x=230,y=350)
v2=IntVar()
c2=Checkbutton(f,text="BE",variable=v2)
c2.place(x=230,y=400)
v3=IntVar()
c3=Checkbutton(f,text="PHD",variable=v3)
c3.place(x=230,y=250)
l3=Label(f,text="Enter salary ",bg="yellow")
l3.place(x=100,y=450)
e2=Entry(f,width=15)
e2.place(x=230,y=450)
l4=Label(f,text="Enter gender ",bg="yellow")
l4.place(x=100,y=500)
v4=IntVar()
r=Radiobutton(f,text="male",variable=v4,value=1)
r.place(x=230,y=500)
r1=Radiobutton(f,text="female",variable=v4,value=2)
r1.place(x=230,y=540)
l5=Label(f,text="Enter designation ",bg="yellow")
l5.place(x=100,y=590)
v5=StringVar()
s=Spinbox(f,text=("manager","intern","HR"),textvariable=v5)
s.place(x=230,y=590)
b=Button(f,text="submit",bg="light blue",command=disp)
b.place(x=400,y=650)
r.mainloop()