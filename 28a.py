# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:55:44 2024

@author: avina
"""

from tkinter import *

def generate_report():
    name = e1.get()
    usn = e2.get()
    sem = v_sem.get()
    
    # Fetching the marks for each subject
    marks = []
    for spinbox in mark_spinboxes:
        marks.append((spinbox.get()))
    
    # Create a new window for the report
    report_window = Toplevel(r)
    report_window.geometry('600x400')
    report_window.title("Student Grade Report")
    
    # Display the report in the new window
    report_frame = Frame(report_window, width=600, height=400, bg="lightgrey")
    report_frame.pack()

    Label(report_frame, text="Student Grade Report", bg='lightgrey', fg='black', font=('Arial', 16)).pack(pady=10)

    report_text = Text(report_frame, height=15, width=70, bg='white', fg='black')
    report_text.pack(pady=10)

    # Insert the new information
    report_text.insert(END, f"Student Name: {name}\n")
    report_text.insert(END, f"USN: {usn}\n")
    report_text.insert(END, f"Semester: {sem}\n")
    report_text.insert(END, "Marks:\n")
    for i, mark in enumerate(marks):
        report_text.insert(END, f"  Subject {i+1}: {mark}\n")

r = Tk()
r.geometry('800x600')
r.title("Student Grade Card Generator")

f = Frame(r, width=800, height=600, bg="lightblue")
f.pack()

# Form 1: Entry Form
Label(f, text="Enter Student Details", bg='lightblue', fg='black', font=('Arial', 16)).place(x=300, y=5)

# Student Name
Label(f, text="Student Name", bg='lightblue', fg='black', font=('Arial', 12)).place(x=50, y=50)
e1 = Entry(f, width=30)
e1.place(x=200, y=50)

# USN
Label(f, text="USN", bg='lightblue', fg='black', font=('Arial', 12)).place(x=50, y=100)
e2 = Entry(f, width=30)
e2.place(x=200, y=100)

# Semester
Label(f, text="Semester", bg='lightblue', fg='black', font=('Arial', 12)).place(x=50, y=150)
v_sem = StringVar()
s_sem = Spinbox(f, from_=1, to=8, textvariable=v_sem, width=5)
s_sem.place(x=200, y=150)

# Marks Entry
Label(f, text="Enter Marks", bg='lightblue', fg='black', font=('Arial', 12)).place(x=50, y=200)

mark_spinboxes = []
for i in range(5):  # Assuming 5 subjects
    Label(f, text=f"Subject {i+1}", bg='lightblue', fg='black', font=('Arial', 12)).place(x=50, y=240 + i*30)
    v = StringVar()
    s = Spinbox(f, from_=0, to=100, textvariable=v, width=5)
    s.place(x=200, y=240 + i*30)
    mark_spinboxes.append(s)

# Button to generate report
Button(f, text='Generate Report', bg='green', fg='white', font=('Arial', 12), command=generate_report).place(x=200, y=400)

r.mainloop()