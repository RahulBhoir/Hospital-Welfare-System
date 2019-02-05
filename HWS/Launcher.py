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
        import Register
        Register.register()

     #for login to the system
    elif(choice == 2):
        import Login
        Login.login()

    #for taking appointment
    elif(choice == 3):
        import Appointment
        Appointment.appoint()

    #for checking the apointment list(for doctor)
    elif (choice == 4):
        import Check_appointment
        Check_appointment.check()

    # for organ donation form filling
    elif(choice == 5):
        import Organ_donation
        Organ_donation.donate()

    # for finding a donor
    elif(choice == 6):
        import Find_a_donor
        Find_a_donor.donor()

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
        import Add_product
        Add_product.product()

    #for exiting the system
    elif (choice == 10):
        exit()
    else:
        print("INVALID CHOICE")
