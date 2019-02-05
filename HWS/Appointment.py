"""
Module Name: Appointment.py
Description: This file allow user to take appointment for a particular doctor.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def appoint():
    print("Appointment\n")

    #Want to take appointment ??
    app = input("Take an appointment (Y/N)?")

    if app == "Y" or app== "y":
        with open("user_details.txt", "a") as f:
            f.write("\n")

            dname = input("Doctor Name:-")#entering doctor name

            # validation for correct data
            if dname.isalpha():
                print()
            else:
                print("invalid name")
                exit()

            # entering patient name
            fname = input("Patient Username:-")

            # validation for correct data
            if fname.isalpha():
                print()
            else:
                print("invalid entry")
                exit()

            # entering mobile number of the patient
            mobile = input("Mobile No:-")

            # validation for correct data
            if mobile.isdigit():
                print()
            else:
                print("invalid entry")
                exit()

    # opening file to save data
    f = open("patient.txt", "a")
    f.write("\n")

    #Storing input data into the file
    if(mobile.isdigit() and fname.isalpha() and dname.isalpha()):

        #writing the input data in the file
        f.write("patient name:")
        f.write(fname)
        f.write("\t")
        f.write("mobile no:")
        f.write(mobile)
        f.write("\t")
        f.write("doctor name:")
        f.write(dname)
        f.write("\t")
        f.close()

        #displaying the confirmation message after storing the data
        print("confirmation message will be send")
    else:
        exit()