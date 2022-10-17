# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 2, 2018.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to "do nothing".  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.

# Import the json module to allow us to read and write data in JSON format.
import json
import ast
import os
# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSP5110 Requirement: Also enforce a minimum value of 1. See assignment brief.

data = {}
line = ""
tempJson = []
min_players,max_players,duration,min_age = 0,0,0,0
name = "";
main_data = []
def inputInt():
    global min_players
    global duration
    global max_players
    global min_age
    
    if (min_players== "" and max_players == "" and duration == "" and min_age == ""):
        print("--Input something--")
    else:
        min_players = int(input("Minimum number of players:"))
        max_players = int(input("Maximum number of players :"))
        duration = int(input("Average duration of game in minutes :"))
        min_age= int(input("Minimum recommended player age :"))

# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething():
    global name
    n1 = input('Name of game :')
    name = n1.strip()


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
backData = []
def saveData():
    #line={}
    read_file=open("data.txt","r")
    line=(read_file.read())
    print("-----------------")
    print(line)
    print(type(line))
    line22 = ast.literal_eval(line)
    print(line22)
    print("+++++++++++++++++")
    print(type(line22))
    print("---line 22 ------")
    line22.append({'name':name,'min_players':min_players,'max_players':max_players,'duration':duration,'min_age':min_age})
    print("-------append line-----------")
    jsonFinalData = json.dumps(line22)
    print("json-Final-Data",jsonFinalData)
    f=open("data.txt","w")
    f.write(str(jsonFinalData))
    f.close()
    print("----------Game Saved--------------")
    
def readData():
    
    read_file=open("data.txt","r")
    line=(read_file.read())
    
    
    line22 = ast.literal_eval(line)
    global main_data
    main_data = json.dumps(line22)
        
# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Details of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Game Finder Admin Program.')

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
        
    if choice == 'a':
        # Add a new game.
        # See Point 3 of the "Details of admin.py" section of the assignment brief.
        
        inputSomething()
        inputInt()
        saveData()
                  
    elif choice == 'l':
        # List the current games.
        # See Point 4 of the "Details of admin.py" section of the assignment brief.
        readData()
        main_data1=json.loads(main_data)
        print("List of games:")
        
        for ele,i in enumerate(main_data1):
            print(str(ele)+") "+i['name'])

        print("________________end of list____________________________")
             
    elif choice == 's':
        # Search the current games.
        # See Point 5 of the "Details of admin.py" section of the assignment brief.
        readData()
        main_data1=json.loads(main_data)
        n2=input("Type a game name to search for :")
        print("Search results:")
        for ele,i in enumerate (main_data1):
            
            if str(n2) in i['name']:
                print(str(ele)+") "+i['name'])
            
    elif choice == 'v':
        # View a game.
        # See Point 6 of the "Details of admin.py" section of the assignment brief.
        readData()
        main_data1=json.loads(main_data)
        v1=eval(input("Game number to view :"))
        print(type(v1))
        for ele,i in enumerate(main_data1):
            if ele == v1:
                print(i['name'])
                print("Players: "+str(i['min_players'])+" - "+str(i['max_players']))
                print("Duration: "+str(i['duration'])+" minutes")
                print("Minimum Age: "+str(i['min_age']))
   
    elif choice == 'd':
        # Delete a game.
        # See Point 7 of the "Details of admin.py" section of the assignment brief.
        readData()
        main_data1=json.loads(main_data)
        d1=eval(input("Game number to delete :"))
        print(type(d1))
        isBreak = False
        for ele,i in enumerate (main_data1):
            if ele == d1:
                del main_data1[ele]
                jsonFinalData = json.dumps(main_data1)
    
                f=open("data.txt","w")
                f.write(str(jsonFinalData))
                f.close()
                print("isreak"+str(isBreak))
                isBreak = True
                #break
            #print("isOUTreak"+str(isBreak))
            if isBreak == True:
                break  

                
    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Details of admin.py" section of the assignment brief.
        print("Goodbye !")
        os._exit(0)

    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Details of admin.py" section of the assignment brief.
        print("--------------invalid choice---------------------")
