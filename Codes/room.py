from tkinter import *
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import datetime



class RoomBooking:
        def __init__(self,root):
            self.root=root
            self.root.title("Hotel Management System")
            self.root.geometry("1310x580+225+215")

        ############# variables to strore the data #############
            self.var_contact=StringVar()
            self.var_checkin=StringVar()
            self.var_chectout=StringVar()
            self.var_roomtype=StringVar()
            self.var_roomavailable=StringVar()
            self.var_meal=StringVar()
            self.var_noOfdays=StringVar()
            self.var_paidtax=StringVar()
            self.var_actualtotal=StringVar()
            self.var_total=StringVar()


        ################# TITLE ##################
            lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            lbl_title.place(x=0,y=0,width=1500,height=50)





        ################ LOGO ########################
            img2=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\hotellleftlogo.jpg")
            img2=img2.resize((230,140),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=100,height=50)


        ############# lable frame #####################
            labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",14,"bold"))
            labelframeleft.place(x=5,y=50,width=425,height=490)


        ################ label and entry ##############
    #    custcontact

            lbl_custcontact=Label(labelframeleft,text="Customer Contact",padx=0,pady=6,font=("arial",12,"bold"),)
            lbl_custcontact.grid(row=0,column=0)

            entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
            entry_contact.grid(row=0,column=1,sticky=W,padx=4)


#       fetch data button

            btnFetchdata=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
            btnFetchdata.place(x=343,y=4)

    #   check in date

            check_in_date=Label(labelframeleft,text="Check in date ",padx=2,pady=6,font=("arial",12,"bold"))
            check_in_date.grid(row=1,column=0)

            txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("arial",13,"bold"))
            txtcheck_in_date.grid(row=1,column=1,sticky=W,padx=4)



    #   check out date

            lbl_check_out_date=Label(labelframeleft,text="Check out date ",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_check_out_date.grid(row=2,column=0)

            txtcheck_out_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_chectout,font=("arial",13,"bold"))
            txtcheck_out_date.grid(row=2,column=1,sticky=W,padx=4)


    #   room type

            lbl_roomtype=Label(labelframeleft,text="Room Type ",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_roomtype.grid(row=3,column=0,sticky=W)

            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            my_cursor.execute("select RoomType from details")
            ide=my_cursor.fetchall()


            # creating the combobox

            combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,textvariable=self.var_roomtype,state="readonly")
            combo_RoomType["values"]=ide
            combo_RoomType.current(0)
            combo_RoomType.grid(row=3,column=1)

           



    #  available room
            lbl_availableroom=Label(labelframeleft,text="Available room ",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_availableroom.grid(row=4,column=0)

            # txtavailableroom=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable,font=("arial",13,"bold"))
            # txtavailableroom.grid(row=4,column=1,sticky=W,padx=4)







#           creating the database to collect data from the other window

            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            my_cursor.execute("select RoomNo from details")
            rows=my_cursor.fetchall()





            # adding combo boxes for available rooms

            combo_RoomNo=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,textvariable=self.var_roomavailable,state="readonly")
            combo_RoomNo["values"]=rows
            combo_RoomNo.current(0)
            combo_RoomNo.grid(row=4,column=1)

            #  meal
            lbl_meal=Label(labelframeleft,text="Meal",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_meal.grid(row=5,column=0)

            txtmeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))
            txtmeal.grid(row=5,column=1,sticky=W,padx=4)


        #    no of days
            lbl_NoOfDays=Label(labelframeleft,text="No Of Days",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_NoOfDays.grid(row=6,column=0)

            txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noOfdays,font=("arial",13,"bold"))
            txtNoOfDays.grid(row=6,column=1,sticky=W,padx=4)


        #    tax paid
            lbl_taxpaid=Label(labelframeleft,text="Paid Tax:",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_taxpaid.grid(row=7,column=0)

            txttaxpaid=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("arial",13,"bold"))
            txttaxpaid.grid(row=7,column=1,sticky=W,padx=4)


        #    Sub Total
            lbl_SubTotal=Label(labelframeleft,text="Sub Total:",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_SubTotal.grid(row=8,column=0)

            txtSubTotal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("arial",13,"bold"))
            txtSubTotal.grid(row=8,column=1,sticky=W,padx=4)

        #    Total cost
            lbl_Totalcost=Label(labelframeleft,text="Total Cost:",padx=2,pady=6,font=("arial",12,"bold"))
            lbl_Totalcost.grid(row=9,column=0)

            txtTotalcost=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"))
            txtTotalcost.grid(row=9,column=1,sticky=W,padx=4)




# ################# bill button ###############

            btnbill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
            btnbill.grid(row=10,column=0,padx=1,sticky=W)



################ other buttons ##############
            btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE,)
            btn_frame.place(x=0,y=400,width=412,height=40)


            btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
            btnAdd.grid(row=0,column=0,padx=1)

            btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
            btnUpdate.grid(row=0,column=1,padx=1)

            btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
            btnDelete.grid(row=0,column=2,padx=1)

            btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
            btnReset.grid(row=0,column=3,padx=1)


