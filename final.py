from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x500")

        # Load the background image
        self.bg_image = Image.open("D:\WORKSPACE\py\Intern_Project\HMS_Tkinter\OIP (1).jpeg")  # Replace with your image path
        self.bg_image = self.bg_image.resize((500, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a canvas and set the background image
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create StringVar for username and password
        self.username = StringVar()
        self.password = StringVar()

        # Place the login widgets on the canvas
        self.canvas.create_text(175, 150, text="Username:", font=("arial",20,"bold"), fill="black",)
        self.username_entry = Entry(self.root, textvariable=self.username, font=("times", 20))
        self.canvas.create_window(250, 180, window=self.username_entry)

        self.canvas.create_text(175, 220, text="Password:", font=("arial",20,"bold"), fill="black")
        self.password_entry = Entry(self.root, textvariable=self.password, show='*', font=("times", 20))
        self.canvas.create_window(250, 250, window=self.password_entry)

        self.login_button = Button(self.root, text="Login", command=self.login, bg="green", fg="white", font=("arial", 12, "bold"),width=15,  pady=8)
        self.canvas.create_window(250, 300, window=self.login_button)

    def login(self):
        # Validate the login credentials here (e.g., against a database)
        if self.username.get() == "admin" and self.password.get() == "123456":
            self.root.destroy()  # Close the login window
            self.open_dashboard()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def open_dashboard(self):
        root = Tk()
        ob = Hospital(root)
        root.mainloop()



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1580x800")



        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.TabletCompany=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.Description=StringVar()

        self. PatientName=StringVar()
        self. PatientId=StringVar()
        self. Age=StringVar()
        self.DateOfBirth=StringVar()
        self. Gender=StringVar()
        self. BloodGroup=StringVar()
        self.PatientPhNo=StringVar()
        self. PatientAddress=StringVar()
        self. FurtherInformation=StringVar()





        lb_title=Label(self.root,bd=20,padx=100,text="+ Hospital Management System",fg="red",bg="black",font=("arial",40,"bold"))
        lb_title.pack(side=TOP,fill="x")



        #=================================================== data frame =========================================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=110,width=1535,height=400)


        Dataframe_Left=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arail",12,"bold"),text="Patient Information")
        Dataframe_Left.place(x=15,y=5,width=990,height=350)

        Dataframe_Right=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arail",12,"bold"),text="Prescription")
        Dataframe_Right.place(x=1020,y=5,width=470,height=350)


        # =================================================== button frame============================================


        buttonframe=Frame(self.root,bd=10)
        buttonframe.place(x=0,y=520,width=1535,height=70)


        #===================================================== Details Frame ===========================================

        Detailsframe = Frame(self.root,bd=20,relief=RIDGE,bg="#BAB5B5")
        Detailsframe.place(x=0,y=595,width=1535,height=195)

        # ==================================================== Dataframe_Left ===========================================


        Tablet_Name=Label (Dataframe_Left, font=("arial", 12, "bold"), text="Name Of Tablets", padx=2, pady=6)
        Tablet_Name.grid(row=0, column=0, sticky=W)

        comNameTablet=ttk. Combobox (Dataframe_Left, state="readonly",font=("arial", 12, "bold"),textvariable=self.Nameoftablets, width=33)
        comNameTablet['value']=("Paracetamol","Cetirizine", "Loperamide", "Acetaminophen", "Adderall", "Amlodipine", "Ativan","Aspirin")
        comNameTablet.current(2)
        comNameTablet.grid(row=0, column=1)

        

        ref=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Refence No",padx=2)
        ref.grid(row=1, column=0, sticky=W)
        txtref=Entry (Dataframe_Left, font=("arial", 13, "bold"),textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)


        Dose=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Dose", padx=2, pady=4)
        Dose.grid(row=2, column=0, sticky=W)
        Dose = Entry (Dataframe_Left, font=("arial", 13, "bold"),textvariable=self.Dose, width=35)
        Dose.grid(row=2, column=1)


        No_of_tablets=Label(Dataframe_Left, font=("arial", 12, "bold"), text="No Of Tablets", padx=2, pady=6)
        No_of_tablets.grid(row=3, column=0, sticky=W)
        txt_No_of_tablets=Entry(Dataframe_Left,textvariable=self.NumberofTablets, font=("arial", 13, "bold"), width=35)
        txt_No_of_tablets.grid(row=3, column=1)


        Tablet_Company=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Tablet Company ", padx=2, pady=6)
        Tablet_Company.grid(row=4, column=0, sticky=W)
        txtLot = Entry(Dataframe_Left,textvariable=self.TabletCompany, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)


        issue_Date=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Issue Date ", padx=2, pady=6)
        issue_Date.grid(row=5, column=0, sticky=W)
        issueDate=Entry (Dataframe_Left,textvariable=self.Issuedate, font=("arial", 13, "bold"), width=35)
        issueDate.grid(row=5, column=1)


        Exp_Date=Label (Dataframe_Left, font=("arial", 12, "bold"), text="Exp Date ", padx=2, pady=6)
        Exp_Date.grid(row=6, column=0, sticky=W)
        ExpDate=Entry (Dataframe_Left,textvariable=self.ExpDate, font=("arial", 13, "bold"), width=35)
        ExpDate.grid(row=6,column=1)


        Daily_Dose = Label (Dataframe_Left, font=("arial", 12, "bold"), text="Daily Dose",padx=2, pady=4)
        Daily_Dose.grid(row=7, column=0, sticky=W)
        DailyDose = Entry (Dataframe_Left,textvariable=self.DailyDose, font=("arial", 13, "bold"), width=35)
        DailyDose.grid(row=7, column=1)


        Description=Label (Dataframe_Left, font=("arial", 12, "bold"), text="Description ", padx=2, pady=6)
        Description.grid(row=8, column=0, sticky=W)
        description = Entry (Dataframe_Left,textvariable=self.Description, font=("arial", 13, "bold"), width=35)
        description.grid(row=8, column=1)


        Patient_name=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Patient Name", padx=12, pady=6)
        Patient_name.grid(row=0, column=2, sticky=W)
        Patientname=Entry (Dataframe_Left,textvariable=self. PatientName, font=("arial", 12, "bold"), width=35)
        Patientname.grid(row=0, column=3)


        Patient_Id=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Patient Id", padx=12, pady=6)
        Patient_Id.grid(row=1, column=2, sticky=W)
        PatientId=Entry (Dataframe_Left,textvariable=self. PatientId, font=("arial", 12, "bold"), width=35)
        PatientId.grid(row=1, column=3)


        age = Label (Dataframe_Left, font=("arial", 12, "bold"), text="Age", padx=12, pady=6)
        age.grid(row=2, column=2, sticky=W)
        p_age = Entry (Dataframe_Left,textvariable=self. Age, font=("arial", 12, "bold"), width=35)
        p_age.grid(row=2, column=3, sticky=W)


        DOB = Label(Dataframe_Left, font=("arial", 12, "bold"), text="Date Of Birth", padx=12, pady=6)
        DOB.grid(row=3, column=2, sticky=W)
        DateOfBirth = Entry (Dataframe_Left,textvariable=self.DateOfBirth, font=("arial", 12, "bold"), width=35)
        DateOfBirth.grid(row=3, column=3)


        Gender= Label(Dataframe_Left, font=("arial", 12, "bold"), text="Gender", padx=12, pady=6)
        Gender.grid(row=4, column=2, sticky=W)
        p_gender=ttk. Combobox (Dataframe_Left,textvariable=self. Gender, state="readonly",font=("arial", 12, "bold"), width=33)
        p_gender['value']=("Male", "Female", "Others")
        p_gender.current()
        p_gender.grid(row=4, column=3)


        Blood_Group = Label(Dataframe_Left, font=("arial", 12, "bold"), text="Blood Group", padx=12, pady=6)
        Blood_Group.grid(row=5, column=2, sticky=W)
        BloodGroup=Entry (Dataframe_Left,textvariable= self. BloodGroup ,  font=("arial", 12, "bold"), width=35)
        BloodGroup.grid(row=5, column=3)


        Number=Label (Dataframe_Left, font=("arial", 12, "bold"), text="Patient Ph.No", padx=12, pady=6)
        Number.grid(row=6, column=2, sticky=W)
        ph_Number=Entry (Dataframe_Left,textvariable=self.PatientPhNo,  font=("arial", 12, "bold"), width=35)
        ph_Number.grid(row=6, column=3)


        Patient_Address=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Patient Address", padx=12,pady=6)
        Patient_Address.grid(row=7, column=2, sticky=W)
        PatientAddress=Entry (Dataframe_Left,textvariable=self. PatientAddress,  font=("arial", 12, "bold"), width=35)
        PatientAddress.grid(row=7, column=3)


        Further_info=Label(Dataframe_Left, font=("arial", 12, "bold"), text="Further Information", padx=12)
        Further_info.grid(row=8, column=2, sticky=W)
        Furtherinfo=Entry (Dataframe_Left,textvariable=self. FurtherInformation ,  font=("arial", 12, "bold"), width=35)
        Furtherinfo.grid(row=8, column=3)



        #======================== data frame right

        self.prescription = Text(Dataframe_Right,font=("arail",12,"bold"), width=47 ,bg="black",fg="white", height=16 , padx=2 , pady=4)
        self.prescription .grid(row=0,column=0)


        #========================== Button
        btn_Prescription = Button(buttonframe, command=self.iPrectioption, text="Prescription", bg="#630CA7", fg="white", font=("arial", 12, "bold"), width=22, padx=11, pady=8)
        btn_Prescription.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_Prescription_Data = Button(buttonframe, command=self.PrescriptionData, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=22, padx=11, pady=8)
        btn_Prescription_Data.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        btn_Update = Button(buttonframe, command=self.update_data, text="Update", bg="#0B83C3", fg="white", font=("arial", 12, "bold"), width=22, padx=11, pady=8)
        btn_Update.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        btn_Delete = Button(buttonframe, command=self.idelete, text="Delete", bg="#f44336", fg="white", font=("arial", 12, "bold"), width=20, padx=11, pady=8)
        btn_Delete.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        btn_Clear = Button(buttonframe, command=self.clear, text="Clear", bg="#CA9A09", fg="white", font=("arial", 12, "bold"), width=20, padx=11, pady=8)
        btn_Clear.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

        btn_Exit = Button(buttonframe, command=self.iExit, text="Exit", bg="#06987F", fg="white", font=("arial", 12, "bold"), width=20, padx=10, pady=8)
        btn_Exit.grid(row=0, column=5, padx=5, pady=5, sticky="ew")



        # ================================== Table =============================
        #====================================== Scroll bar ===============

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.Hospital_table = ttk.Treeview(Detailsframe, columns=("Tablet Name", "Reference No", "Dose", "No Of Tablets", "Tablet Company", "Issue Date", "Exp Date", "Daily Dose", "Description", "Patient Name", "Patient Id", "AGE", "Date Of Birth", "Gender", "Blood Group", "Patient Ph.No", "Patient Address", "Further Information"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill="x")
        scroll_y.pack(side=RIGHT, fill="y")

        self.Hospital_table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.configure(command=self.Hospital_table.xview)
        scroll_y.configure(command=self.Hospital_table.yview)

        # Adding headings to the table
        self.Hospital_table.heading("Tablet Name", text="Name Of Tablets")
        self.Hospital_table.heading("Reference No", text="Reference No")
        self.Hospital_table.heading("Dose", text="Dose")
        self.Hospital_table.heading("No Of Tablets", text="No Of Tablets")
        self.Hospital_table.heading("Tablet Company", text="Tablet Company")
        self.Hospital_table.heading("Issue Date", text="Issue Date")
        self.Hospital_table.heading("Exp Date", text="Exp Date")
        self.Hospital_table.heading("Daily Dose", text="Daily Dose")
        self.Hospital_table.heading("Description", text="Description")
        self.Hospital_table.heading("Patient Name", text="Patient Name")
        self.Hospital_table.heading("Patient Id", text="Patient Id")
        self.Hospital_table.heading("AGE", text="AGE")
        self.Hospital_table.heading("Date Of Birth", text="Date Of Birth")
        self.Hospital_table.heading("Gender", text="Gender")
        self.Hospital_table.heading("Blood Group", text="Blood Group")
        self.Hospital_table.heading("Patient Ph.No", text="Patient Ph.No")
        self.Hospital_table.heading("Patient Address", text="Patient Address")
        self.Hospital_table.heading("Further Information", text="Further Information")

        self.Hospital_table["show"] = "headings"

        # Setting column widths
        self.Hospital_table.column("Tablet Name", width=120)
        self.Hospital_table.column("Reference No", width=100)
        self.Hospital_table.column("Dose", width=50)
        self.Hospital_table.column("No Of Tablets", width=100)
        self.Hospital_table.column("Tablet Company", width=120)
        self.Hospital_table.column("Issue Date", width=100)
        self.Hospital_table.column("Exp Date", width=100)
        self.Hospital_table.column("Daily Dose", width=70)
        self.Hospital_table.column("Description", width=100)
        self.Hospital_table.column("Patient Name", width=120)
        self.Hospital_table.column("Patient Id", width=100)
        self.Hospital_table.column("AGE", width=50)
        self.Hospital_table.column("Date Of Birth", width=100)
        self.Hospital_table.column("Gender", width=70)
        self.Hospital_table.column("Blood Group", width=50)
        self.Hospital_table.column("Patient Ph.No", width=100)
        self.Hospital_table.column("Patient Address", width=120)
        self.Hospital_table.column("Further Information", width=120)

        self.Hospital_table.pack(fill=BOTH, expand=1)
        self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.fatch_data()
        
    #================================ Functinality Declaration =============
    def PrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vijayalakshmi", database="my_data")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO hospital (Name_of_tablets, Reference_No, Dose, Numberoftablets, Tablet_Company, IssueDate, ExpDate, DailyDose, Description, PatientName, PatientId, Age, DOB, Gender, BloodGroup, PatientPhNo, PatientAddress, FurtherInfo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.Nameoftablets.get(),
                        self.ref.get(),
                        self.Dose.get(),
                        self.NumberofTablets.get(),
                        self.TabletCompany.get(),
                        self.Issuedate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.Description.get(),
                        self.PatientName.get(),
                        self.PatientId.get(),
                        self.Age.get(),
                        self.DateOfBirth.get(),
                        self.Gender.get(),
                        self.BloodGroup.get(),
                        self.PatientPhNo.get(),
                        self.PatientAddress.get(),
                        self.FurtherInformation.get()
                    )
                )
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been Inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Something went wrong: {err}")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="vijayalakshmi", database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Name_of_tablets=%s, Reference_No=%s, Dose=%s, Numberoftablets=%s, Tablet_Company=%s, IssueDate=%s, ExpDate=%s, DailyDose=%s, Description=%s, PatientName=%s, PatientId=%s, Age=%s, DOB=%s, Gender=%s, BloodGroup=%s, PatientPhNo=%s, PatientAddress=%s, Furtherinfo=%s ",
        (

                        self.Nameoftablets.get(),
                        self.ref.get(),
                        self.Dose.get(),
                        self.NumberofTablets.get(),
                        self.TabletCompany.get(),
                        self.Issuedate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.Description.get(),
                        self.PatientName.get(),
                        self.PatientId.get(),
                        self.Age.get(),
                        self.DateOfBirth.get(),
                        self.Gender.get(),
                        self.BloodGroup.get(),
                        self.PatientPhNo.get(),
                        self.PatientAddress.get(),
                        self.FurtherInformation.get(),
                                                                  
        )
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record has been Updated")


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="vijayalakshmi", database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len (rows) !=0:
            self.Hospital_table.delete(*self.Hospital_table.get_children())
            for i in rows:
                self.Hospital_table.insert("",END,values=i)
                conn.commit()
        conn. close()




    def get_cursor(self, event=""):
        cursor_row=self.Hospital_table.focus()
        content=self.Hospital_table.item(cursor_row)
        row=content ["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.TabletCompany.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Description.set(row[8])
        self.PatientName.set(row[9])
        self.PatientId.set(row[10])
        self.Age.set(row[11])
        self.DateOfBirth.set(row[12])
        self.Gender.set(row[13])
        self.BloodGroup.set(row[14])
        self.PatientPhNo.set(row[15])
        self.PatientAddress.set(row[16])
        self.FurtherInformation.set(row[17])



    def iPrectioption(self):
        self.prescription.insert(END,"Name of Tables:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.prescription.insert(END,"Reference No:\t\t\t" + self.ref.get() + "\n")
        self.prescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
        self.prescription.insert(END,"No of Tablets: \t\t\t" + self.NumberofTablets.get() + "\n")
        self.prescription.insert(END, "Tablet Compant:\t\t\t" + self.TabletCompany.get() + "\n")
        self.prescription.insert(END,"Issue Date:\t\t\t"+ self.Issuedate.get() + "\n")
        self.prescription.insert(END,"Expdate:\t\t\t"+ self.ExpDate.get() +"\n")
        self.prescription.insert(END,"DailyDose: \t\t\t"+ self.DailyDose.get() + "\n")
        self.prescription.insert(END,"Description:\t\t\t"+ self.Description.get() + "\n")
        self.prescription.insert(END,"PatientName:\t\t\t" +self.PatientName.get() + "\n")
        self.prescription.insert(END,"PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.prescription.insert(END,"Age: \t\t\t" + self.Age.get() + "\n")
        self.prescription.insert (END,"DateofBirth:\t\t\t"+self.DateOfBirth.get() + "\n")
        self.prescription.insert (END,"Gender:\t\t\t"+self.Gender.get() + "\n")
        self.prescription.insert (END,"BloodGroup:\t\t\t"+self.BloodGroup.get() + "\n")
        self.prescription.insert(END,"PatientPhNo:\t\t\t"+self.PatientPhNo.get() + "\n")
        self.prescription.insert(END,"PatientAddress:\t\t\t"+ self.PatientAddress. get() + "\n")
        self.prescription.insert(END,"FurtherInformation:\t\t\t" + self.FurtherInformation.get() + "\n")

        

    def idelete(self):
        conn=mysql.connector.connect(host="localhost" ,username="root" ,password="vijayalakshmi", database="my_data" )
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor. execute (query, value)


        conn.commit()
        conn. close()
        self.fatch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self) :
        self .Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.TabletCompany.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.Description.set("")

        self.PatientName.set("")
        self.PatientId.set("")
        self.Age.set ("")
        self.DateOfBirth.set("")
        self.Gender.set("")
        self.BloodGroup.set("")
        self.PatientPhNo.set("")
        self.PatientAddress.set("")
        self.FurtherInformation.set("")
        self.prescription.delete("1.0", END)
    

    def iExit(self) :
        iExit = messagebox.askyesno("Hospital managemnt system", "Confirm you want to exit")
        if iExit > 0:
            root. destroy()
            return








# Create the main application window
root = Tk()
login = Login(root)
root.mainloop()
