from tkinter import*
def cal(c): 
    a=float(e.get())
    b=float(e1.get())
    if c==1:
       res=a+b
    elif c==2:
         res=a-b
    elif c==3:
         res=a*b
    elif c==4:
         res=a/b
    l3=Label(f,text="Result is "+str(res),font=50,width=25,bg="seagreen1")
    l3.place(x=500,y=300)         
    
r=Tk()
r.geometry('900x900')
f=Frame(r,width=1500,height=1500,bg="turquoise3")
f.place(x=0,y=0)

l=Label(f,text="SIMPLE CALCULATER",font=('Georgia', 20),bg="turquoise2")
l.place(x=300,y=50)

l1=Label(f,text="Enter first value:",bg="turquoise1",font=10,width=15)
l1.place(x=250,y=150)
l2=Label(f,text="Enter second value:",bg="turquoise1",font=10,width=15)
l2.place(x=250,y=180)
e=Entry(f,width=15)
e1=Entry(f,width=15)
e.place(x=400,y=150)
e1.place(x=400,y=180)
ad_button=Button(f,text="ADD",bg="cyan4",fg="black",font=10,width=15,command=lambda:cal(1))
ad_button.place(x=250,y=250)

sub_button=Button(f,text="SUBSTRACT",bg="cyan4",fg="black",font=10,width=15,command=lambda:cal(2))
sub_button.place(x=250,y=290)

mul_button=Button(f,text="MULTIPLICATION",bg="cyan4",fg="black",font=10,width=15,command=lambda:cal(3))
mul_button.place(x=250,y=330)

div_button=Button(f,text="DIVISION",bg="cyan4",fg="black",font=10,width=15,command=lambda:cal(4))
div_button.place(x=250,y=370)

r.mainloop()