import datetime
from ValidateInputs import*

def OfferRide(user):
    print("========")
    print("Offering rides:(mandatory fields)")
    while True:
        dateInput = input("Please enter the date of your ride (YYYY-MM-DD)> ")
        if Vali_Date(dateInput) is False:
            print("Enter date properly you fuck")
        else:
            break
    seatNumber = input("Please enter the number of seat you are offering> ")
    seatPrice = input("Please enter your asking price for each seat ($)> ")
    luggage = input("Please enter a quick luggage description>")
    locationSrc = getLocation(input("Enter your starting location and select from the list")) #Returns LCODE
    locationDes = getLocation(input("Enter your destination location and select from the list")) #Returns LCODE

    print("========")
    print("Offering rides:(Optional, leave blank if not applicable)")

    #TODO: get optional fields, car number and some enroute locations



    #TODO: Finally, smash all these fields into an sqlite insert statement, then go back to membersoptions menu





    return True


