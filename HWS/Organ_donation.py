""""
Module Name: Organ_donation.py
Description: This file will allow the actor to donate organs by doing online
registration through the system.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def donate():
    print("Organ Donation Form")

    print(10*"=","Donor Form",10*"=")

    # enter first name
    fname = input("First Name:-")

    # validation for correct data
    if (fname.isalpha()) == True:
        print()
    else:
        print("invalid entry")
        exit()

    # enter last name
    lname = input("Last Name:-")

    # validation for correct data
    if (lname.isalpha()) == True:
        print()
    else:
        print("invalid entry")
        exit()

    # enter mobile number
    mobile = input("Mobile No:-")

    # validation for correct data
    if (mobile.isdigit()):
        print()
    else:
        print("invalid entry")
        exit()

    # enter organ to donate
    organ = input("Organ to donate:" )

    # validation for correct data
    if (organ.isalpha()):
        print()
    else:
        print("invalid entry")
        exit()

    # enter gender
    gender = input("Gender (M/F):")

    # validation for correct data
    if (gender == "M" or gender =="m" or gender=="f" or gender == "F"):
        print()
    else:
        print("invalid entry")
        exit()


    #storing input data if every input data is valid
    if (mobile.isdigit() and lname.isalpha() and fname.isalpha()and
            (gender == "M" or gender =="m" or gender=="f" or gender == "F") and organ.isalpha()):
        f = open("organ.txt", "a")
        f.write("\n")
        f.write("Donor Name:")
        f.write(fname)
        f.write(" ")
        f.write(lname)
        f.write("\t")
        f.write("mobile no:")
        f.write(mobile)
        f.write("\t")
        f.write("Gender:")
        f.write(gender.upper())
        f.write("\t")
        f.write("Organ:")
        f.write(organ)
        f.write("\t")
        f.close()

        # display message if data entry is successful
        print(" Thank You for Saving a Life")
    else:
        exit()