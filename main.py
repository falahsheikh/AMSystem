import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql


window = tk.Tk()
window.configure(bg='white')
window.geometry('1350x700+0+0')
window.title('Student Record System')

window.configure(bg='white')

title_label = tk.Label(window, text = 'STUDENT RECORD SYSTEM', font=('Courier', 30, 'bold'), border=12, relief=tk.GROOVE, bg='grey', foreground='black')
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(window, text='Enter Details', font = ("Courier", 25, 'bold'),bg ="grey",fg ="black", border=12, relief=tk.GROOVE)
detail_frame.place(x=20, y=90, width=420,height=575)

data_frame = tk.Frame(window, border=12, background='lightgrey', relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)


#--------VARIABLES--------#

studentuid=tk.StringVar()
fulllegalname=tk.StringVar()
faculty=tk.StringVar()
dateofbirth=tk.StringVar()
gender=tk.StringVar()
homephone=tk.StringVar()
mobilephone=tk.StringVar()
email=tk.StringVar()
emergencyphone=tk.StringVar()
address=tk.StringVar()

search_by=tk.StringVar()

#-------------------------#


#---------USR_ENT---------#

studentuid_label=tk.Label(detail_frame, text='Student UID', font=('Courier', 17, 'bold'), bg='grey')
studentuid_label.grid(row=0, column=0, padx=2, pady=2)
studentuid_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=studentuid)
studentuid_ent.grid(row=0, column=1,padx=2, pady=2)


fulllegalname_label=tk.Label(detail_frame, text='Full Legal Name', font=('Courier', 17, 'bold'), bg='grey')
fulllegalname_label.grid(row=1, column=0, padx=2, pady=2)
fulllegalname_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=fulllegalname)
fulllegalname_ent.grid(row=1, column=1,padx=2, pady=2)


faculty_label=tk.Label(detail_frame, text='Faculty', font=('Courier', 17, 'bold'), bg='grey')
faculty_label.grid(row=2, column=0, padx=2, pady=2)
faculty_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=faculty)
faculty_ent.grid(row=2, column=1,padx=2, pady=2)


dateofbirth_label=tk.Label(detail_frame, text='Date of Birth', font=('Courier', 17, 'bold'), bg='grey')
dateofbirth_label.grid(row=3, column=0, padx=2, pady=2)
dateofbirth_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=dateofbirth)
dateofbirth_ent.grid(row=3, column=1,padx=2, pady=2)



gender_label=tk.Label(detail_frame, text='Gender', font=('Courier', 16, 'bold'), bg='grey')
gender_label.grid(row=4, column=0, padx=2, pady=2)
gender_ent=ttk.Combobox(detail_frame, font=('Ariel',16),state='readonly',textvariable=gender)
gender_ent['values']=("Male","Female","Prefer Not To Say")
gender_ent.grid(row=4,column=1,padx=2,pady=2)



homephone_label=tk.Label(detail_frame, text='Home Phone', font=('Courier', 17, 'bold'), bg='grey')
homephone_label.grid(row=5, column=0, padx=2, pady=2)
homephone_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=homephone)
homephone_ent.grid(row=5, column=1,padx=2, pady=2)


mobilephone_label=tk.Label(detail_frame, text='Mobile Phone', font=('Courier', 17, 'bold'), bg='grey')
mobilephone_label.grid(row=6, column=0, padx=2, pady=2)
mobilephone_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=mobilephone)
mobilephone_ent.grid(row=6, column=1,padx=2, pady=2)


email_label=tk.Label(detail_frame, text='E-mail', font=('Courier', 17, 'bold'), bg='grey')
email_label.grid(row=7, column=0, padx=2, pady=2)
email_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=email)
email_ent.grid(row=7, column=1,padx=2, pady=2)


emergencyphone_label=tk.Label(detail_frame, text='Emergency Phone', font=('Courier', 17, 'bold'), bg='grey')
emergencyphone_label.grid(row=8, column=0, padx=2, pady=2)
emergencyphone_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=emergencyphone)
emergencyphone_ent.grid(row=8, column=1,padx=2, pady=2)


address_label=tk.Label(detail_frame, text='Address', font=('Courier', 17, 'bold'), bg='grey')
address_label.grid(row=9, column=0, padx=2, pady=2)
address_ent=tk.Entry(detail_frame, border=7, font=('Arial', 17, 'bold'),textvariable=address)
address_ent.grid(row=9, column=1,padx=2, pady=2)

#-------------------------#


#--------FUNCTIONS--------#setting up php admin database with SRS

def fetch_data():
    conn=pymysql.connect(host='localhost', user='root', password='',database='srs1')
    curr=conn.cursor()
    curr.execute('SELECT * FROM datasrs')
    rows=curr.fetchall()
    if len(rows)!=0:
        student_records.delete(*student_records.get_children())
        for row in rows:
            student_records.insert('',tk.END,values=row)
        conn.commit()
    conn.close()


