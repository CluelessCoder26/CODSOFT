from tkinter import *
from tkinter import messagebox
import ast
import webbrowser

interface=Tk()
interface.title("Mobile app login")
interface.geometry('925x500+300+200')
interface.configure(bg='#fff')
interface.resizable(False,False)

def open_facebook():
    webbrowser.open('https://www.facebook.com/login')
def open_twitter():
    webbrowser.open('https://twitter.com/login')

#---------------------------------------------#

def sign_up():
    window=Toplevel(interface)
    window.title("Sign Up")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    imgSignin=PhotoImage(file='signin.png')
    Label(window,image=imgSignin,border=0,bg='white').place(x=50,y=90)

    frame=Frame(window,width=350,height=390,bg='white')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI',23,'bold'))
    heading.place(x=120,y=5)

    def sign_up(event=None):
        username=user.get()
        password=passcode.get()
        confirm_password=code.get()
        if password==confirm_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()
                file=open('datasheet.txt', 'w')
                w=file.write(str(r))
                messagebox.showinfo('Success','Sign up successful')
                window.destroy()
            except:
                file=open('datasheet.txt', 'w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', "Both the passwords should be same")
            
                
    ######**************************************************

    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
        

    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25 ,y=107)

    #####****************************************************

    def on_enter(e):
        passcode.delete(0,'end')

    def on_leave(e):
        name=passcode.get()
        if name=='':
            passcode.insert(0,'Enter Password')
        

    passcode=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    passcode.place(x=30,y=150)
    passcode.insert(0,'Enter Password')
    passcode.bind('<FocusIn>',on_enter)
    passcode.bind('<FocusOut>',on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25 ,y=177)

    #####****************************************************

    def on_enter_code(e):
        code.delete(0, 'end')

    def on_leave_code(e):
        if not code.get():
            code.insert(0, 'Confirm Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=220)
    code.insert(0, 'Confirm Password')
    code.bind('<FocusIn>', on_enter_code)
    code.bind('<FocusOut>', on_leave_code)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    #####*******************************************************

    Button(frame,width=39,pady=10,text='Sign up',bg='#57a1f8',fg='white',border=2,command=sign_up).place(x=35 ,y=270)
    window.bind('<Return>',sign_up)
    window.mainloop()


#---------------------------------------------#

def sign_in():
    root=Toplevel(interface)
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)

    def sign_in(event=None):
        username=user.get()
        password=passcode.get()

        file=open('datasheet.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()    

        if username in r.keys()and password in r.values():
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg='white')

            Label(screen,text='Welcome to the mobile application!!!!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

            screen.mainloop()
        else:
            messagebox.showerror("Invalid","Invalid Username or password")
        
    img=PhotoImage(file='login.png')
    Label(root,image=img,bg='white').place(x=50,y=50)

    frame=Frame(root,width=350,height=350,bg='white')
    frame.place(x=480,y=70)

    heading=Label(frame,text='SIGN IN',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI',23,'bold'))
    heading.place(x=110,y=5)

    #####***********************************************
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
        

    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25 ,y=107)

    #####************************************************
    def on_enter(e):
        passcode.delete(0,'end')

    def on_leave(e):
        name=passcode.get()
        if name=='':
            passcode.insert(0,'Password')
        

    passcode=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    passcode.place(x=30,y=150)
    passcode.insert(0,'Password')
    passcode.bind('<FocusIn>',on_enter)
    passcode.bind('<FocusOut>',on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25 ,y=177)

    #####****************************************************

    Button(frame,width=39,pady=10,text='Sign in',bg='#57a1f8',fg='white',border=2,command=sign_in).place(x=35 ,y=204)
    root.bind('<Return>',sign_in)

    root.mainloop()



#---------------------------------------------#    

img=PhotoImage(file='interface.png')
Label(interface,image=img,border=0,bg='white').place(x=50,y=90)
frame=Frame(interface,width=350,height=390,bg='white')
frame.place(x=480,y=50)

heading=Label(frame,text='Welcome to Mobile App',fg='purple',bg='white',font=('Microsoft Yahei UI',20,'bold'))
heading.place(x=0,y=55)

Button(frame,width=20,text='Login with Facebook',border=0,bg='white',cursor='hand2',fg='purple',font=(18),command=open_facebook).place(x=50 ,y=117)
img1=PhotoImage(file='facebook.png')
Label(frame,image=img1,border=0,bg='white').place(x=35,y=117)

Button(frame,width=20,text='Login with X',border=0,bg='white',cursor='hand2',fg='purple',font=(18),command=open_twitter).place(x=14 ,y=160)
img2=PhotoImage(file='twitter.png')
Label(frame,image=img2,border=0,bg='white').place(x=35,y=165)

Button(frame,width=39,pady=10,text='Sign up',bg='#57a1f8',fg='white',border=2,command=sign_up).place(x=35 ,y=270)
label=Label(frame,text="Already having an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=320)
sign_in=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign_in)
sign_in.place(x=235,y=320)


interface.mainloop()
