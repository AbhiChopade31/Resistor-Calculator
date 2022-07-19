import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

#Prajakta Yogesh Band
#Roll NO.242
#GR - 22110818
#BAtch - B2

def find():

    main_color_values = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}

    multiplier_values = {"black":1,"brown":10,"red":100,"orange":1000,"yellow":10000,"green":100000,"blue":1000000,"violet":10000000,
    "grey":100000000,"white":1000000000,"gold":0.1,"silver":0.01}

    tolerance_values = {"brown":1,"red":2,"orange":0.05,"yellow":0.02,"green":0.5,"blue":0.25,"violet":0.1,"grey":0.01,"gold":5,"silver":10}

    #Calculation Program
    if e1.get():
        a=e1.get()
        b=e2.get()
        m=e3.get()
        f=e4.get()

        
        x = main_color_values[a]
        y = main_color_values[b]
        d = multiplier_values[m]
        t = tolerance_values[f]

        z = str(x)+str(y)
        p = int(z) #string to integer saved in p
        q = float(d) #Integer to float saved in q
        

        A = p*q
        D = str(A)
        R = str(t)
        B = (D + "  +/-" + R +" ohm")
        ohm = str(B)
        ans['text'] = ohm
    
    else:
        messagebox.showerror('Warning',"Please Check The Input")



# Main Interface
root=Tk()
root.title('Electronics Calculator')
root.geometry('700x500+440+50')
root.configure(bg='black')
root.resizable(0,0)

# GUI
l1=Label(root,text='Electronics Calculator',bg='black',fg='White',font=('calibri',28,'bold','italic'))
l1.pack(pady=10)

l2=Label(root,text='Enter 1st Colour Band :-',bg='black',fg='white',font=('calibri',14,'bold'))
l2.place(x=150,y=100)

l2=Label(root,text='Enter 2nd Colour Band :-',bg='black',fg='white',font=('calibri',14,'bold'))
l2.place(x=150,y=165)

l3=Label(root,text='Enter 3rd Colour Band :-',bg='black',fg='white',font=('calibri',14,'bold'))
l3.place(x=150,y=230)

l4=Label(root,text='Enter 4th Colour Band :-',bg='black',fg='white',font=('calibri',14,'bold'))
l4.place(x=150,y=295)

#Entries of the colour code
e1=Entry(root,bg='white',fg='black',font=('calibri',12)) #Significant Figures
e1.place(x=360,y=105)

e2=Entry(root,bg='white',fg='black',font=('calibri',12)) #Significant Figures
e2.place(x=360,y=170)

e3=Entry(root,bg='white',fg='black',font=('calibri',12)) #Multiplier
e3.place(x=360,y=235)

e4=Entry(root,bg='white',fg='black',font=('calibri',12)) #Tolerance
e4.place(x=360,y=300)

# Button
b1=Button(root,text='Calculate',bg='#231F20',fg='#D3D3D3',bd=2,font=('calibri',14,'bold',),command=find) #To call the find function
b1.place(x=290,y=360)

an=Label(root,text="Answer is:-",bg='black',fg='white',font=('calibri',16))                                                                           
an.place(x=200,y=425)

ans=Label(root,text=" ",bg='black',fg='white',font=('calibri',16))
ans.place(x=330,y=425)

root.mainloop();