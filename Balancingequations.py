from tkinter import *
import openpyxl
from tkinter import messagebox
from sympy import Matrix
                                                        
root = Tk()
root.title("Balancing equation")

reactants = []                                         #initialising arrays required in the code
products = []

Reactantlabel = Label(root, text="Reactants:")         #creating input boxes and labels used as part of the GUI interface   
Reactantlabel.grid(row=1,column=1)

Productlabel = Label(root, text="Products:")
Productlabel.grid(row=2,column=1)

Inputreactants = Entry(root,width=30,borderwidth=2)
Inputreactants.grid(row=1,column=2)

Inputproducts = Entry(root,width=30,borderwidth=2)
Inputproducts.grid(row=2,column=2)

Solutionlabel = Label(root, text="Solution:")
Solutionlabel.grid(row=3,column=1)

Outputsolution = Entry(root,width=30,borderwidth=2)
Outputsolution.grid(row=3,column=2)

def solve():

    if (len(Inputreactants.get())==0):                         #performing presence check
        messagebox.showinfo("Error","No reactant input")
  
    elif (len(Inputproducts.get())==0):                        #performing presence check
        messagebox.showinfo("Error","No product input")

    else:    
        reactants=(Inputreactants.get()).replace("","").split(" + ")            #separating each reactant molecule into an array
        products=(Inputproducts.get()).replace("","").split(" + ")              #separating each product molecule into an array
        reactantscopy=(Inputreactants.get()).replace("","").split(" + ")        #creating copy of the arrays
        productscopy=(Inputproducts.get()).replace("","").split(" + ")
        allelements=[]                                                          #array of all the elements
        allelementsandnumbersreactants=[]                                       #initialising arrays required in the code
        allelementsandnumbersproducts=[]
        allelementmatrix=[]
        for i in range (len(reactants)):                                        
            elementsandnumbersseparate=[]                                       #initialising array required in the code that will store the elements and their number of molecules separately
            while(len(reactants[i])>0):
                
                if (len(reactants[i])>1):
                    
                    if (ord((reactants[i])[1])>=48) and (ord((reactants[i])[1])<=57): #Since elements come as one capital letter or one capital letter and one lowercase letter followed by a number of molecules of that element, checks to see if the second value of the reactant is a number indicating a one capital letter element
                        elementsandnumbersseparate.append((reactants[i])[0])
                        check=0
                        if (len(allelements)==0):                               #sees if array is empty and adds the element if it is
                            allelements.append((reactants[i])[0])    
                        else:
                            for g in range (len(allelements)):                  #sees if array already contains the element and adds a value to the check if it did
                                if allelements[g]==(reactants[i])[0]:
                                    check=1
                            if (check==0):
                                allelements.append((reactants[i])[0])           #if the check has stayed as 0, the array doesnt contain the element and the element is added
                        reactants[i]=(reactants[i])[1:]                         #removes the first value from the string
                        b=0
                        for a in range (len(reactants[i])):
                            if (((ord((reactants[i])[a])<48) or (ord((reactants[i])[a])>57)) and b==0): #since the number of molecules doesnt have to be only one digit, checks to see how long the digit is
                                b=a                                                                     
                        if (b!=0):
                            elementsandnumbersseparate.append((reactants[i])[:b]) #adds the number of molecules to an array
                            reactants[i]=(reactants[i])[(b):]                     #removes the number of molecules from the reactant
                        else:
                            elementsandnumbersseparate.append(reactants[i])       #adds the number of molecules to an array
                            reactants[i]=""                                       #removes the number of molecules from the reactant

                    elif ((ord((reactants[i])[1])>=65) and (ord((reactants[i])[1])<=90)): #checks to see if the second value was instead a lowercase letter
                          elementsandnumbersseparate.append((reactants[i])[0])
                          check=0
                          if (len(allelements)==0):                               #same check to see if element has been inputed already
                              allelements.append((reactants[i])[0])    
                          else:
                              for g in range (len(allelements)):
                                  if allelements[g]==(reactants[i])[0]:
                                      check=1
                              if (check==0):                                      
                                  allelements.append((reactants[i])[0])
                          reactants[i]=(reactants[i])[1:]
                          elementsandnumbersseparate.append('1')
                          
                    else:                                                        
                        elementsandnumbersseparate.append((reactants[i])[:2])     #The only other alternative is that two capital characters denoting two elements comes back to back 
                        check=0
                        if (len(allelements)==0):
                            allelements.append((reactants[i])[:2])    
                        else:
                            for g in range (len(allelements)):
                                if (allelements[g]==(reactants[i])[:2]):
                                    check=1
                            if (check==0):
                                allelements.append((reactants[i])[:2])
                        reactants[i]=(reactants[i])[2:]
                        b=0
                        if (len(reactants[i])==0):
                            elementsandnumbersseparate.append('1')              #Since no number of atoms of the elements is specified in this case, 1 is given as the number of atoms
                        else:
                            for a in range (len(reactants[i])):
                                if (((ord((reactants[i])[a])<48) or (ord((reactants[i])[a])>57)) and b==0):
                                    b=a
                            if ((ord((reactants[i])[0])<48) or (ord((reactants[i])[0])>57)):
                                elementsandnumbersseparate.append('1')
                            elif (b!=0):
                                elementsandnumbersseparate.append((reactants[i])[:b])
                                reactants[i]=(reactants[i])[(b):]
                            else:
                                elementsandnumbersseparate.append(reactants[i])
                                reactants[i]=""
                else:
                    elementsandnumbersseparate.append(reactants[i])                                             #Since the length is equal to one, only a single character elements remains and is inputted
                    check=0
                    if (len(allelements)==0):
                        allelements.append((reactants[i])[0])    
                    else:
                        for g in range (len(allelements)):
                            if allelements[g]==(reactants[i])[0]:
                                check=1
                        if (check==0):
                            allelements.append((reactants[i])[0])
                    reactants[i]=(reactants[i])[1:]
                    elementsandnumbersseparate.append('1')                                                    #Since no number of atoms of the elements is specified in this case, 1 is given as the number of atoms
            allelementsandnumbersreactants.append(elementsandnumbersseparate)

            
        for i in range (len(products)):
            elementsandnumbersseparate=[]                                                                      #The code for products is the same as the code for the reactants so notes can be referenced from there
            while(len(products[i])>0):        
                if (len(products[i])>1): 
                    if (ord((products[i])[1])>=48) and (ord((products[i])[1])<=57):
                        elementsandnumbersseparate.append((products[i])[0])
                        check=0
                        if (len(allelements)==0):
                            allelements.append((products[i])[0])    
                        else:
                            for g in range (len(allelements)):
                                if allelements[g]==(products[i])[0]:
                                    check=1
                            if (check==0):
                                allelements.append((products[i])[0])
                        products[i]=(products[i])[1:]
                        b=0
                        for a in range (len(products[i])):
                            if (((ord((products[i])[a])<48) or (ord((products[i])[a])>57)) and b==0):
                                b=a
                        if (b!=0):
                            elementsandnumbersseparate.append((products[i])[:b])
                            products[i]=(products[i])[(b):]
                        else:
                            elementsandnumbersseparate.append(products[i])
                            products[i]=""
                    elif ((ord((products[i])[1])>=65) and (ord((products[i])[1])<=90)):
                          elementsandnumbersseparate.append((products[i])[0])
                          check=0
                          if (len(allelements)==0):
                              allelements.append((products[i])[0])    
                          else:
                              for g in range (len(allelements)):
                                  if allelements[g]==(products[i])[0]:
                                      check=1
                              if (check==0):
                                  allelements.append((products[i])[0])
                          products[i]=(products[i])[1:]
                          elementsandnumbersseparate.append('1')
                    else:
                        elementsandnumbersseparate.append((products[i])[:2])
                        check=0
                        if (len(allelements)==0):
                            allelements.append((products[i])[:2])    
                        else:
                            for g in range (len(allelements)):
                                if allelements[g]==(products[i])[:2]:
                                    check=1
                            if (check==0):
                                allelements.append((products[i])[:2])
                        products[i]=(products[i])[2:]
                        b=0
                        if (len(products[i])==0):
                            elementsandnumbersseparate.append('1')
                        else:
                            for a in range (len(products[i])):
                                if (((ord((products[i])[a])<48) or (ord((products[i])[a])>57)) and b==0):
                                    b=a
                            if ((ord((products[i])[0])<48) or (ord((products[i])[0])>57)):
                                elementsandnumbersseparate.append('1')
                            elif (b!=0):
                                elementsandnumbersseparate.append((products[i])[:b])
                                products[i]=(products[i])[(b):]
                            else:
                                elementsandnumbersseparate.append(products[i])
                                products[i]=""
                else:
                    elementsandnumbersseparate.append(products[i])
                    check=0
                    if (len(allelements)==0):
                        allelements.append((products[i])[0])    
                    else:
                        for g in range (len(allelements)):
                            if allelements[g]==(products[i])[0]:
                                check=1
                        if (check==0):
                            allelements.append((products[i])[0])
                    products[i]=(products[i])[1:]
                    elementsandnumbersseparate.append('1')
            allelementsandnumbersproducts.append(elementsandnumbersseparate)


        for i in range (len(allelementsandnumbersreactants)):                                                     #Creating a two dimensional array using the reactants and products that will be converted to a matrix and solved
            counter=0
            for a in range (len(allelementsandnumbersreactants[i])//2):
                counter=(a*2)+1
                (allelementsandnumbersreactants[i])[counter]=int((allelementsandnumbersreactants[i])[counter])
        for i in range (len(allelementsandnumbersproducts)):
            counter=0
            for a in range (len(allelementsandnumbersproducts[i])//2):
                counter=(a*2)+1
                (allelementsandnumbersproducts[i])[counter]=(int((allelementsandnumbersproducts[i])[counter]))*-1
        for i in range (len(allelementsandnumbersreactants)):
            matrix=[]
            for a in range (len(allelements)):
                matrixcounter=0
                counter=0
                for b in range (len(allelementsandnumbersreactants[i])//2):
                    counter=(b*2)
                    if (allelements[a]==(allelementsandnumbersreactants[i])[counter]):
                        matrix.append((allelementsandnumbersreactants[i])[counter+1])
                        matrixcounter=1
                if (matrixcounter==0):
                    matrix.append(0)
            allelementmatrix.append(matrix)           
        for i in range (len(allelementsandnumbersproducts)):
            matrix=[]
            for a in range (len(allelements)):
                matrixcounter=0
                counter=0
                for b in range (len(allelementsandnumbersproducts[i])//2):
                    counter=(b*2)
                    if (allelements[a]==(allelementsandnumbersproducts[i])[counter]):
                        matrix.append((allelementsandnumbersproducts[i])[counter+1])
                        matrixcounter=1
                if (matrixcounter==0):
                    matrix.append(0)                
            allelementmatrix.append(matrix)
            
        allelementmatrix=Matrix(allelementmatrix)                     #Turns the two dimensional array into a matrix and solves it
        allelementmatrix=allelementmatrix.transpose()
        finalanswer=allelementmatrix.nullspace()[0]
        low=0
        newmatrixlist=[]
        for i in range (len(finalanswer)):
            if (low==0):                                              #Matrix is given as fractions so to give whole numbers of molecules, every number is divinded by the lowest
                low=finalanswer[i]
            elif (finalanswer[i]<low):
                low=finalanswer[i]
        for i in range (len(finalanswer)):
            newmatrixlist.append((finalanswer[i])/low)

        reactantsoutput=""
        for i in range (len(reactantscopy)):                          #Outputting while putting the correct balanced number of the element/molecule with the correct element/molecule
            if (len(reactantscopy)-1==i):
                reactantsoutput=reactantsoutput+str(newmatrixlist[i])
                reactantsoutput=reactantsoutput+ "(" + reactantscopy[i] + ")"
            else:
                reactantsoutput=reactantsoutput+str(newmatrixlist[i])
                reactantsoutput=reactantsoutput+ "(" + reactantscopy[i] + ")"
                reactantsoutput=reactantsoutput+" + "
                
        productsoutput=""
        for i in range (len(productscopy)):
            if (len(productscopy)-1==i):
                productsoutput=productsoutput+str(newmatrixlist[(i+len(reactantscopy))])
                productsoutput=productsoutput+ "(" + productscopy[i] + ")"
            else:
                productsoutput=productsoutput+str(newmatrixlist[(i+len(reactantscopy))])
                productsoutput=productsoutput+ "(" + productscopy[i] + ")"
                productsoutput=productsoutput+" + "

        Outputsolution.delete(0,END)
        Outputsolution.insert(0,(reactantsoutput + " = " + productsoutput))

def reset():
    allelements=[]                                                #Resetting all arrays and and deleting text in all the boxes
    allelementsandnumbersreactants=[]
    allelementsandnumbersproducts=[]
    allelementmatrix=[]
    elementsandnumbersseparate=[]
    reactants = []
    products = []
    elementsandnumbersseparate=[]
    matrix=[]
    newmatrixlist=[]
    Inputreactants.delete(0,END)
    Inputproducts.delete(0,END)
    Outputsolution.delete(0,END)
     
Solvebutton = Button(root, text="Solve", command=solve)                  #Buttons to perform the necessary code
Solvebutton.grid(row=1,column=3)

resetbutton = Button(root,text="Reset", command=reset)
resetbutton.grid(row=2,column=3)

root.mainloop()
