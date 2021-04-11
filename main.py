# Front end

from tkinter import *
import tkinter.messagebox
import stdDatabase_BackEnd

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database management System")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        # create variables
        StdID = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Email = StringVar()
        Gender = StringVar()

        # ************************************function*********************************

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
            return

        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtgnd.delete(0,END)
            self.txteml.delete(0,END)

        def addData():
            if(len(StdID.get()) !=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Email.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Email.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.viewData():
                studentlist.insert(END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtsna.delete(0,END)
            self.txtsna.insert(END,sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtgnd.delete(0,END)
            self.txtgnd.insert(END,sd[6])
            self.txteml.delete(0,END)
            self.txteml.insert(END,sd[7])

        def DeleteData():
            if(len(StdID.get()) !=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()


        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.searchData(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Email.get()):
                studentlist.insert(END,row,str(""))

        def Update():
            if (len(StdID.get()) != 0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(),Gender.get(), Email.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), FirstName.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Email.get()))



        #************************************frame************************************
                
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Student Database management System",
                            bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('arial', 20, 'bold'), text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White", font=('arial', 20, 'bold'), text="Student details\n")
        DataFrameRIGHT.pack(side=RIGHT)

 # ************************************LABELS AND ENTRIES WIDGET************************************

        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID", padx=2, pady=2, bg="Ghost White")
        self.lblStdID. grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="First name", padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=FirstName, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblsna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname", padx=2, pady=2,bg="Ghost White")
        self.lblsna.grid(row=2, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtsna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblgnd = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender", padx=2, pady=2, bg="Ghost White")
        self.lblgnd.grid(row=5, column=0, sticky=W)
        self.txtgnd = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtgnd.grid(row=5, column=1)

        self.lbleml = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Email", padx=2, pady=2, bg="Ghost White")
        self.lbleml.grid(row=6, column=0, sticky=W)
        self.txteml = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Email, width=39)
        self.txteml.grid(row=6, column=1)
        #============================================List box and scrollbar widget=======================================================

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky="ns")

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)

        #==============================================Button Widget=================================================================
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command = addData)
        self.btnAddData.grid(row = 0, column = 0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), width=10, height=1, bd=4, command = DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), width=10, height=1, bd=4, command = clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), width=10, height=1, bd=4, command = DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), width=10, height=1, bd=4, command = searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.UpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), width=10, height=1, bd=4, command=Update)
        self.UpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), width=10, height=1, bd=4, command = iExit)
        self.btnExit.grid(row=0, column=6)

if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
