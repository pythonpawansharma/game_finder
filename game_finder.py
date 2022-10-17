# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "game_finder.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 2, 2018.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to "do nothing".  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json

from tkinter import *

class ProgramGUI:
   
    
    def __init__(self):
        
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of game_finder.py" section of the assignment brief. 

        global no_player
        global time_available
        global age_player
        
        root = Tk()
        root.title("Game Finder")
        #root.geometry("500*300")
        heading = Label(root , text="Constraints :",fg="blue",font=14)
        no_player = Label(root, text="Number of players :")
        time_available = Label(root, text="Time available (mins) :")
        age_player = Label(root, text="Age of youngest player :")
        
        heading.grid(row=0 , column=1)
        no_player.grid(row=1,column=0)
        time_available.grid(row=2,column=0)
        age_player.grid(row=3,column=0)

        no_player = Entry(root)
        time_available = Entry(root)
        age_player = Entry(root)

        no_player.grid(row=1, column=1 ,ipadx="5")
        time_available.grid(row=2, column=1, ipadx="5")
        age_player.grid(row=3, column=1, ipadx="5")

        submit = Button(root,text = "Submit" ,command =self.findGames)
        submit.grid(row=8, column=1)

        # -------- Button -------       
        heading1 = Label(root , text="Matching Games:",fg="blue",font=14)
        heading1.grid(row=10 , column=1)
        
        submit1 = Button(root,text = "data from data" ,width=20 )#,command =findGames)
        submit1.grid(row=11, column=1)

        submit2 = Button(root,text = "Ticket to Ride" ,width=20,command =self.tkMessage)
        submit2.grid(row=12, column=1)

        root.mainloop()
  
    def findGames(self):
        #print("you clicked")
        read_file=open("data.txt","r")
        self.data1=(read_file.read())
        self.data=json.loads(self.data1)

        
        print(type(self.data))
        print("--------data is printting now ---------")
    
    

        if (no_player.get() == "" and time_available.get() == "" and age_player.get() == ""):
            print("empty input")
        else:
            print("===========loop  working===========")
            n1,n2,n3=int(no_player.get()),int(time_available.get()),int(age_player.get())
            print(self.data)
            print("self.data",type(self.data))  
            print(n1,n2,n3)
            print("n1 n2 n3",type(n1))
            for ele,i in enumerate(self.data):
                if int((i['min_players']) > n1 or int(i['min_players']) < n1 ):
                    if int(i['duration']) <= n2:
                        if int(i['min_age']) <= n3:
                            print(i['name'])
                        break
        #self.entry.delete(0, 'end')
    def close(self):
        ProgrameGUI().destroy()
    
    
        self.entry.delete(0, 'end')
    
   
    def tkMessage(self):

        tkinter.messagebox.showinfo("Ticket to Ride",)
   
        # This method finds and displays games matching the criteria entered by the user.
        # See the "The findGames() Method of the GUI Class of game_finder.py" section of the assignment brief.
         



# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