def add_func():
    if studentuid.get()=='' or fulllegalname.get()=='' or faculty.get()=='':
        messagebox.showerror('Error!', 'Please fill in all the fields.')
    else:
        conn=pymysql.connect(host='localhost',user='root',password='',database='srs1')
        curr=conn.cursor()
        curr.execute('INSERT INTO datasrs VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(studentuid.get(),fulllegalname.get(),faculty.get(),dateofbirth.get(),gender.get(),homephone.get(),mobilephone.get(), email.get(),emergencyphone.get(),address.get()))
        conn.commit()
        conn.close()

        fetch_data() #fetch data after adding (UPDATES!)


def get_cursor(event):
    '''This function will provide data on selected rows'''
    cursor_row=student_records.focus()
    content=student_records.item(cursor_row)
    row=content['values']
    studentuid.set(row[0])
    fulllegalname.set(row[1])
    faculty.set(row[2])
    dateofbirth.set(row[3])
    gender.set(row[4])
    homephone.set(row[5])
    mobilephone.set(row[6])
    email.set(row[7])
    emergencyphone.set(row[8])
    address.set(row[9])


def clear():
    '''This is a function will erase the entry text-boxes'''
    studentuid.set('')
    fulllegalname.set('')
    faculty.set('')
    dateofbirth.set('')
    gender.set('')
    homephone.set('')
    mobilephone.set('')
    email.set('')
    emergencyphone.set('')
    address.set('')





def update_func():
    '''updates data according to user input'''
    conn=pymysql.connect(host='localhost',user='root',password='',database='srs1')
    curr=conn.cursor()
    curr.execute('update datasrs set studentuid=%s, fulllegalname=%s, faculty=%s, dateofbirth=%s, gender=%s,homephone=%s, mobilephone=%s, email=%s, emergencyphone=%s, address=%s',(studentuid.get(), fulllegalname.get(),faculty.get(),dateofbirth.get(),gender.get(),homephone.get(),mobilephone.get(), email.get(),emergencyphone.get(),address.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()

#-------------------------#


#--------SELECTIONS-------#
button_frame=tk.Frame(detail_frame,background='lightgrey',border=10, relief=tk.GROOVE)
button_frame.place(x=0,y=460, width=393,height=60)

add_button=tk.Button(button_frame, background='grey',text='Save', border=7, font=('Courier',15,'bold'),width=5,command=add_func)
add_button.grid(row=0,column=0,padx=2,pady=2)


updte_button=tk.Button(button_frame, background='grey',text='Update', border=7, font=('Courier',15,'bold'),width=5,command=update_func)
updte_button.grid(row=0,column=1,padx=2,pady=2)

delete_button=tk.Button(button_frame, background='grey',text='Delete', border=7, font=('Courier',15,'bold'),width=5)
delete_button.grid(row=0,column=2,padx=2,pady=2)

clr_button=tk.Button(button_frame, background='grey',text='Clear', border=7, font=('Courier',15,'bold'),width=5, command=clear)
clr_button.grid(row=0,column=3,padx=2,pady=2)

#-------------------------#


#------DATABASE-FRAME-----#

main_frame=tk.Frame(data_frame,background='white',border=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_records=ttk.Treeview(main_frame,columns=('Student UID','Full Legal Name','Faculty','Date of Birth','Gender','Home Phone','Mobile Phone','E-mail','Emergency Phone','Address'),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_records.yview)
x_scroll.config(command=student_records.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_records.heading('Student UID',text='Student UID')
student_records.heading('Full Legal Name',text='Full Legal Name')
student_records.heading('Faculty',text='Faculty')
student_records.heading('Date of Birth',text='Date of Birth')
student_records.heading('Gender',text='Gender')
student_records.heading('Home Phone',text='Home Phone')
student_records.heading('Mobile Phone',text='Mobile Phone')
student_records.heading('E-mail',text='E-mail')
student_records.heading('Emergency Phone',text='Emergency Phone')
student_records.heading('Address',text='Address')
student_records['show']='headings'


student_records.column('Student UID',width=100)
student_records.column('Full Legal Name',width=100)
student_records.column('Faculty',width=100)
student_records.column('Date of Birth',width=100)
student_records.column('Gender',width=100)
student_records.column('Home Phone',width=100)
student_records.column('Mobile Phone',width=100)
student_records.column('E-mail',width=100)
student_records.column('Emergency Phone',width=100)
student_records.column('Address',width=150)

student_records.pack(fill=tk.BOTH,expand=True)


fetch_data()

student_records.bind('<ButtonRelease 1>',get_cursor)

#-------------------------#


window.mainloop()