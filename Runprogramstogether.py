from tkinter import *

root=Tk()
root.title("Selection Window")

def EM():
    import EftoMf #opens the code for Empirical to Molecular
    
def ME():
    import MftoEf #opens the code for Molecular to Empirical

def BE():
    import Balancingequations #opens the code for Balancing Equations

EfMf = Button(root, text="Empirical Formula to Molecular Formula", command=EM) #creates buttons to open the specific code when clicked
EfMf.grid(row=1,column=1)
MfEf = Button(root, text="Molecular Formula to Empirical Formula", command=ME)
MfEf.grid(row=2,column=1)
Be = Button(root, text="Balancing Equations", command=BE)
Be.grid(row=3,column=1)

root.mainloop()
