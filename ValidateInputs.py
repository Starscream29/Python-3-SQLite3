
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

def getLocation(input):
    input = "%" + input + "%"

    conn = sqlite3.connect('./Database.db')
    c = conn.cursor()
    c.execute("select * from locations where city like ? or address like ? or prov like ? or lcode like ?", (input, input, input, input))

    LocationResults = c.fetchall()
    print(LocationResults)
    a = 0
    b = 5

    for n in range(len(LocationResults[a:b])):
        print(n + a, "  :  ", LocationResults[n + a])

    print("Enter the number of your intended location, then hit enter. Enter X to scroll up or Z to scroll down")
    #TODO: read inputs, adjust a and b to show different values, and finally return LCODE of selected location





    return 1