
import sqlite3
from ValidateInputs import*

def OfferRide(user):
    print("========")
    print("Offering rides:(Mandatory Fields)")

    while True:
        dateInput = input("Please enter the date of your ride (YYYY-MM-DD)> ")
        if Vali_Date(dateInput) is False:
            print("Format incorrect, please enter a date in the YYYY-MM-DD format only (for example: 2018-05-26)")
        else:
            break

    while True:
        seatNumber = GetInteger(input("Please enter the number of seat you are offering> "))
        if seatNumber is not False:
            break

    while True:
        seatPrice = GetInteger(input("Please enter your asking price for each seat ($)> "))
        if seatPrice is not False:
            break

    luggage = input("Please enter a quick luggage description>")

    print("Find a source location")
    locationSrc = getLocation() #Returns LCODE
    print("Find a destination location")
    locationDes = getLocation() #Returns LCODE

    print("========")
    print("Offering rides:(Optional, leave blank if not applicable)")

    carNumber = input("Please enter your car number> ")
    if not carNumber:
        #then no number was given
        carNumber = None


    print("Select enroute location")
    enrouteNumber = input("Please select the number of enroute locations you wish to enter (0 is ok)> ")
    enrouteLocations = [None] * int(enrouteNumber)


    conn = sqlite3.connect('./Database.db')
    c = conn.cursor()
    c.execute("select COALESCE(max(rno)+1,0)from rides")
    currentRNO = c.fetchone()

    c.execute("INSERT INTO rides VALUES(?,?,?,?,?,?,?,?,?)", (currentRNO[0], seatPrice, dateInput, seatNumber, luggage, locationSrc, locationDes, user[0], carNumber))

    for n in range(len(enrouteLocations)):
        enrouteLocations[n] = getLocation()
        c.execute("INSERT INTO enroute VALUES(?,?)", (currentRNO[0], enrouteLocations[n]))

    conn.commit()

    conn.close()

    return True


