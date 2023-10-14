from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1273x800+0+0")

        self.Nameoftables=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTables=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StrongAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=15,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",35,"bold"),height=1)
        lbltitle.pack(side=TOP,fill=X)

        #====================DataFrame==========================

        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=85,width=1273,height=395)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=10,y=5,width=840,height=350)

        DataFrameRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Prescription")
        DataFrameRight.place(x=860,y=5,width=370,height=350)

        #=====================Buttons frame======================

        # Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        # Buttonframe.place(x=0,y=530,width=1530,height=70)
        Buttonframe = Frame(self.root, bd=16, relief=RIDGE)
        Buttonframe.place(x=0, y=481, width=1273, height=70)

        #======================Details frame=====================

        # Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        # Detailsframe.place(x=0,y=600,width=1530,height=190)
        Detailsframe = Frame(self.root, bd=15, relief=RIDGE)
        Detailsframe.place(x=0, y=553, width=1273, height=134)

        #=======================Dataframeleft=======================

        lblNameTablet=Label(DataFrameLeft,text="Names Of Tablet: ",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftables,state="readonly",font=("arial",12,"bold"),width=25)
        comNameTablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No.:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.ref,width=25)
        txtref.grid(row=1,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblref.grid(row=2,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.Dose,width=25)
        txtref.grid(row=2,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblref.grid(row=3,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.NumberofTables,width=25)
        txtref.grid(row=3,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblref.grid(row=4,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.Lot,width=25)
        txtref.grid(row=4,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblref.grid(row=5,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.Issuedate,width=25)
        txtref.grid(row=5,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblref.grid(row=6,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.ExpDate,width=25)
        txtref.grid(row=6,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblref.grid(row=7,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.DailyDose,width=25)
        txtref.grid(row=7,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblref.grid(row=8,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.sideEffect,width=25)
        txtref.grid(row=8,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblref.grid(row=0,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.FurtherInformation,width=25)
        txtref.grid(row=0,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblref.grid(row=1,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.DrivingUsingMachine,width=25)
        txtref.grid(row=1,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblref.grid(row=2,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.StrongAdvice,width=25)
        txtref.grid(row=2,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblref.grid(row=3,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.HowToUseMedication,width=25)
        txtref.grid(row=3,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblref.grid(row=4,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.PatientId,width=25)
        txtref.grid(row=4,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="NSH Number:",padx=2,pady=6)
        lblref.grid(row=5,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.nhsNumber,width=25)
        txtref.grid(row=5,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblref.grid(row=6,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.PatientName,width=25)
        txtref.grid(row=6,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblref.grid(row=7,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.DateOfBirth,width=25)
        txtref.grid(row=7,column=3)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblref.grid(row=8,column=2,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12),textvariable=self.PatientAddress,width=25)
        txtref.grid(row=8,column=3)

        #=========================DataFrameRight============================

        # self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        # self.txtPrescription.grid(row=0,column=0)
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=36, height=16, padx=2, pady=2)
        self.txtPrescription.grid(row=0, column=0)

        #============================Buttons================================

        btnPrescription = Button(Buttonframe,command=self.iPrectioption, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe,command=self.iPrescriptionData, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,command=self.update, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=19, height=1, padx=2, pady=2)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,command=self.idelete, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=19, height=1, padx=2, pady=2)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command=self.clear, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=19, height=1, padx=2, pady=2)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,command=self.iExit, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnExit.grid(row=0, column=5)

        #============================Table====================================
        #++++++++++++++++++++++++++++ScrollBar++++++++++++++++++++++++++++++++

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=80)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=80)
        self.hospital_table.column("issuedate",width=90)
        self.hospital_table.column("expdate",width=90)
        self.hospital_table.column("dailydose",width=90)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=80)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

    #===========================Functionality Declaration=================================
    def iPrescriptionData(self):
        if self.Nameoftables.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Qwertakhil@2003",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftables.get(),self.ref.get(),self.Dose.get(),self.NumberofTables.get(),self.Lot.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StrongAdvice.get(),self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAddress.get()))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("success","Record has been inserted")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Qwertakhil@2003",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Name_Of_Tablets=%s,Dose=%s,Lot=%s,Issue_Date=%s,Expirie_Date=%s,Daily_Dose=%s,Side_Effect=%s,Strong_Advice=%s,Blood_Pressure=%s,Storage_Advice=%s,NSH_Number=%s,Patient_Name=%s,Date_Of_Birth=%s,Patient_Address=%s where Reference_No=%s",(self.Nameoftables.get(),self.Dose.get(),self.NumberofTables.get(),self.Lot.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StrongAdvice.get(),self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAddress.get(),self.ref.get()))

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Qwertakhil@2003",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftables.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTables.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StrongAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrectioption(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftables.get() + "\n" )
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get() + "\n" )
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get() + "\n" )
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberofTables.get() + "\n" )
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get() + "\n" )
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get() + "\n" )
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get() + "\n" )
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get() + "\n" )
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get() + "\n" )
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get() + "\n" )
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StrongAdvice.get() + "\n" )
        self.txtPrescription.insert(END,"DrivingIsingMachine:\t\t\t"+self.DrivingUsingMachine.get() + "\n" )
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get() + "\n" )
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get() + "\n" )
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get() + "\n" )
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get() + "\n" )
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get() + "\n" )

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Qwertakhil@2003",database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s "
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")


    def clear(self):
        self.Nameoftables.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTables.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StrongAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

root=Tk()
ob=Hospital(root)
root.mainloop()