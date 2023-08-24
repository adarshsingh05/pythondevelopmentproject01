from tkinter import*
from tkinter import ttk
from PIL import Image ,ImageTk
from tkinter import messagebox
import mysql.connector
from details import Details
from hotel import HotelManagementSystem



# for he other login page
def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()













# we have created two windows in a single class so that we can enhance the performance

class Login_Window:

# defining the constructor
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
# size declaratiion
        self.root.geometry("1550x800+0+0")

        # for the image

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\loginwindowbg.jpg")
        lbl_bg=Label(self.root,image=self.bg)

        # giving x and y coordinates
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)



        # creating the frame

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black" , borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)


        # creating the other label for details
        get_str=Label(frame,text="get started",font=("times new roman",20,"bold"),fg="white",bg="black")
 

        # now placing the label,since we are placing under the frame not in root thus we need x and y

        get_str.place(x=106,y=100)


        # labels for username we are going to create 

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=150)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=45,y=185,width=270)


        # creating label for password
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=220)


        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=45,y=255,width=270)


        # putting icon images  resize the icons properly search on google icons
        img2=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\username.png")
        img=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black" , borderwidth=0)
        lblimg2.place(x=655,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\password.png")
        img=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black" , borderwidth=0)
        lblimg3.place(x=655,y=393,width=25,height=25)




        # creating button for login

        loginbtn=Button(frame,command=self.login,text="Login",font=("new times roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red", activeforeground="blue")
        loginbtn.place(x=110,y=316,width=120,height=35 )

        # register button
        registerbtn=Button(frame,text="Register",command=self.register_window,font=("new times roman",13,"bold"),borderwidth=0,bd=3,relief=RIDGE,fg="white",bg="black",activebackground="red", activeforeground="blue")
        registerbtn.place(x=30,y=380,width=120,height=35 )

        # forgot password
        forgotbtn=Button(frame,text="Forgot pass",command=self.forgot_password_window,font=("new times roman",13,"bold"),borderwidth=0,bd=3,relief=RIDGE,fg="white",bg="black",activebackground="red", activeforeground="blue")
        forgotbtn.place(x=170,y=380,width=150,height=35 )
















    # creating a new function to redirect to the register page

    def register_window(self):
        self.new_Window=Toplevel(self.root)
        self.app=Register(self.new_Window)




















        # function for the login page
        # also we need to call under the button using the command tool

    def login(self):
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error", "all field required")

            elif self.txtuser.get()=="raj" and self.txtpass.get()=="raj1234":
                 
                 messagebox.showinfo("Success","welcome to the site")

            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='a8400629408', database='mydata')
                mycursor=conn.cursor()
                mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()

                ))

                # collecting data while login
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Eroor","Invalid username or password")
                else:
                    open_main=messagebox.askyesno("YesNo","Eccess only admin")
                    if open_main>0:
                        self.new_Window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_Window)
                        # adding a new page or the project to redirect after login
                        # we are still to add that login page
                        # messagebox.showinfo("logined")
                    else:
                        if not  open_main:
                            return
                conn.commit()
                conn.close()












    # RESET PASSWORD WINDOW



    def reset_pass(self):
        if self.combo_security_Q.get=="Select":
            messagebox.showerror("ERROR","Select the security question")
        elif self.txt_security.get()=="":
            messagebox.showerror("ERROR","Please select answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("ERROR","Please enter the new password")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='a8400629408', database='mydata')
            mycursor=conn.cursor()
            query=("select * from register where email %s and securityQ=%s and securityA %s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            mycursor.execute(query,value)
            # fetching the aoive data and storing in variable
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Erorr","please enter the correct answer")
            # updating the query
            else:
                query=("update register set password=%s where email %s")
                value(self.txt_newpass.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password has been reset properly please login with new password",parent=self.root2)
                self.root2.destroy()










        # function for the forgot password THE FORGOT PASSWORD WINDOW
        #  forgot password is not working


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Eroor","Please enter the email to reset password")
        else:
            # connection creting to fetch the data
                conn=mysql.connector.connect(host='localhost',username='root',password='a8400629408', database='mydata')
                mycursor=conn.cursor()
                # my sql quesry to fecth the data
                query=("select * from register where email=%s")
                value=(self.txtuser.get(),)
                mycursor.execute(query,value)
                # storing the data which was fetched earlier and adding the command in the button( name of the function)
                row=mycursor.fetchone()
                # to print the data in the terminal
                # print(row)

                if row==None:
                    messagebox.showerror("Erorr","Please enter the valid email address")
                else:
                    conn.close()
                    # creating the main window to open while resetiing password
                    self.root2=Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("340x450+610+170")

                    # creating the lable for the new window
                    l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                    l.place(x=0,y=10,relwidth=1)







                    # ading the security window and pass
                    security_Q=Label(self.root2,text="Select secuity question",font=("times new roman",15,"bold",),bg="white",fg="black")
                    security_Q.place(x=50,y=80)


                    self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                    self.combo_security_Q["values"]=("Select","Your birth place","your girlfriend name","your pet name")
                    self.combo_security_Q.place(x=50,y=110,width=250)

                    # using tuple to put the value intial=0
                    self.combo_security_Q.current(0)

                    # answer

                    security_A=Label(self.root2,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                    security_A.place(x=50,y=150)

                    self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                    self.txt_security.place(x=50,y=180,width=250)


                    # entry fill for the password reset or the new password entry fill


                    new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg="black")
                    new_password.place(x=50,y=220)

                    self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                    self.txt_newpass.place(x=50,y=250,width=250)

                    # creating the button
                    btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                    btn.place(x=135,y=295)





    
    
                













# for the login 2 to connect the database one



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
        b2=Button(frame,image=self.photoimage1,borderwidth=0,command=self.return_login,cursor="hand2",bg="white")
        b2.place(x=300,y=470,width=300)








        # adding the functionlity to the register button using function, we stored in the variable defined at the 
        # top of the code ad now we w=use those datas to provide the functionality to the code
    
    
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
        




        # function to redirect to the login page

    def return_login(self):
        self.root.destroy()










if __name__ =="__main__":
    main()





