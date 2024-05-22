import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Stock Sentiment Analysis Bot")
root.geometry("500x450")

labels = []  # create an empty list to hold label objects

spacing = Label(root, text="")

# clear function for text
def clear():
    global labels
    
    # loop over the list of labels and destroy each one
    for label in labels:
        label.destroy()
    
    # clear the list of labels
    labels = []
  
     
# Gets the company info input and displays it to the GUI
def get_Company(string):
    global labels
    
    # create label objects and append them to the list
    company_Name = Label(root, text=string)
    
    labels.extend([company_Name])
    
    return company_Name
    
def display_Company(dataLists):
    for dataList in dataLists:

        string = f"{dataList[0]}, {dataList[1]}, {dataList[2]}, \n{str(dataList[3])}"
        get_Company(string)  # call the get_Company() function to create label objects for each dataList
    
    # display label objects
    for label in labels:
        label.pack()
    
    spacing.pack(pady=10)

def CreateDisplay(dataLists):
    #intiates the button frames to the root(body of the GUI)
    button_frame = Frame(root)
    button_frame.pack()

    #these four lines to create and display the buttons, the command calls the named function above.
    clear_button = Button(button_frame, text="Clear Screen", command=clear) 
    clear_button.grid(row=0, column=0)

    get_text_button = Button(button_frame, text="Display Results", command=lambda: display_Company(dataLists))
    get_text_button.grid(row=0, column=1, padx=20)

    root.mainloop()