###################### right side image #################

            img3=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\hotelbedroomimage.jpg")
            img3=img3.resize((700,250),Image.ANTIALIAS)
            self.photoimg3=ImageTk.PhotoImage(img3)

            lblimg3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
            lblimg3.place(x=760,y=55,width=537,height=210)





#  outline for the below table data
            Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",14,"bold"))
            Table_Frame.place(x=435,y=290,width=860,height=490)

            lblSearchbar=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white",pady=2)
            lblSearchbar.grid(row=0,column=0 ,sticky=W)




        # creating variable for the search by data
            self.search_var=StringVar



            combo_search=ttk.Combobox(Table_Frame,font=("arial",13,"bold"),width=24,state="readonly")
        
            combo_search["value"]=("Contact","Ref")
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








################ Show the table frame search system ###############



            details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
            details_table.place(x=0,y=50,width=860,height=180)

        # creating the scroll bar
            scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        # creating the table
            self.room_Table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomsavailable","meal","noofdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.room_Table.xview)
            scroll_y.config(command=self.room_Table.yview)
 
        # to view the data in left window
            self.room_Table.heading("contact",text="Contact")
            self.room_Table.heading("checkin",text="Check-in")
            self.room_Table.heading("checkout",text="Check-out")
            self.room_Table.heading("roomtype",text="Room TYpe")
            self.room_Table.heading("roomsavailable",text="Room Available")
            self.room_Table.heading("meal",text="Meal")
            self.room_Table.heading("noofdays",text="NoOfDays")


            self.room_Table["show"]="headings"

        # adjusting the width of the columns
            self.room_Table.column("contact",width=100)
            self.room_Table.column("checkin",width=100)
            self.room_Table.column("checkout",width=100)
            self.room_Table.column("roomtype",width=100)
            self.room_Table.column("roomsavailable",width=100)
            self.room_Table.column("meal",width=100)
            self.room_Table.column("noofdays",width=100)


            self.room_Table.pack(fill=BOTH,expand=1)


        # bionding the function

            self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)


        # calling the fetch data to show 

            self.fetch_data()












    # function to show data on the right side to fetch the data












# creating function for the button to add room details in database



        def add_data(self):
            if self.var_contact.get()=="" or self.var_checkin.get()=="":
                messagebox.showerror("Error","All fields required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_checkin.get(),
                                                                                                            self.var_chectout.get(),
                                                                                                            self.var_roomtype.get(),
                                                                                                            self.var_roomavailable.get(),
                                                                                                            self.var_meal.get(),
                                                                                                            self.var_noOfdays.get()
                                                                                                          
                                                                                                
                    ))
                    conn.commit()
                    # calling the fetch data function
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Success","Customer's Details has been added",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)






                ############ fetch data function ################

        def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_Table.delete(* self.room_Table.get_children())
                for i in rows:
                    self.room_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()


    # get cursor
    # function for the other buttons and show the data in entry fill
        def get_cursor(self,event=""):
            cursor_row=self.room_Table.focus()
            content=self.room_Table.item(cursor_row)
            row=content["values"]




            self.var_contact.set(row[0]),
            self.var_checkin.set(row[1]),
            self.var_chectout.set(row[2]),
            self.var_roomtype.set(row[3]),
            self.var_roomavailable.set(row[4]),
            self.var_meal.set(row[5]),
            self.var_noOfdays.set(row[6])


        





########### working on update button ###############

        def update(self):
            if self.var_contact.get()=="":
             messagebox.showerror("Error message","Please enter the mobile number",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                my_cursor.execute("update room set checkin=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                
                                                                                                self.var_checkin.get(),
                                                                                                self.var_chectout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noOfdays.get(),
                                                                                                self.var_contact.get()
                                                                                                                                                                                                                                                
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Updated","Room details has been updates successfully")




############### working on the delete button ###################

        def mDelete(self):
       
            mDelete=messagebox.askyesno("Delete","Do you want to delete these details?" , parent=self.root)
            if mDelete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query="delete from room where Contact=%s"
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
            else:
                if not mDelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close() 






############## fuinction for reset data ############

        def reset(self):
            self.var_contact.set(""),
            self.var_checkin.set(""),
            self.var_chectout.set(""),
            self.var_roomtype.set(""),
            self.var_roomavailable.set(""),
            self.var_meal.set(""),
            self.var_noOfdays.set("")
            self.var_paidtax.set(""),
            self.var_actualtotal.set(""),
            self.var_total.set("")


  




###################################### All fetched Data ##########################

        def Fetch_contact(self):
            if self.var_contact.get()=="":
                messagebox.showerror("Erorr","Please enter the contact number ",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query=("select Name from employeedetails where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


# if data is not availbe (the search data)
                if row == None:
                    messagebox.showerror("Erorr","Number not found",parent=self.root)
                else:
                    conn.commit()
                    conn.close()


                    showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                    showDataframe.place(x=440,y=60,width=300,height=205)

                    lblName=Label(showDataframe,text="Name :",font=("arial",12,"bold"))

                    lblName.place(x=0,y=0)

                # to show the data from the database right side

                    lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                    lbl.place(x=90,y=0)








                # for the gender part


                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query=("select Gender from employeedetails where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                # show data frame


                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=440,y=60,width=300,height=205)

                lblName=Label(showDataframe,text="Name :",font=("arial",12,"bold"))

                lblName.place(x=0,y=0)


                # label to display the data of gender


                lblgender=Label(showDataframe,text="Gender :",font=("arial",12,"bold"))

                lblgender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)







                # email
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query=("select Email from employeedetails where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email :",font=("arial",12,"bold"))

                lblEmail.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)





                # nationality

                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query=("select Nationality from employeedetails where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality :",font=("arial",12,"bold"))

                lblNationality.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)



                # address

                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query=("select Address from employeedetails where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address :",font=("arial",12,"bold"))

                lblAddress.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)





