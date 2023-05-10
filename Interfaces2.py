from tkinter import messagebox
import main
import tkinter as tk


def start_project():
    def Search():
        def ss():
            if SearchText.get() != "":
                var = main.SearchInfo(SearchText.get())
                if var != "Nothing Found!":
                    var2 = "Patient ID:" + var["ID"] + '\n\n' + "Patient Age:" + var["age"] + '\n\n' + \
                           "Patient Address:" + var["address"] + '\n\n' + "Patient Phone Number:" + var[
                               "phone_number"] + '\n\n' + "Patient Insurance:" + var["insurance"] + '\n\n' \
                           + "Patient Medical History:" + var["medical_history"]
                    ResultLabel = tk.Label(root3, text=var2, fg="#FFFFFF", bg="#5D5D81")
                    ResultLabel.config(font=("Century Gothic (Body)", 20))
                    ResultLabel.pack(anchor="center", pady=20)
            else:
                messagebox.showinfo("ERROR", "You Must Enter ID")
        root3 = tk.Tk()
        root3.geometry("700x600")
        root3.title("BlockChain")
        root3.resizable(False, False)
        root3.positionfrom()
        root3.config(bg="#5D5D81")
        header_label3 = tk.Label(root3, text="Medical Health Care Information", fg="#A3D9FF", bg="#5D5D81")
        header_label3.config(font=("Century Gothic (Body)", 20))
        header_label3.pack(anchor="center", pady=10)
        SearchText = tk.Entry(root3)
        button4 = tk.Button(root3, text="Search",
                            command=ss, bg="#3B3355", activebackground="#3B3355", fg="#000000")
        SearchText.config(font=("Century Gothic (Body)", 16))
        button4.config(font=("Century Gothic (Body)", 24))
        SearchText.pack()
        button4.pack()
        root2.destroy()
        root3.mainloop()

    def EnterInfo():
        def en():
            if IDText.get() != "" and ageText.get() != "" and addressText.get() != "" and phoneText.get() != "" and InsuranceText.get() != "" and medicalText.get() != "":
                var = main.EnterInfo(IDText.get(), ageText.get(), addressText.get(), phoneText.get(),
                                     InsuranceText.get(),
                                     medicalText.get())
                messagebox.showinfo("Successfully", var)
            else:
                messagebox.showinfo("ERROR", "You Must Enter All Fields")
        root4 = tk.Tk()
        root4.geometry("600x700")
        root4.title("BlockChain")
        root4.resizable(False, False)
        root4.positionfrom()
        root4.config(bg="#5D5D81")
        header_label4 = tk.Label(root4, text="Medical Health Care Information", fg="#FFFFFF", bg="#5D5D81")
        header_label4.config(font=("Century Gothic (Body)", 20))
        header_label4.pack(anchor="center", pady=10)
        IDLabel = tk.Label(root4, text="Enter patient ID", fg="#000000", bg="#3B3355")
        IDText = tk.Entry(root4)
        IDLabel.config(font=("Century Gothic (Body)", 16))
        IDText.config(font=("Century Gothic (Body)", 16))
        IDLabel.pack(anchor="w", pady=10)
        IDText.pack(anchor="w", pady=10)
        ageLabel = tk.Label(root4, text="Enter patient Age", fg="#000000", bg="#3B3355")
        ageText = tk.Entry(root4)
        ageLabel.config(font=("Century Gothic (Body)", 16))
        ageText.config(font=("Century Gothic (Body)", 16))
        ageLabel.pack(anchor="w", pady=10)
        ageText.pack(anchor="w", pady=10)
        addressLabel = tk.Label(root4, text="Enter patient Address", fg="#000000", bg="#3B3355")
        addressText = tk.Entry(root4)
        addressLabel.config(font=("Century Gothic (Body)", 16))
        addressText.config(font=("Century Gothic (Body)", 16))
        addressLabel.pack(anchor="w", pady=10)
        addressText.pack(anchor="w", pady=10)
        phoneLabel = tk.Label(root4, text="Enter patient Phone Number", fg="#000000", bg="#3B3355")
        phoneText = tk.Entry(root4)
        phoneLabel.config(font=("Century Gothic (Body)", 16))
        phoneText.config(font=("Century Gothic (Body)", 16))
        phoneLabel.pack(anchor="w", pady=10)
        phoneText.pack(anchor="w", pady=10)
        InsuranceLabel = tk.Label(root4, text="Enter patient Insurance", fg="#000000", bg="#3B3355")
        InsuranceText = tk.Entry(root4)
        InsuranceLabel.config(font=("Century Gothic (Body)", 16))
        InsuranceText.config(font=("Century Gothic (Body)", 16))
        InsuranceLabel.pack(anchor="w", pady=10)
        InsuranceText.pack(anchor="w", pady=10)
        medicalLabel = tk.Label(root4, text="Enter patient Medical History", fg="#000000", bg="#3B3355")
        medicalText = tk.Entry(root4)
        medicalLabel.config(font=("Century Gothic (Body)", 16))
        medicalText.config(font=("Century Gothic (Body)", 16))
        medicalLabel.pack(anchor="w", pady=10)
        medicalText.pack(anchor="w", pady=10)
        button4 = tk.Button(root4, text="Save",
                            command=en, bg="#3B3355", activebackground="#3B3355", fg="#22B14C")
        button4.config(font=("Century Gothic (Body)", 24))
        button4.pack()
        root2.destroy()
        root4.mainloop()

    root2 = tk.Tk()
    root2.geometry("500x400")
    root2.title("BlockChain")
    root2.resizable(False, False)
    root2.positionfrom()
    header_label2 = tk.Label(root2, text="Medical Health Care Information", fg="#A3D9FF", bg="#5D5D81")
    button2 = tk.Button(root2, text="Enter Patient", bg="#3B3355", command=EnterInfo, activebackground="#3B3355",
                        fg="#000000")
    button3 = tk.Button(root2, text="Search About Patient", command=Search, bg="#3B3355", activebackground="#3B3355",
                        fg="#000000")
    root2.config(bg="#5D5D81")
    header_label2.config(font=("Century Gothic (Body)", 20))
    button2.config(font=("Century Gothic (Body)", 24))
    button3.config(font=("Century Gothic (Body)", 24))

    root.destroy()
    header_label2.pack(anchor="center", pady=10)
    button2.pack(anchor="center", pady=30)
    button3.pack(anchor="center", pady=30)
    root2.mainloop()


root = tk.Tk()
root.geometry("600x400")
root.title("BlockChain")
root.config(bg="#3B3355")
root.resizable(False, False)
root.positionfrom()
header_label = tk.Label(root, text="Medical Health Care Information", fg="#A3D9FF", bg="#3B3355")
header_label.config(font=("Century Gothic (Body)", 28))
# widgets
button = tk.Button(root, text="Start Project", command=start_project, bg="#5D5D81", activebackground="#5D5D81",
                   fg="#000000")
button.config(font=("Century Gothic (Body)", 24))
st_label = tk.Label(root, text="Created by: Zainab Jamal Hashim", fg="#A3D9FF", bg="#3B3355")
st_label.config(font=("Century Gothic (Body)", 14))
sp_label = tk.Label(root, text="Supervised by:Dr. Amna Atyaa Dawood", fg="#A3D9FF", bg="#3B3355")
sp_label.config(font=("Century Gothic (Body)", 14))
# place of widgets
header_label.pack(pady=20, anchor="center", side="top")
button.pack(pady=60, anchor="center", side="top")
sp_label.pack(anchor="center", pady=5, side="bottom")
st_label.pack(anchor="center", pady=10, side="bottom")
root.mainloop()
