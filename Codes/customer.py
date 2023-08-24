from tkinter import *
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random



class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1310x580+225+215")


        # variable to connect the data base



        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))


        self.var_custname=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        
        
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()
        






################# TITLE ##################
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1500,height=50)





################ LOGO ########################
        img2=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\hotellleftlogo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)







############# lable frame #####################
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",14,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)





################ label and entry ##############
    #    custref

        lbl_custref=Label(labelframeleft,text="Customer refer no",padx=0,pady=6,font=("arial",12,"bold"),)
        lbl_custref.grid(row=0,column=0)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1,sticky=W,padx=4)


    #   custname

        cname=Label(labelframeleft,text="Customer Name ",padx=2,pady=6,font=("arial",12,"bold"))
        cname.grid(row=1,column=0)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_custname,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1,sticky=W,padx=4)

    
    # mother name

        lblmname=Label(labelframeleft,text="Mother's Name  ",padx=0,pady=6,font=("arial",12,"bold"))
        lblmname.grid(row=2,column=0)

        txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("arial",13,"bold"))
        txtcname.grid(row=2,column=1,sticky=W,padx=4)

    
    # gender combobox
        label_gender=Label(labelframeleft,font=("arial",13,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W,padx=0)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",13,"bold"),width=27,state="readonly")
        
        combo_gender["value"]=("Male","Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


    # postcode

        lblPostCode=Label(labelframeleft,text="Post Code",padx=2,pady=6,font=("arial",12,"bold"))
        lblPostCode.grid(row=4,column=0 ,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1,sticky=W,padx=4)


    # mobile number

        lblmobile=Label(labelframeleft,text="Mobile",padx=2,pady=6,font=("arial",12,"bold"))
        lblmobile.grid(row=5,column=0 ,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1,sticky=W,padx=4)


    # email

       

        lblemail=Label(labelframeleft,text="Email",padx=2,pady=6,font=("arial",12,"bold"))
        lblemail.grid(row=6,column=0 ,sticky=W)

        txtemail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1,sticky=W,padx=4)


    # nationality
        labelNationality=Label(labelframeleft,font=("arial",13,"bold"),text="Nationality",padx=2,pady=6)
        labelNationality.grid(row=7,column=0,sticky=W,padx=0)
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",13,"bold"),width=27,state="readonly")
        
        combo_nationality["value"]=("Indian","Americal", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)


    # idproof type

        labelIdProof=Label(labelframeleft,font=("arial",13,"bold"),text="IdProof",padx=2,pady=6)
        labelIdProof.grid(row=8,column=0,sticky=W,padx=0)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",13,"bold"),width=27,state="readonly")
        
        combo_id["value"]=("Adhar","Passport", "Driving licence")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
    
    # id number

        lblIdNumber=Label(labelframeleft,text="IdNumber",padx=2,pady=6,font=("arial",12,"bold"))
        lblIdNumber.grid(row=9,column=0 ,sticky=W)

        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1,sticky=W,padx=4)

    # address
        lblAddress=Label(labelframeleft,text="Address",padx=2,pady=6,font=("arial",12,"bold"))
        lblAddress.grid(row=10,column=0 ,sticky=W)

        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1,sticky=W,padx=4)

        ######### buttons ################
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)



         ###############  table frame for database ########


        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",14,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchbar=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white",pady=2)
        lblSearchbar.grid(row=0,column=0 ,sticky=W)




        # creating variable for the search by data
        self.search_var=StringVar



        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",13,"bold"),width=24,state="readonly")
        
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        # creating the variable for the search data

        self.txt_search=StringVar()


        # for the entry fill

        txtSearch=ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,sticky=W,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)


        ############  The data table ###########
        details_table=LabelFrame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        # creating the scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        # creating the table
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
 
        # to view the data in left window
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        # adjusting the width of the columns
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)


        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        # creating the function for the buttons and adding to database
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employeedetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_ref.get(),
                                                                                                self.var_custname.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_address.get(),
                                                                                                
                ))
                conn.commit()
                # calling the fetch data function
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)











# creating the function to show the data in gui



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employeedetails")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(* self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
            conn.close()




            # function to show data in respective column
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_custname.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        
        
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])



        # working on the update button
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error message","Please enter the mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            my_cursor.execute("update employeedetails set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,idnumber=%s,Address=%s where Ref=%s",(
                                                                                                
                                                                                                self.var_custname.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_ref.get(),                                                                                                                                                  
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Customer's details has been updates successfully")
    
    
    
    
    
    # deleteb button functionality



    def mDelete(self):
       
        mDelete=messagebox.askyesno("Delete","Do you want to delete the customer's details?" , parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            query="delete from employeedetails where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 


        # reset function
    def reset(self):
        self.var_ref.set(""),
        self.var_custname.set(""),
        self.var_mother.set(""),
        self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        
        self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")


# solve this problem of search by ref lect 03
        # function for search button

    def search(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from employeedetails where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
            conn.close()                                                                                                 



if __name__== "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()