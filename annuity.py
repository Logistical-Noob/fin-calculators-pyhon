from tkinter import *

root = Tk() 
root.title("Annuity Calculator")
root.geometry("500x500")

def annuity():
    if investment_entry.get() and contribution_entry.get() and years_entry.get() and return_entry.get():
        investment = int(investment_entry.get())
        principle = int(contribution_entry.get())
        years = int(years_entry.get())
        rate = float(return_entry.get())
        # calculation
        rate_return = rate / 100 
        # annuity calc
        annuity = investment * (1 + rate_return)**(years) + principle * ((1 + rate_return)**(years) - 1) / rate_return
        # format
        annuity = "{:,.2f}".format(annuity)
        # output
        annuity_label.config(text="FV of Annuity: ${}".format(annuity))
    else:
        annuity_label.config(text="complete form")

my_label_frame = LabelFrame(root, text="Annuity Calculator")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# defining labesl and entry boxes
investment_label = Label (my_frame, text="Investment")
investment_entry = Entry(my_frame,)

countribution_label = Label (my_frame, text=" Yearly Contribution")
contribution_entry = Entry(my_frame,)

years_label = Label (my_frame, text="Years")
years_entry = Entry(my_frame,)

return_label = Label (my_frame, text="Expected Return %")
return_entry = Entry(my_frame,)

# putting labels and entry boxes on screen

investment_label.grid(row=0, column=0)
investment_entry.grid(row=0, column=1, pady=10)

countribution_label.grid(row=1, column=0)
contribution_entry.grid(row=1, column=1, pady=10)

years_label.grid(row=2, column=0)
years_entry.grid(row=2, column=1, pady=10)

return_label.grid(row=3, column=0)
return_entry.grid(row=3, column=1, pady=10)

# the fucking button that makes shit happen 

my_button = Button(my_label_frame, text="Calculate Annuity", command=annuity)
my_button.pack(pady=15)

# output label

annuity_label = Label(root, text="", font=("helvetica", 18))
annuity_label.pack(pady=20)

root.mainloop()