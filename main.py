from tkinter import*

#window setup
my_window = Tk()
my_window.title("BMI CALCULATOR")
my_window.minsize(300,200)

#labels info with your weight,height
weight_label = Label(text="Enter Your Weight(Kg)",font=("arial",12))
weight_label.place(x=90,y=30,anchor="center")
height_label = Label(text="Enter Your Height(Cm)",font=("arial",12))
height_label.place(x=90,y=90,anchor="center")

#info label
info_label = Label(text="CALCULATED",font=("arial",10))

#basic entry for weight,height
my_weight_entry = Entry(width=12,font=("arial",12))
my_weight_entry.place(x=90,y=50,anchor="center")
my_height_entry = Entry(width=12,font=("arial",12))
my_height_entry.place(x=90,y=110,anchor="center")

#def func for bmi calculate,
def button_clicked():
    while True:
        global info_label
        info_label.config(text="")
        try:
            bmi = int(my_weight_entry.get())/((int(my_height_entry.get())/100)**2)
            if bmi >= 40:
                info_label.config(text="You are Obesity Class III")
                break
            elif 35 <= bmi <40:
                info_label.config(text="You are Obesity Class II")
                break
            elif 30 <= bmi <35:
                info_label.config(text="You are Obesity Class I")
                break
            elif 25 <= bmi <30:
                info_label.config(text="You are Pre Obesity")
                break
            elif 18.5 <= bmi <25:
                info_label.config(text="You are Normal Weight")
                break
            elif  bmi < 18.5:
                info_label.config(text="You are Underweight")
                break
        except:
            info_label.config(text="Enter a Valid Number!!!")
            break
    info_label.place(x=150, y=160, anchor="center")


#Calculate Button
my_calculate_button = Button(
    text="CALCULATE",font=("calibri",13,"bold"),
    height=3,width=10,relief="raised",border=10,command=button_clicked)
my_calculate_button.place(x=230,y=70,anchor="center")

my_window.mainloop()