#############################  SEARCH SYSTEM ###################

        def search(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.room_Table.delete(*self.room_Table.get_children())
                    for i in rows:
                        self.room_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()  





############ function to calculate the time stayed automatically ###########



        def total(self):
                        indate=self.var_checkin.get()
                        outdate=self.var_chectout.get()
                        indate=datetime.strptime(indate,"%d/%m/%Y")
                        outdate=datetime.strptime(outdate,"%d/%m/%Y")
                        self.var_noOfdays.set(abs(outdate-indate).days)

# breakfast  + single

                        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
                            q1=float(300)
                            q2=float(700)
                            q3=float(self.var_noOfdays.get())

                            q4=float(q1+q2)
                            q5=float(q4*q3)

                            Tax="Rs."+str("%.2f"%((q5)*0.1))
                            ST= "Rs."+str("%.2f"%((q5)))
                            TT="Rs."+str("%.2f"%((q5+((q5)*0.1))))
                            self.var_paidtax.set(Tax)
                            self.var_actualtotal.set(ST)
                            self.var_total.set(TT)

#     luxuary + allmeal


                        elif (self.var_meal.get()=="AllMeal" and self.var_roomtype.get()=="Luxuary"):
                            q1=float(900)
                            q2=float(2100)
                            q3=float(self.var_noOfdays.get())

                            q4=float(q1+q2)
                            q5=float(q4*q3)

                            Tax="Rs."+str("%.2f"%((q5)*0.1))
                            ST= "Rs."+str("%.2f"%((q5)))
                            TT="Rs."+str("%.2f"%((q5+((q5)*0.1))))
                            self.var_paidtax.set(Tax)
                            self.var_actualtotal.set(ST)
                            self.var_total.set(TT)


#  single + all

                        elif (self.var_meal.get()=="AllMeal" and self.var_roomtype.get()=="Single"):
                            q1=float(900)
                            q2=float(700)
                            q3=float(self.var_noOfdays.get())

                            q4=float(q1+q2)
                            q5=float(q4*q3)

                            Tax="Rs."+str("%.2f"%((q5)*0.1))
                            ST= "Rs."+str("%.2f"%((q5)))
                            TT="Rs."+str("%.2f"%((q5+((q5)*0.1))))
                            self.var_paidtax.set(Tax)
                            self.var_actualtotal.set(ST)
                            self.var_total.set(TT)



#  double + all

                        elif (self.var_meal.get()=="AllMeal" and self.var_roomtype.get()=="Double"):
                            q1=float(900)
                            q2=float(1400)
                            q3=float(self.var_noOfdays.get())

                            q4=float(q1+q2)
                            q5=float(q4*q3)

                            Tax="Rs."+str("%.2f"%((q5)*0.1))
                            ST= "Rs."+str("%.2f"%((q5)))
                            TT="Rs."+str("%.2f"%((q5+((q5)*0.1))))
                            self.var_paidtax.set(Tax)
                            self.var_actualtotal.set(ST)
                            self.var_total.set(TT)




# adding the show data frame

                            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                            showDataframe.place(x=440,y=60,width=300,height=205)

                            lblName=Label(showDataframe,text="Name :",font=("arial",12,"bold"))

                            lblName.place(x=0,y=0)





                
                # idnumbeIdproof

                        conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                        my_cursor=conn.cursor()
                        query=("select Idproof from employeedetails where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblIdproof=Label(showDataframe,text="Idproof :",font=("arial",12,"bold"))

                        lblIdproof.place(x=0,y=150)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=150)


                # id number
                        conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                        my_cursor=conn.cursor()
                        query=("select Idnumber from employeedetails where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblIdnumber=Label(showDataframe,text="Idnumber :",font=("arial",12,"bold"))

                        lblIdnumber.place(x=0,y=175)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=175)



















if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
