#Presidents (CREATE task)

#Our purpose of our program is to inform users about specific presidents of their choosing



#Initialize

import time

import webbrowser

import pandas as pd

data = pd.read_csv("presidents.csv")



num = data["Presidency"].tolist() # what number president they were

name = data["President"].tolist() #The president's name

took = data["Took office"].tolist() #Displays what year the president took office

left = data["Left office"].tolist() #Displays what year the president left office

party = data["Party"].tolist() #Displays the president's political party

image = data["Portrait"].tolist() #Displays an image of the president

home = data["Home state"].tolist() #Displays the president's home state

filter = [] #Array I will use for filtering data in my code



#Functions

#This acts as the menu to take input from the user and uses the function for the chosen information

def PresMenu(menu):

    for i in range(len(name)):

        if menu == name[i]:

            time.sleep(1)

            info = input("What would like to know about the chosen president (Presidency number, Years in office, Background, Portrait)? ").capitalize()

            if info == "Presidency number":

                time.sleep(1)

                getPresNum(info)

            elif info == "Years in office":

                time.sleep(1)

                getPresYr(info)

            elif info == "Background":

                time.sleep(1)

                getPresBg(info)

            elif info == "Portrait":

                time.sleep(1)

                getPresPic(info)

            else:

                print("Please check spelling")



#This function prints the numbered president the chosen president is

def getPresNum(title):

    for i in range(len(name)):

        if menu == name[i]:

            if title == "Presidency number":

                filter.append(num[i])

    print(filter)

    filter.clear()



#This function prints the year the chosen president took and left office

def getPresYr(year):

    for i in range(len(name)):

        if menu == name[i]:

            if year == "Years in office":

                filter.append(took[i])

                filter.append(left[i])

    print(filter)

    filter.clear()



#This function prints the political party and home state of the chosen president

def getPresBg(bg):

    for i in range(len(name)):

        if menu == name[i]:

            if bg == "Background":

                filter.append(party[i])

                filter.append(home[i])

    print(filter)

    filter.clear()



#This function opens a potrait of chosen president and prints url

def getPresPic(pic):

    for i in range(len(name)):

        if menu == name[i]:

            if pic == "Portrait":

                webbrowser.open(image[i])

                filter.append(image[i])

    print(filter)

    filter.clear()



#This is the start of the program to welcome the user and ask for the president they want to learn about

print("Hello, welcome to the U.S. President Info Guide")

while True:

    menu = input("Please enter the name of a president or exit: ").title()
    if menu not in name and menu != "Exit":
        time.sleep(1)
        print("Please check spelling")


    if menu == "Exit":
        break

    PresMenu(menu)







#Sources

#Website name: Whitehousehistory.org

#URL: https://www.whitehousehistory.org/galleries/presidential-portraits

#Article name: Presidential Portraits



#US Presidents dataset

#Website name: code.org

#URL: https://code.org/en-US

#Dataset source: https://www.whitehouse.gov/about-the-white-house/presidents/
