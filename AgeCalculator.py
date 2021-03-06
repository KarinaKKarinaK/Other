from tkinter import *
from PIL import ImageTk, Image
import datetime

root = Tk()
root.title("Age Calculator")
root.geometry("350x295")
root.resizable(0, 0)

#frame background
j = 0
r = 0
for i in range(100):
    c = str(94422+r)
    Frame(root, width=10, height=500, bg="#d"+c).place(x=j, y=0)
    j = j+10
    r = r+1

Frame(root, width=320, height=180, bg="white").place(x=15, y=15)
Frame(root, width=320, height=35, bg="#e8e8e8").place(x=15, y=15)
Frame(root, width=320, height=70, bg="white").place(x=15, y=210)
Label(root, text = "E N T E R   D A T E  O F  B I R T H", bg = "#e8e8e8").place(x=80, y=22)

#Mechanism
def calculate_age():
    b_day = int(birth_year_entry.get())
    b_month = int(birth_month_entry.get())
    b_year = int(birth_day_entry.get())

    today = datetime.date.today()
    b = str(today)
    year = b[0]+b[1]+b[2]+b[3]
    age = int(year) - b_year
    month = b[5]+b[6]

    if int(month)>b_month:
        age2 = int(month) - b_month
    elif int(month)<b_month:
        age=int(year)-(b_year + 1)
        age2=12-((int(month)-b_month)*-1)
    else:
        age2=0
    total_months = age*12+age2

    txt1  = Text(height=1, width=40, border=0)
    txt1.place(x=30, y=220)
    txt1.configure(font=("Helvetica",10))
    txt1.insert(END, " A G E :  {}  Y E A R S  {}  M O N T H S".format((age), (age2)))

    txt2  = Text(height=1, width=40, border=0)
    txt2.place(x=30, y=250)
    txt2.configure(font=("Helvetica",10))
    txt2.insert(END, "I N  M O N T H S :  {}  M O N T H S".format(total_months))


button1 = Button(root, width=15, bg="black", text="C A L C U L A T E", fg='white', font = ("Helvetica", 11),command=calculate_age, border=0)
button1.place(x=100, y=145)

Label(root, text="D A Y", bg="white").place(x=57, y=67)
birth_year_entry = Entry(root, border=0, bg="#e8e8e8", width=5, justify="center")
birth_year_entry.configure(font=("Helvetica", 17, "bold"))
birth_year_entry.place(x=48.8, y=90)

Label(root, text="M O N T H", bg="white").place(x=140, y=67)
birth_month_entry = Entry(root, border=0, bg="#e8e8e8", width=5, justify="center")
birth_month_entry.configure(font=("Helvetica", 15, "bold"))
birth_month_entry.place(x=148.8, y=90)

Label(root, text="Y E A R", bg="white").place(x=248, y=67)
birth_day_entry = Entry(root, border=0, bg="#e8e8e8", width=5, justify="center")
birth_day_entry.configure(font=("Helvetica", 15, "bold"))
birth_day_entry.place(x=248.8, y=90)





root.mainloop()