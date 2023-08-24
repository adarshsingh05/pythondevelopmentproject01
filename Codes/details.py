from tkinter import *
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import datetime



class Details:
    def __init__(self,root):
            self.root=root
            self.root.title("Hotel Management System")
            self.root.geometry("1310x580+225+215")

        ################# TITLE ##################
            lbl_title=Label(self.root,text="ROOM MANAGEMENT WINDOWS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            lbl_title.place(x=0,y=0,width=1500,height=50)





        ################ LOGO ########################
            img2=Image.open(r"C:\Users\ADARSH SINGH\OneDrive\Desktop\Python hotel management\hotellleftlogo.jpg")
            img2=img2.resize((230,140),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=100,height=50)


        ############# lable frame #####################
            labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add New Rooms",padx=2,font=("times new roman",14,"bold"))
            labelframeleft.place(x=5,y=50,width=540,height=350)


   #    floor

            lbl_floor=Label(labelframeleft,text="Floor",padx=0,pady=6,font=("arial",12,"bold"),)
            lbl_floor.grid(row=0,column=0)


            # the variable
            self.var_floor=StringVar()

            entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
            entry_floor.grid(row=0,column=1,sticky=W,padx=4)


   #    RoomNo

            lbl_RoomNo=Label(labelframeleft,text="Room No",padx=0,pady=6,font=("arial",12,"bold"),)
            lbl_RoomNo.grid(row=1,column=0)


            # the variable

            self.var_roomno=StringVar()

            entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"))
            entry_RoomNo.grid(row=1,column=1,sticky=W,padx=4)


   #    RoomType

            lbl_RoomType=Label(labelframeleft,text="Room Type",padx=0,pady=6,font=("arial",12,"bold"),)
            lbl_RoomType.grid(row=2,column=0)

            # variable

            self.var_roomtype=StringVar()

            entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=20,font=("arial",13,"bold"))
            entry_RoomType.grid(row=2,column=1,sticky=W,padx=4)



################ buttons ##############


            btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE,)
            btn_frame.place(x=0,y=250,width=530,height=40)


            btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=12)
            btnAdd.grid(row=0,column=0,padx=1)

            btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=12)
            btnUpdate.grid(row=0,column=1,padx=1)

            btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=12)
            btnDelete.grid(row=0,column=2,padx=1)

            btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=12)
            btnReset.grid(row=0,column=3,padx=1)


#  making of frame #  outline for the below table data
            Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("times new roman",14,"bold"))
            Table_Frame.place(x=600,y=55,width=600,height=350)





############### creating the scroll bar  #########
            scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        # creating the table
            self.room_Table=ttk.Treeview(Table_Frame,columns=("Floor","Room No","Room Type",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.room_Table.xview)
            scroll_y.config(command=self.room_Table.yview)



        # to view the data in left window
            self.room_Table.heading("Floor",text="Floor")
            self.room_Table.heading("Room No",text="Room No")
            self.room_Table.heading("Room Type",text="Room Type")


            self.room_Table["show"]="headings"

        # adjusting the width of the columns
            self.room_Table.column("Floor",width=100)
            self.room_Table.column("Room No",width=100)
            self.room_Table.column("Room Type",width=100)



            self.room_Table.pack(fill=BOTH,expand=1)
            # calling the function
            self.fetch_data()

            # binding the get cursor
            self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)


















########################## function to add the data in the workbench ###################
  
  
  
  
    def add_data(self):
            if self.var_floor.get()=="" or self.var_roomtype.get()=="":
                messagebox.showerror("Error","All fields required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                                            
                                                                                                            self.var_floor.get(),
                                                                                                            self.var_roomno.get(),
                                                                                                            self.var_roomtype.get()
                                                                                                           
                                                                                                          
                                                                                                
                    ))
                    conn.commit()
                    # calling the fetch data function
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)




# to show the data on the right side


    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_Table.delete(* self.room_Table.get_children())
                for i in rows:
                    self.room_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()




#  get cursor

    def get_cursor(self,event=""):
            cursor_row=self.room_Table.focus()
            content=self.room_Table.item(cursor_row)
            row=content["values"]




            
            self.var_floor.set(row[0]),
            self.var_roomno.set(row[1]),
            self.var_roomtype.set(row[2])





########### working on update button ###############

    def update(self):
            if self.var_floor.get()=="":
             messagebox.showerror("Error message","Please enter the floor and room number",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                
                                                                                                            self.var_floor.get(),
                                                                                                            self.var_roomtype.get(),
                                                                                                            self.var_roomno.get()
                                                                                                            
                                                                                                            
                                                                                                                                                                                                                                                
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Updated","New Room details has been updates successfully")






# working on the delete button

    def mDelete(self):
       
            mDelete=messagebox.askyesno("Delete","Do you want to delete these details?" , parent=self.root)
            if mDelete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="a8400629408",database="managment")
                my_cursor=conn.cursor()
                query="delete from details where RoomNo=%s"
                value=(self.var_roomno.get(),)
                my_cursor.execute(query,value)
            else:
                if not mDelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()





# working on the reset part

    def reset(self):
            self.var_floor.set(""),
            self.var_roomno.set(""),
            self.var_roomtype.set(""),






if __name__ == "__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()