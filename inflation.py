from tkinter import *

root = Tk() 
root.title("Inflation")
root.geometry("500x500")

def futurevalue():
    if cash_entry.get()  and inflation_entry.get() and years_entry.get():
        cash = int(cash_entry.get())
        rate = float(inflation_entry.get())
        years = int(years_entry.get())
        # calculation
        inflation_rate = rate / 100 
        # annuity calc
        futurevalue = cash * (1 + inflation_rate)**(-years)
        # format
        futurevalue = "{:,.2f}".format(futurevalue)
        # output
        compound_label.config(text="Purchasing Power in Future: ${}".format(futurevalue))
    else:
        compound_label.config(text="complete form")

my_label_frame = LabelFrame(root, text="Inflation")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# defining labesl and entry boxes
cash_label = Label (my_frame, text="Cash")
cash_entry = Entry(my_frame,)

inflation_label = Label (my_frame, text="Inflation %")
inflation_entry = Entry(my_frame,)

years_label = Label (my_frame, text="Years Held")
years_entry = Entry(my_frame,)

# putting labels and entry boxes on screen

cash_label.grid(row=0, column=0)
cash_entry.grid(row=0, column=1, pady=10)

inflation_label.grid(row=2, column=0)
inflation_entry.grid(row=2, column=1, pady=10)

years_label.grid(row=3, column=0)
years_entry.grid(row=3, column=1, pady=10)

# the fucking button that makes shit happen 

my_button = Button(my_label_frame, text="Calculate", command=futurevalue)
my_button.pack(pady=15)

# output label

compound_label = Label(root, text="", font=("helvetica", 18))
compound_label.pack(pady=20)

root.mainloop()