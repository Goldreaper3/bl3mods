# Going to try to import only what I need to save on space and calculation time
# My files
from bl3data import BL3Data
from __info_function__ import Create_HotFix_File, FileChoice
from _global_lists import Mod_Header, Reg_hotfix, Search_Results
from _global_lists import List_Info
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import Entry, Button, Label, Tk, StringVar
################################################################################################################################################################
# Global variables
data = BL3Data()
################################################################################################################################################################
#Creates a new window for the user to see and for the commands to be used
def SelectionWindow(Func):
    # Global/Window variables
    SelectionWindow = Tk()
    # Default values for window sizes, can manipulate inside the functions
    w = 500
    h = 350 
    ws = SelectionWindow.winfo_screenwidth()
    hs = SelectionWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # These variables will determine how many things to add to the window as i need them
    Lab, Ent, Butt = 0, 0, 0
    # Generics we can reuse for any task I have created
    Entry_1, Entry_2, Entry_3, Entry_4, Entry_5, Entry_6 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    
    # Used to grab the values the then entry textvariables,
    def Get_Val(Type):
        # Puts information into a queue to be executed later
        if Type == "ModHeader":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Puts the Information to make the file into a queue to be called later
            Mod_Header.extend([A, B, C, D, E, F])
        # Allows for the creation of multiple regular hotixes
        elif Type == "HotFix":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Info is put into a regular hotfix queue for later
            Reg_hotfix.extend([A, B, C, D, E, F])
        # This will search the database for provided information
        elif Type == "Search":
            Search = Entry_1.get()
            Info = data.get_refs_from_data(Search)
            for Details in Info:
                if Details[0] not in Search_Results:
                    Search_Results.append(Details[0])
    
    if Func == "ModHeader":  # Creates a mod file of you to use
        SelectionWindow.title("Mod Header")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h/1.8, x/4, y))

        Lab = 6
        Ent = 6
        Label_1_Text = 'Name of the hotfix file: '
        Label_2_Text = 'The actual mod name: '
        Label_3_Text = 'Author(s) name: '
        Label_4_Text = 'Discription: '
        Label_5_Text = 'Version of this mod: '
        Label_6_Text = 'The catagory in which this mods fits to: '

        Button_1_Text = 'Create Mod Header'
        def Button_1_Command(): return Get_Val("ModHeader")
        Butt = 1

    #This will make the user put hotfix information into a queue to be executed later
    elif Func == "HotFix":
        SelectionWindow.title("Creating Regular Hot Fix. NOTE: Very much a WIP, so things will be buggy")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h/1.2, x, y/10))

        Lab = 6
        Ent = 6
        Label_1_Text = 'Hotfix Type: \n(Package Tuple)'
        Label_2_Text = 'Map Name: \n(Object Name)'
        Label_3_Text = 'JSON Path + _JWP_ Object: \n(Attribute Name)'
        Label_4_Text = 'JSON Attribute: \n("From" Length)'
        Label_5_Text = 'True or type new value: \n("From" Value)'
        Label_6_Text = 'For right now type "", \n(Will give better instructions later when I understand it more): \n("To" Value)'

        Button_1_Text = "Add This Regular Hotfix To The Queue"
        def Button_1_Command(): return Get_Val("HotFix")
        Butt = 1
    
    # The user will search for a word, and puncuation does not matter, but spelling does
    elif Func == "Search":
        SelectionWindow.title("Find All References")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h/4, x*1.8, y))
        
        Lab = 1
        Ent = 1
        Label_1_Text = 'Enter what you want to search for: \nSometimes the program will take a \nwhile to load in all the data, so be patient with it.'

        Button_1_Text = "Search"
        def Button_1_Command(): return Get_Val("Search")
        Butt = 1
    
    # Reuseable variables, saves on code space and looks nicer
    # Labels
    if Lab >= 1:
        Label(SelectionWindow, text=Label_1_Text).grid(row=0)
    if Lab >= 2:
        Label(SelectionWindow, text=Label_2_Text).grid(row=1)
    if Lab >= 3:
        Label(SelectionWindow, text=Label_3_Text).grid(row=2)
    if Lab >= 4:
        Label(SelectionWindow, text=Label_4_Text).grid(row=3)
    if Lab >= 5:
        Label(SelectionWindow, text=Label_5_Text).grid(row=4)
    if Lab >= 6:
        Label(SelectionWindow, text=Label_6_Text).grid(row=5)

    # Entries
    if Ent >= 1:
        Entry(SelectionWindow, textvariable=Entry_1, width=100).grid(row=0, column=1)
    if Ent >= 2:
        Entry(SelectionWindow, textvariable=Entry_2, width=100).grid(row=1, column=1)
    if Ent >= 3:
        Entry(SelectionWindow, textvariable=Entry_3, width=100).grid(row=2, column=1)
    if Ent >= 4:
        Entry(SelectionWindow, textvariable=Entry_4, width=100).grid(row=3, column=1)
    if Ent >= 5:
        Entry(SelectionWindow, textvariable=Entry_5, width=100).grid(row=4, column=1)
    if Ent >= 6:
        Entry(SelectionWindow, textvariable=Entry_6, width=100).grid(row=5, column=1)

    # Buttons
    if Butt >= 1:
        Button(SelectionWindow, font=("Times New Roman", 14), text=Button_1_Text, command=Button_1_Command).grid(row=Lab)
    # if b >= 2:
        # Button(Nwindow, font=("Times New Roman", 14), text=b2text, command=b2command).grid(row=l, column=1)
################################################################################################################################################################
# Main menu.
if __name__ == "__main__":
    MainWindow = tk.Tk()
    MainWindow.title("Hot Fix Generator")
    w = 500
    h = 350 
    ws = MainWindow.winfo_screenwidth()
    hs = MainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    MainWindow.geometry('%dx%d+%d+%d' % (w, h/1.5, x, y))
    Button(text="Add To Mod Header Queue",font=("Times New Roman", 14), command=lambda: SelectionWindow("ModHeader")).grid(row=1)
    Button(text="Add To The HotFix Queue", font=("Times New Roman", 14), command=lambda: SelectionWindow("HotFix")).grid(row=2)
    Button(text="Choose File To Search Through", font=("Times New Roman", 14), command=lambda: FileChoice()).grid(row=3)
    Button(text="Find All References To An Object", font=("Times New Roman", 14), command=lambda: SelectionWindow("Search")).grid(row=4)
    Button(text="Click To Look At Stored information", font=("Times New Roman", 14), command=lambda: List_Info()).grid(row=5)
    Button(text="Click This To Create Your HotFix File", font=("Times New Roman", 14), command=lambda: Create_HotFix_File()).grid(row=6)
    
    #this will pack everything so that I do not have to do it every time
    i = 1
    for c in sorted(MainWindow.children):
        MainWindow.children[c].pack()
        i += 1
    MainWindow.mainloop()
################################################################################################################################################################