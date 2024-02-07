from tkinter import *

root = Tk()
root.title("mortgage calc")
root.geometry("500x500")

def payment():
    if amount_entry.get() and down_entry.get() and interest_entry.get() and duration_entry.get(): 
        # convert entry boxes to numbers
        years = int(duration_entry.get())
        months = years * 12
        rate = float(interest_entry.get())
        loan = int(amount_entry.get()) - int(down_entry.get())
        # calculate the loan
        # monthly int rate
        monthly_rate = rate / 100 / 12
        # get payment
        payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
        # format payment
        payment = "{:,.2f}".format(payment)
        # output payment to screen
        payment_label.config(text="Monthly Payment: ${}".format(payment))
    else:
        payment_label.config(text="complete form")


my_label_frame = LabelFrame(root, text="Mortgage Calculator")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# define labels and entry boxes
amount_label = Label (my_frame, text="Loan Amount")
amount_entry = Entry(my_frame, font=("Helvetica", 18))

down_label = Label (my_frame, text="Down Payment")
down_entry = Entry(my_frame, font=("Helvetica", 18))

interest_label = Label (my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("Helvetica", 18))

duration_label = Label (my_frame, text="Loan Duration")
duration_entry = Entry(my_frame, font=("Helvetica", 18))

# put labels and entry boxes on screen

amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1, pady=10)

down_label.grid(row=1, column=0)
down_entry.grid(row=1, column=1, pady=10)

interest_label.grid(row=2, column=0)
interest_entry.grid(row=2, column=1, pady=10)

duration_label.grid(row=3, column=0)
duration_entry.grid(row=3, column=1, pady=10)

# button 
my_button = Button(my_label_frame, text="Calculate Payment", command=payment)
my_button.pack(pady=15)

# output label
payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack(pady=20)

root.mainloop()