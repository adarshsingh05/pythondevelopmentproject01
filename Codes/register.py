from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from login import Login_Window



class Register:
    def __init__ (self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x910+0+0")


        # creating text variable to collect data from entryfill

        self.var_fname= StringVar()
        self.var_lname= StringVar()
        self.var_contact= StringVar()
        self.var_email= StringVar()
        self.var_securityQ= StringVar()
        self.var_securityA= StringVar()
        self.var_pass= StringVar()
        self.var_confpass= StringVar()
        self.var_check= IntVar()




        # adding background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\hotelbg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)


        # left background image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\leftbg.jpg")
        left_lbl=Label(self.root,image=self.bg)
        # change the photo later on there
        left_lbl.place(x=50,y=100,height=550,width=470)


        # creating the main frame on the right side

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        # creating the register label (under the frame nnot in the root)
        register_lbl=Label(frame,text="REGISTER HERE!",font=("times new roman",20,"bold"),fg="red", bg="white")
        register_lbl.place(x=20,y=30)


        # creating the labels and the entries
        fname=Label(frame,text="First name", font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=145,width=250)

        lname=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)
    
        self.txt_lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname_entry.place(x=370,y=145,width=250)

        # for the contact no

        contact=Label(frame,text="Contact no",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=180)
    
        self.txt_contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact_entry.place(x=50,y=210,width=250)

        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=180)
    
        self.txt_email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email_entry.place(x=370,y=210,width=250)

        # for the security questions

        security_Q=Label(frame,text="Select secuity question",font=("times new roman",15,"bold",),bg="white",fg="black")
        security_Q.place(x=50,y=260)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place","your girlfriend name","your pet name")
        self.combo_security_Q.place(x=50,y=310,width=250)

        # using tuple to put the value intial=0
        self.combo_security_Q.current(0)

        # answer

        security_A=Label(frame,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=260)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=310,width=250)


        # for password section
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=355)

        password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        password.place(x=50,y=385,width=250)

        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cpassword.place(x=370,y=355)

        cpassword=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        cpassword.place(x=370,y=385,width=250)




        ##############checkbox##############
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms & conditions",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=437)

        # creating the button
        # command =self.register data is use to provide the command to the button

        
        img=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\registerbtn.jpeg")
        img=img.resize((140,36), Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data2,borderwidth=0,cursor="hand2",bg="white",font=("times new roman",15,"bold"))
        b1.place(x=10,y=485,width=300)


        # redirecting to the login page button
        img2=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\loginbtn.jpeg")
        img2=img2.resize((150,68), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img2)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,command=self.login,cursor="hand2",bg="white")
        b2.place(x=300,y=470,width=300)








        # adding the functionlity to the register button using function, we stored in the variable defined at the 
        # top of the code ad now we we use those datas to provide the functionality to the code
    
    
    def register_data2(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the terms and conditions")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='a8400629408', database='mydata')
            mycursor=conn.cursor()
            query=("select * from register where email = %s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            # fetching email daata to avoid the duplicacy
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already exixst")
            # else adding the data to the base
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","registerd successfully")

    def login(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)
















if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
