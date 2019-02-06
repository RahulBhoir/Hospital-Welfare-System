""""
Module Name: Launcher.py
Description: This file allow the user to access the complete system.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
print("       Welcome")
print("         TO")
print("HOSPITAL WELFARE SYSTEM")
print("\n")
t = 1
while t!=10:
    #options tos select from
    print("======================================")
    print("SELECT FROM THE OPTION BELOW\n")
    print("1.  REGISTER")
    print("2.  LOGIN")
    print("3.  TAKE APPOINTMENT")
    print("4.  CHECK APPOINTMENT")
    print("5.  ORGAN DONATION")
    print("6.  FIND A DONOR")
    print("7.  PHARMACY")
    print("8.  QUICK DIAGNOSIS")
    print("9.  ADD PRODUCT")
    print("10. EXIT")
    print("\n")
    choice = int(input("Enter Your Choice:"))

    #for registeration of the new user
    if(choice == 1):
        from Register import *

        r.user_details()
        r.validate_details()
        r.store_detail()

     #for login to the system
    elif(choice == 2):
        from Login import *
        Login.login()

    #for taking appointment
    elif(choice == 3):
        from Appointment import *
        app.enter_details()
        app.validate_details()
        app.add_appointment()

    #for checking the apointment list(for doctor)
    elif (choice == 4):
        from Check_Appointment import *
        ca.appoint_details()

    # for organ donation form filling
    elif(choice == 5):
        from Organ_Donation import *
        od.enter_details()
        od.validate()
        od.add_user()

    # for finding a donor
    elif(choice == 6):
        from Find_a_donor import *
        d.donor()


     #for buying medicines online
    elif(choice == 7):
        import Pharmacy
        Pharmacy.buy_product()

    #for getting treatment inforamtion
    elif(choice == 8):
        import Quick_diagnosis
        Quick_diagnosis.quick_diagnosis()

    # for adding product to the database(only for admin)
    elif(choice == 9):
        from Add_Product import *
        ap.product_details()
        ap.validate_product()
        ap.add_product()

    #for exiting the system
    elif (choice == 10):
        exit()
    else:
        print("INVALID CHOICE")
