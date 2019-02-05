""""
Module Name: Register1.py
Description: This file allow the user to create a new account in the system.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""


def register():
    import re #importing this package for using match funtion for validation of email id

    #print Registration on the Screen
    print("Registration")

    # entering user details
    fname = input("First Name:-")  # enter first name

    if fname.isalpha():            # validation for correct data
        print()
    else:
        print("invalid entry")
        exit()

    lname = input("Last Name:-")    # enter last name

    if lname.isalpha():   # validation for correct data
        print()
    else:
        print("invalid entry")
        exit()

    mobile = input("Mobile No:-")   # enter mobile number

    if mobile.isdigit():  # validation for correct data
        print()
    else:
        print("invalid entry")
        exit()

    mail = input("E-mail:-")  # enter e-mail
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
    if (match == None):  # validation for correct data
        print("invalid mail address")
        exit()
    else:
        print()

    uname = input("Username:-")  # enter username
    if uname.isalnum():  # validation for correct data
        print()
    else:
        print("invalid username")
        exit()

    password = input("Password:-")           # enter password
    cpassword = input("Confirm Password:-")  # enter password again for confirm password
    if password == cpassword:                # validation for correct data
        print()
    else:
        print(" password not match")
        exit()

# storing input data if every input data is correct
    if ((mobile.isdigit()) and (lname.isalpha()) and (fname.isalpha()) and
            (password == cpassword) and (uname.isalnum())):

        f = open("user_details.txt", "a")
        f.write("\n")
        f.write(fname)
        f.write("\t")
        f.write(lname)
        f.write("\t")
        f.write(mobile)
        f.write("\t")
        f.write(mail)
        f.write("\t")
        f.write(uname)
        f.write("\t")
        f.write(password)
        f.close()
        print("Registration successful")  # display message if data entry is successful
    else:
        exit()
