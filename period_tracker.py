#date time always set to today
#prompt user for username
#prompt to enter symptoms or see graphs
#menu of symptoms - enter a number to record symptom then rate severity (1-5)
#store inputs in file
#line graphs always 30 days past from today's date, even if no symptoms recorded (will show 0 values)

import pandas as pd
import csv
import os
from datetime import datetime
today = datetime.now()

usernames = []

#create the file to store usernames with admin as default
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin")
    default_file.close()

#open the file to APPEND new usernames
with open("user.txt", "r+") as user_file:
    for lines in user_file:
        item = lines.strip()
        usernames.append(item)

#create the csv file to store input symptoms
header = ["DATE", "USERNAME", "SYMPTOM", "SEVERITY", "COUNT"]
data = [["default date", "default username", "default symptom", "default severity", "default count"]]
df = pd.DataFrame(data, columns=header)
if not os.path.exists("symptoms.csv"):
    df.to_csv("symptoms.csv", index=False)

# greeting menu
def menu():
    menu = input("S - input today's symptoms \n"
                 "G - see your monthly graphs \n"
                 "X - exit \n").lower()
    if menu == "s":
        symptoms()
    #    elif menu == "g":
    #        graphs()
    elif menu == "x":
        exit()
    else:
        print("Invalid option, please re-enter")
        menu()


# function to select symptom
def symptoms():
    global symptom
    symptom = ""
    symptom_menu = input("Enter the number to record your symptom: \n"
                         "1 - swollen/tender breasts \n"
                         "2 - irritable \n"
                         "3 - sugar/carb cravings \n"
                         "4 - headaches \n"
                         "5 - tearful/low mood \n"
                         "6 - unmovtivated \n"
                         "7 - difficulty focussing \n"
                         "8 - anxiety/difficulty relaxing \n"
                         "9 - night sweats/hot flushes \n"
                         "0 - fatigue \n"
                         "x - exit menu \n").lower()

    if symptom_menu == "1":
        symptom = "swollen/tender breasts"
        grade()
    elif symptom_menu == "2":
        symptom = "irritable"
        grade()
    elif symptom_menu == "3":
        symptom = "sugar/carb cravings"
        grade()
    elif symptom_menu == "4":
        symptom = "headaches"
        grade()
    elif symptom_menu == "5":
        symptom = "tearful/low mood"
        grade()
    elif symptom_menu == "6":
        symptom = "unmotivated"
        grade()
    elif symptom_menu == "7":
        symptom = "difficulty focussing"
        grade()
    elif symptom_menu == "8":
        symptom = "anxiety /difficulty relaxing"
        grade()
    elif symptom_menu == "9":
        symptom = "night sweats/hot flushes"
        grade()
    elif symptom_menu == "0":
        symptom = "fatigue"
        grade()
    elif symptom_menu == "x":
        exit()
    else:
        print("Invalid entry, please try again \n")
        symptoms()


# function to grade severity of symptom
def grade():
        severity = int(input(f"How would you grade {symptom} (from 1 - 5) \n"))
        if severity <= 0:
            print("Invalid entry, please try again")
            symptoms()
        elif severity >= 6:
            print("Invalid entry, please try again")
            symptoms()
        else:
            print(f"You have graded {symptom} as {severity} out of 5")



        more_symptoms = input("Do you want to record more symptoms? (y/n) ").lower()
        if more_symptoms == "y":
            symptoms()
        elif more_symptoms == "n":
            menu()
        else:
            print("Invalid entry, please try again")
            symptoms()



# function to view graphs
# def graphs():


#log in interface
logged_in = False

while not logged_in:
    username = input("Please enter your username: ")
    if username not in usernames:
        new_user = input("Username not found, try again or press N to create new user ").lower()
        if new_user == "n":
            new_user = input("Please create your username: ")
            usernames.append(new_user)
            logged_in = True
            print(f"Welcome {new_user}, what would you like to do today?")
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{username}")
        elif new_user in usernames:
            print(f"Welcome {new_user}, what would you like to do today?")
            logged_in = True
        else:
            username = input("Please re-enter your username: ")
    else:
        print(f"Hello {username}, what would you like to do today?")
        logged_in = True
        menu()


