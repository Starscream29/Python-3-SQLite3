
import sqlite3

#
#This file to mostly just hold misc functions that're gonna be called a whole bunch
#

from datetime import datetime

#Validate the date
def Vali_Date(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


    return True

def getLocation():
    LocationResults = 0
    while True:

        succ = input("Enter your location and select from the list")
        succ = "%" + succ + "%"
        conn = sqlite3.connect('./Database.db')
        c = conn.cursor()
        c.execute("select * from locations where city like ? or address like ? or prov like ? or lcode like ?", (succ, succ, succ, succ))

        LocationResults = c.fetchall()

        if LocationResults:
            break
        print("Sorry, your keyword didn't return any results, please try a different keyword")
    a = 0
    b = 5
    while True:
        for n in range(len(LocationResults[a:b])):
            print(n + a, "  :  ", LocationResults[n + a])

        x = input("Enter the number of your intended location or enter X to scroll up or Z to scroll down")
        if x.isdigit() and (a <= int(x) <= a+4):
            return LocationResults[int(x)][0]
            break
        elif x.upper() == 'X' and a >= 0:
            a -= 5
            b -= 5
        elif x.upper() == 'Z':
            a += 5
            b += 5
        else:
            print("Invalid input, try again")
    return 1

def getRequests():
    RequestResults = 0
    while True:

        succ = input("Enter your location and select from the list")
        succ = "%" + succ + "%"
        conn = sqlite3.connect('./Database.db')
        c = conn.cursor()
        c.execute("select* from requests, locations where pickup = lcode and (city like ? or lcode like ?)", (succ, succ))

        RequestResults = c.fetchall()

        if RequestResults:
            break
        print("Sorry, your keyword didn't return any results, please try a different keyword")

    a = 0
    b = 5
    while True:
        for n in range(len(RequestResults[a:b])):
            print(n + a, "  :  ", RequestResults[n + a])

        x = input("Enter the number of your intended request or enter X to scroll up or Z to scroll down")
        if x.isdigit() and (a <= int(x) <= a+4):
            return RequestResults[int(x)][1]
            break
        elif x.upper() == 'X' and a >= 0:
            a -= 5
            b -= 5
        elif x.upper() == 'Z':
            a += 5
            b += 5
        else:
            print("Invalid input, try again")
    return 1